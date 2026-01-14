import os
from agent_core import run_agent

# TEMPORARY: hardcoded ONLY for testing
API_KEY = "---"

result = run_agent(
    prompt="List the files in this project.",
    temperature=0.2,
    max_iterations=5,        
    working_directory="./calculator",
    api_key=API_KEY,
)

print(result)
