# AgentWeaver

AgentWeaver is a **local AI agent framework** that runs as a **single executable** and performs controlled operations inside a given working directory using tool-based reasoning.

It is designed to be **simple, local-first, and production-friendly**, without servers, APIs, or frameworks like FastAPI.

---

## What AgentWeaver Does

AgentWeaver accepts a JSON request via **stdin**, processes it using an AI agent, and returns results via **stdout**.

It can:
- List files and folders
- Read file contents
- Write or modify files
- Execute Python scripts
- Answer general questions using an LLM
