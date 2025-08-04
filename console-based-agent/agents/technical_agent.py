import google.generativeai as genai
from models import UserContext, IssueType
from tools import get_available_tools, RestartServiceTool, CheckAccountTool
from rich.console import Console
from rich.panel import Panel
from typing import Dict, Any

console = Console()


class TechnicalAgent:
    """Agent specialized in handling technical issues"""
    
    def __init__(self, config):
        self.config = config
        genai.configure(api_key=config.gemini_api_key)
        self.model = genai.GenerativeModel(config.model_name)
        self.tools = [RestartServiceTool(), CheckAccountTool()]
    
    def process_query(self, user_input: str, context: UserContext) -> str:
        """Process technical queries"""
        console.print(Panel("🔧 [Technical Agent] Processing your request...", style="blue"))
        
        # Create system prompt for technical agent
        system_prompt = f"""
        You are a technical support agent. You can help with:
        - Service restarts (only for technical issues)
        - System troubleshooting
        - Performance issues
        - Account status checks
        
        Current context:
        - User: {context.name or 'Unknown'}
        - Premium: {context.is_premium_user}
        - Issue Type: {context.issue_type}
        
        Available tools: {[tool.name for tool in self.tools]}
        
        Respond technically and use appropriate tools when needed.
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
        
        # Check for service restart requests
        if any(word in user_input.lower() for word in ["restart", "reboot", "service", "system"]) and "restart_service" in available_tools:
            service_name = "system"  # Default service name
            # Try to extract service name from user input
            if "restart" in user_input.lower():
                words = user_input.lower().split()
                for i, word in enumerate(words):
                    if word == "restart" and i + 1 < len(words):
                        service_name = words[i + 1]
                        break
            
            tool_results.append(available_tools["restart_service"].execute(context, service_name=service_name))
        
        # Check for account status
        if any(word in user_input.lower() for word in ["account", "status", "check"]) and "check_account" in available_tools:
            tool_results.append(available_tools["check_account"].execute(context))
        
        return "\n".join(tool_results) if tool_results else "" 