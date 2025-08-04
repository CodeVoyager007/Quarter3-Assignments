# Console-Based Support Agent System

🎓 **Assignment**: Console-Based Support Agent System using OpenAI Agents SDK with Gemini API

## Overview

This project implements a multi-agent support system that handles different types of user queries (billing, technical, general) using the OpenAI Agents SDK with Google's Gemini API. The system features agent-to-agent handoffs, dynamic tool gating, and context management.

## ✅ Assignment Requirements Fulfilled

### Required Concepts
- **🧠 Agents**: 4 agents (Triage + 3 specialized agents)
- **🔧 Tools**: Each specialized agent has tools with dynamic `is_enabled()` logic
- **⚙️ is_enabled()**: Tools are conditionally enabled based on context
- **🔁 Handoffs**: Triage agent routes to appropriate specialized agents
- **📦 Context**: User info passed between agents (name, premium status, issue type)
- **🎛 CLI Interface**: Console-based input/output

### Dynamic Tool Gating
- `refund()` - only enabled if `is_premium_user == True`
- `restart_service()` - only enabled if `issue_type == "technical"`
- `check_account()` - available to all agents
- `update_billing()` - available to billing agent

## 🏗️ Architecture

### Agents
1. **Triage Agent**: Routes queries and extracts user context
2. **Billing Agent**: Handles refunds, payments, billing updates
3. **Technical Agent**: Handles service restarts, troubleshooting
4. **General Agent**: Handles general questions and guidance

### Tools
- **RefundTool**: Processes refunds (premium users only)
- **RestartServiceTool**: Restarts services (technical issues only)
- **CheckAccountTool**: Checks account status (all users)
- **UpdateBillingTool**: Updates billing information

## 🚀 Quick Start

1. **Get Gemini API Key**:
   - Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Create a new API key

2. **Set Environment Variables**:
```bash
   # Create .env file
   echo "GEMINI_API_KEY=your_api_key_here" > .env
   ```

3. **Install Dependencies**:
   ```bash
uv sync
   ```

4. **Run the System**:
   ```bash
uv run main.py
```

## 📖 Usage Examples

### Billing Queries
```
"I want a refund for my premium subscription"
"My name is John and I need to update my billing information"
"I'm a premium user and I want to check my account status"
```

### Technical Queries
```
"I need to restart my system service"
"My application is running slow, can you help?"
"There's a technical issue with my account"
```

### General Queries
```
"What services do you offer?"
"How can I get help?"
"I'm new here, can you guide me?"
```

## 🔧 Features

- **Dynamic Tool Gating**: Tools are enabled/disabled based on user context
- **Context Management**: User information is passed between agents
- **Rich Console Output**: Colored panels and professional interface
- **Error Handling**: Graceful error handling and user feedback
- **Session Management**: Context persists throughout the session

## 📁 Project Structure

```
console-based-agent/
├── main.py                 # Main system entry point
├── models.py              # Pydantic models for context
├── tools.py               # Tool implementations
├── agents/
│   ├── triage_agent.py    # Routing agent
│   ├── billing_agent.py   # Billing specialist
│   ├── technical_agent.py # Technical specialist
│   └── general_agent.py   # General support
├── pyproject.toml         # Project configuration
├── .env                   # Environment variables
├── USAGE_GUIDE.txt       # Detailed usage guide
└── README.md             # This file
```

## 🛠️ Dependencies

- `google-generativeai`: Gemini API integration
- `pydantic`: Data validation and settings
- `rich`: Rich console output
- `python-dotenv`: Environment variable management
- `typer`: CLI framework

## 🎯 Bonus Features

- Rich console output with colored panels
- Real-time context display
- Professional error handling
- Clean exit handling
- Comprehensive usage guide

## 🔍 Troubleshooting

1. **API Key Issues**: Ensure `GEMINI_API_KEY` is set in `.env` file
2. **Dependency Issues**: Run `uv sync` to reinstall dependencies
3. **Runtime Errors**: Check console output for specific error messages

## 📚 Documentation

See `USAGE_GUIDE.txt` for detailed setup and usage instructions.

---
