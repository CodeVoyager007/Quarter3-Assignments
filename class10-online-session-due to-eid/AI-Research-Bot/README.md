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
3. In Streamlit Cloud settings:
   - Set the main file path to: `class10-online-session-due to-eid/AI-Research-Bot/main.py`
   - Add the following environment variables:
     ```
     OPENROUTER_API_KEY=your_openrouter_api_key
     LITELLM_API_KEY=your_litellm_api_key
     ```
   - Set Python version to 3.11
   - Enable "Always rerun" option

4. The application uses multiple dependency files for compatibility:
   - `requirements.txt` - Standard Python dependencies
   - `packages.txt` - Streamlit Cloud specific dependencies
   - `pyproject.toml` - Project metadata and build configuration

5. After deployment:
   - Check the logs for any installation issues
   - Verify that all dependencies are installed correctly
   - Test each feature to ensure proper functionality

Note: If you encounter any deployment issues:
1. Check the Streamlit Cloud logs for specific error messages
2. Verify that all API keys are set correctly
3. Ensure the main file path is correct
4. Try clearing the cache and redeploying

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgments

- OpenRouter for providing access to multiple LLM models
- LiteLLM for the unified LLM interface
- Streamlit for the web framework
- UV for the package management system
