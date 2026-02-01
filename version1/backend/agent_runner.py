import json
import sys
from agent_core import run_agent


def main():
    payload = json.loads(sys.stdin.read())

    required = ["prompt", "temperature", "maxIterations", "workingDirectory", "apiKey"]
    for k in required:
        if k not in payload:
            raise RuntimeError(f"Missing field: {k}")

    result = run_agent(
        prompt=payload["prompt"],
        temperature=payload["temperature"],
        max_iterations=payload["maxIterations"],
        working_directory=payload["workingDirectory"],
        api_key=payload["apiKey"],
    )

    print(result)


if __name__ == "__main__":
    main()
