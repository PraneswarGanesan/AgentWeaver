from google import genai
from google.genai import types
import os

from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.run_python_file import schema_run_python_file
from functions.write_file import schema_write_file
from call_function import call_function


def run_agent(
    prompt: str,
    temperature: float,
    max_iterations: int,
    working_directory: str,
    api_key: str,
):
    """
    Core agent loop with deterministic stopping conditions.
    """

    # ---------- Hard validation ----------
    if not prompt:
        raise RuntimeError("Prompt is required")

    if not api_key:
        raise RuntimeError("API key not provided")

    if not working_directory:
        raise RuntimeError("Working directory not provided")

    if not os.path.isdir(working_directory):
        raise RuntimeError(f"Invalid working directory: {working_directory}")

    if max_iterations <= 0:
        raise RuntimeError("max_iterations must be > 0")

    # ---------- LLM client ----------
    client = genai.Client(api_key=api_key)

    # ---------- System prompt ----------
    system_prompt = """
You are a helpful AI coding agent.

You may:
- Inspect files and directories
- Read file contents
- Modify files
- Execute Python files

Rules:
- All paths MUST be relative to the provided working directory
- Do not access files outside the working directory
- When you have enough information, STOP calling tools and answer
"""

    # ---------- Conversation state ----------
    messages = [
        types.Content(
            role="user",
            parts=[types.Part(text=prompt)]
        )
    ]

    # ---------- Tool registration ----------
    tools = types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_get_file_content,
            schema_run_python_file,
            schema_write_file,
        ]
    )

    # ---------- Generation config ----------
    config = types.GenerateContentConfig(
        tools=[tools],
        system_instruction=system_prompt,
        temperature=temperature,
        max_output_tokens=1024,
        candidate_count=1,
    )

    # ---------- Tool budget (KEY FIX) ----------
    MAX_TOOL_ITERATIONS = min(3, max_iterations - 1)

    # ---------- Agent loop ----------
    for iteration in range(max_iterations):
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=messages,
            config=config,
        )

        if response is None or not response.candidates:
            raise RuntimeError("Malformed response from model")

        # Add model outputs to memory
        for candidate in response.candidates:
            if candidate.content:
                messages.append(candidate.content)

        # 🔴 HARD STOP: tool budget exhausted → force final answer
        if iteration >= MAX_TOOL_ITERATIONS:
            final_response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=messages,
                config=types.GenerateContentConfig(
                    system_instruction=system_prompt,
                    temperature=temperature,
                    max_output_tokens=1024,
                    candidate_count=1,
                ),
            )
            return final_response.text

        # ---------- Tool handling ----------
        if response.function_calls:
            tool_parts = []

            for function_call_part in response.function_calls:
                function_call_result = call_function(
                    function_call_part,
                    working_directory=working_directory,
                )

                if not function_call_result.parts:
                    raise RuntimeError("Tool response has no parts")

                function_response = function_call_result.parts[0].function_response
                if not function_response or function_response.response is None:
                    raise RuntimeError("Invalid function response")

                tool_parts.append(function_call_result.parts[0])

            messages.append(
                types.Content(
                    role="user",
                    parts=tool_parts
                )
            )

        else:
            # ✅ Model decided to stop
            return response.text

    # ---------- Absolute safety exit ----------
    raise RuntimeError(
        f"Agent did not finish within iteration limit ({max_iterations})"
    )
