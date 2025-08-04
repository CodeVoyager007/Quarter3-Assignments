from typing import Any, Dict
from models import UserContext, IssueType
import google.generativeai as genai
from rich.console import Console
from rich.panel import Panel

console = Console()


class BaseTool:
    """Base class for all tools"""
    
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
    
    def is_enabled(self, context: UserContext) -> bool:
        """Override this method to implement dynamic tool gating"""
        return True
    
    def execute(self, context: UserContext, **kwargs) -> str:
        """Execute the tool and return result"""
        raise NotImplementedError


class RefundTool(BaseTool):
    """Tool for processing refunds - only enabled for premium users"""
    
    def __init__(self):
        super().__init__(
            name="refund",
            description="Process a refund for the user's account"
        )
    
    def is_enabled(self, context: UserContext) -> bool:
        """Only enabled if user is premium"""
        return context.is_premium_user
    
    def execute(self, context: UserContext, **kwargs) -> str:
        if not self.is_enabled(context):
            return "❌ Refund tool is not available for non-premium users."
        
        amount = kwargs.get('amount', 'full')
        console.print(Panel(f"💰 Processing {amount} refund for {context.name or 'user'}", style="green"))
        return f"✅ Refund of {amount} has been processed successfully for {context.name or 'user'}."


class RestartServiceTool(BaseTool):
    """Tool for restarting services - only enabled for technical issues"""
    
    def __init__(self):
        super().__init__(
            name="restart_service",
            description="Restart a service on the user's system"
        )
    
    def is_enabled(self, context: UserContext) -> bool:
        """Only enabled for technical issues"""
        return context.issue_type == IssueType.TECHNICAL
    
    def execute(self, context: UserContext, **kwargs) -> str:
        if not self.is_enabled(context):
            return "❌ Service restart is only available for technical issues."
        
        service_name = kwargs.get('service_name', 'default')
        console.print(Panel(f"🔄 Restarting {service_name} service", style="blue"))
        return f"✅ {service_name} service has been restarted successfully."


class CheckAccountTool(BaseTool):
    """Tool for checking account status"""
    
    def __init__(self):
        super().__init__(
            name="check_account",
            description="Check the user's account status and details"
        )
    
    def execute(self, context: UserContext, **kwargs) -> str:
        status = "Premium" if context.is_premium_user else "Standard"
        console.print(Panel(f"📊 Checking account for {context.name or 'user'}", style="yellow"))
        return f"📋 Account Status: {status}\nUser: {context.name or 'Unknown'}\nIssue Type: {context.issue_type or 'Not specified'}"


class UpdateBillingTool(BaseTool):
    """Tool for updating billing information"""
    
    def __init__(self):
        super().__init__(
            name="update_billing",
            description="Update billing information for the user"
        )
    
    def execute(self, context: UserContext, **kwargs) -> str:
        payment_method = kwargs.get('payment_method', 'credit card')
        console.print(Panel(f"💳 Updating billing information", style="cyan"))
        return f"✅ Billing information updated successfully. Payment method: {payment_method}"


# Tool registry
TOOLS = {
    "refund": RefundTool(),
    "restart_service": RestartServiceTool(),
    "check_account": CheckAccountTool(),
    "update_billing": UpdateBillingTool(),
}
def get_available_tools(context: UserContext) -> Dict[str, BaseTool]:
    """Get tools that are enabled for the current context"""
    return {
        name: tool for name, tool in TOOLS.items()
        if tool.is_enabled(context)
    } 