# AI Research Assistant 🤖

A powerful AI-powered research assistant that combines multiple AI technologies to help with research tasks. This project was developed as part of a class assignment to explore and integrate various AI technologies including UV, OpenRouter, and LiteLLM.

## Assignment Requirements Fulfillment

This project successfully implements all the required topics from the assignment:

### 00_swarm
- Implemented a swarm architecture using the `swarm_controller.py` orchestrator
- Created multiple specialized agents (summarizer, translator, QA, research paper generator)
- Agents work together through the swarm controller to handle different tasks
- Each agent is modular and can be easily extended or modified

### 01_uv
- Project uses `uv` for dependency management
- All dependencies are specified in `requirements.txt`
- Easy installation using `uv ad -r requirements.txt`
- Ensures consistent and fast package installation across different environments

### 02_openrouter
- Integrated OpenRouter API for accessing multiple LLM models
- Implemented in `openrouter_setup.py`
- Provides access to various AI models through a single API
- Handles authentication and API key management
- Supports different model configurations

### 03_litellm_openai_agent
- Implemented LiteLLM integration in `litellm_setup.py`
- Created a unified interface for different LLM providers
- Supports OpenAI-compatible API calls
- Handles model selection, token management, and response processing
- Enables easy switching between different AI models

## Features

1. **Text Summarization**
   - Generate concise summaries of long texts
   - Multiple summary styles (concise, detailed, bullet points)
   - Customizable length control

2. **English-Urdu Translation**
   - Bidirectional translation between English and Urdu
   - Preserves formality levels
   - Context-aware translation

3. **Question Answering**
   - Context-aware Q&A system
   - Conversation history support
   - Multiple question types handling

4. **Research Paper Generation**
   - Generate structured research papers
   - Customizable sections and length
   - PDF export with proper formatting
   - Academic writing style

### Technology Stack
- **Python 3.11+**: Core programming language
- **Streamlit**: Web interface
- **UV**: Package management
- **OpenRouter**: LLM API access
- **LiteLLM**: LLM abstraction layer
- **FPDF2**: PDF generation
- **Markdown**: Text formatting

## Setup and Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/CodeVoyager007/AI-Research-Bot.git
   cd AI-Research-Bot
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # Linux/Mac
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   # Using UV (recommended)
   uv pip install -r requirements.txt
   
   # Or using pip
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   ```bash
   # Copy the example env file
   cp .env.example .env
   # Edit .env with your API keys
   ```

5. Run the application:
   ```bash
   streamlit run main.py
   ```

### Deployment

For deploying to Streamlit Cloud:

1. Make sure your repository is public
2. Connect your GitHub repository to Streamlit Cloud
3. Set the following environment variables in Streamlit Cloud:
   - `OPENROUTER_API_KEY`
   - `LITELLM_API_KEY` (if using LiteLLM)
   - Any other required API keys

The application will automatically detect the `pyproject.toml` and install dependencies using UV.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgments

- OpenRouter for providing access to multiple LLM models
- LiteLLM for the unified LLM interface
- Streamlit for the web framework
- UV for the package management system
