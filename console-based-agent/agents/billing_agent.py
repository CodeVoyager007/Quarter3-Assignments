import google.generativeai as genai
from models import UserContext, IssueType
from tools import get_available_tools, RefundTool, UpdateBillingTool, CheckAccountTool
from rich.console import Console
from rich.panel import Panel
from typing import Dict, Any

console = Console()


class BillingAgent:
    """Agent specialized in handling billing-related queries"""
    
    def __init__(self, config):
        self.config = config
        genai.configure(api_key=config.gemini_api_key)
        self.model = genai.GenerativeModel(config.model_name)
        self.tools = [RefundTool(), UpdateBillingTool(), CheckAccountTool()]
    
    def process_query(self, user_input: str, context: UserContext) -> str:
        """Process billing-related queries"""
        console.print(Panel("💳 [Billing Agent] Processing your request...", style="cyan"))
        
        # Create system prompt for billing agent
        system_prompt = f"""
        You are a billing support agent. You can help with:
        - Refunds (only for premium users)
        - Billing information updates
        - Account status checks
        
        Current context:
        - User: {context.name or 'Unknown'}
        - Premium: {context.is_premium_user}
        - Issue Type: {context.issue_type}
        
        Available tools: {[tool.name for tool in self.tools]}
        
        Respond professionally and use appropriate tools when needed.
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
        
        # Check for refund requests
        if "refund" in user_input.lower() and "refund" in available_tools:
            tool_results.append(available_tools["refund"].execute(context))
        
        # Check for billing updates
        if any(word in user_input.lower() for word in ["update", "change", "billing", "payment"]) and "update_billing" in available_tools:
            tool_results.append(available_tools["update_billing"].execute(context))
        
        # Check for account status
        if any(word in user_input.lower() for word in ["account", "status", "check"]) and "check_account" in available_tools:
            tool_results.append(available_tools["check_account"].execute(context))
        
        return "\n".join(tool_results) if tool_results else "" 