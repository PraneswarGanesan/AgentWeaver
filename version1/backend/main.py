import os
import sys
from config import MAX_ITERATIONS, Temperature
from agent_core import run_agent


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <prompt>")
        sys.exit(1)

    prompt = sys.argv[1]
    api_key = os.environ.get("GEMINI_API_KEY")

    if not api_key:
        raise RuntimeError("GEMINI_API_KEY not set")

    result = run_agent(
        prompt=prompt,
        temperature=Temperature,
        max_iterations=MAX_ITERATIONS,
        api_key=api_key,
    )

    print(result)


if __name__ == "__main__":
    main()
