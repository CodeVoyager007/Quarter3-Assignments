import google.generativeai as genai
from models import UserContext, IssueType
from tools import get_available_tools, CheckAccountTool
from rich.console import Console
from rich.panel import Panel
from typing import Dict, Any

console = Console()


class GeneralAgent:
    """Agent specialized in handling general queries"""
    
    def __init__(self, config):
        self.config = config
        genai.configure(api_key=config.gemini_api_key)
        self.model = genai.GenerativeModel(config.model_name)
        self.tools = [CheckAccountTool()]
    
    def process_query(self, user_input: str, context: UserContext) -> str:
        """Process general queries"""
        console.print(Panel("🤖 [General Agent] Processing your request...", style="green"))
        
        # Create system prompt for general agent
        system_prompt = f"""
        You are a general support agent. You can help with:
        - General questions and information
        - Account status checks
        - Basic troubleshooting guidance
        - Directing users to appropriate specialized agents
        
        Current context:
        - User: {context.name or 'Unknown'}
        - Premium: {context.is_premium_user}
        - Issue Type: {context.issue_type}
        
        Available tools: {[tool.name for tool in self.tools]}
        
        Respond helpfully and guide users to specialized agents when needed.
        """
        
        # Get available tools based on context
        available_tools = get_available_tools(context)
        
        # Generate response using Gemini
        response = self.model.generate_content([
            system_prompt,
            f"User query: {user_input}"
        ])
        
        # Check if we need to use any tools
        tool_result = self._check_and_use_tools(user_input, context, available_tools)
        
        if tool_result:
            return f"{response.text}\n\n{tool_result}"
        
        return response.text
    
    def _check_and_use_tools(self, user_input: str, context: UserContext, available_tools: Dict[str, Any]) -> str:
        """Check if any tools should be used and execute them"""
        tool_results = []
        
        # Check for account status
        if any(word in user_input.lower() for word in ["account", "status", "check"]) and "check_account" in available_tools:
            tool_results.append(available_tools["check_account"].execute(context))
        
        return "\n".join(tool_results) if tool_results else "" 