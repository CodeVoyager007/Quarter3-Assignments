# Bank Agent Mini Project

This project demonstrates the use of OpenAI SDK concepts to build a modular, multi-agent banking assistant with robust input/output guardrails and agent handoffs.

## Features

- **Input Guardrails:** Ensures only bank-related queries are processed.
- **Output Guardrails:** Ensures all responses are safe, policy-compliant, and non-offensive.
- **Multiple Handoff Agents:** Specialized agents for bank teller, loan officer, credit card, and customer support queries.
- **Contextual Validation:** Only registered users (e.g., "Ayesha Mughal") can access sensitive tools.
- **Agent Router:** Automatically routes queries to the appropriate agent based on intent.

## Project Structure

- `main.py` — Main application logic and agent definitions
- `.env` — Environment variables (add your `GEMINI_API_KEY` here)
- `pyproject.toml` — Project dependencies and metadata

## Setup

1. **Clone the repository** and navigate to the project directory.
2. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```
    Or use a tool compatible with `pyproject.toml` (e.g., `pip install .` or `uv`).

3. **Set up your `.env` file:**
    ```
    GEMINI_API_KEY=your_api_key_here
    ```

4. **Run the project:**
    ```sh
    python main.py
    ```

## Example Queries

- "Check my account balance"
- "What is the status of my loan ID 12345?"
- "What is my credit card limit?"
- "I want to file a complaint about ATM cash not dispensing"

## Requirements

- Python 3.10+
- See [pyproject.toml](pyproject.toml) for dependencies

## Notes

- Only the user `"Ayesha Mughal"` with PIN `2162009` can access account tools.
- The project uses [openai-agents](https://pypi.org/project/openai-agents/) and [pydantic](https://docs.pydantic.dev/) for agent orchestration and data validation.

---
