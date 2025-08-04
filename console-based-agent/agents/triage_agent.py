import google.generativeai as genai
from models import UserContext, IssueType
from rich.console import Console
from rich.panel import Panel
from typing import Tuple, Optional
import re

console = Console()


class TriageAgent:
    """Agent responsible for routing queries to appropriate specialized agents"""
    
    def __init__(self, config):
        self.config = config
        genai.configure(api_key=config.gemini_api_key)
        self.model = genai.GenerativeModel(config.model_name)
    
    def analyze_and_route(self, user_input: str, context: UserContext) -> Tuple[str, IssueType]:
        """Analyze user input and determine which agent should handle it"""
        console.print(Panel("🚦 [Triage Agent] Analyzing your request...", style="yellow"))
        
        # Create system prompt for triage
        system_prompt = """
        You are a triage agent. Analyze the user's query and determine the appropriate issue type.
        
        Issue types:
        - billing: Refunds, payments, billing questions, account charges
        - technical: System issues, service problems, performance, restarts
        - general: General questions, information requests, basic support
        
        Respond with ONLY the issue type (billing, technical, or general).
        """
        
        # Generate response using Gemini
        response = self.model.generate_content([
            system_prompt,
            f"User query: {user_input}"
        ])
        
        # Extract issue type from response
        issue_type = self._extract_issue_type(response.text, user_input)
        
        # Update context
        context.issue_type = issue_type
        
        # Determine if user is premium based on keywords
        self._update_premium_status(context, user_input)
        
        # Extract name if mentioned
        self._extract_user_name(context, user_input)
        
        console.print(Panel(f"📋 Routing to: {issue_type.value.upper()} Agent", style="yellow"))
        
        return response.text, issue_type
    
    def _extract_issue_type(self, ai_response: str, user_input: str) -> IssueType:
        """Extract issue type from AI response or fallback to keyword analysis"""
        response_lower = ai_response.lower().strip()
        
        # Try to extract from AI response first
        if "billing" in response_lower:
            return IssueType.BILLING
        elif "technical" in response_lower:
            return IssueType.TECHNICAL
        elif "general" in response_lower:
            return IssueType.GENERAL
        
        # Fallback to keyword analysis
        user_lower = user_input.lower()
        
        # Billing keywords
        billing_keywords = ["refund", "payment", "billing", "charge", "bill", "money", "cost", "premium", "subscription"]
        if any(keyword in user_lower for keyword in billing_keywords):
            return IssueType.BILLING
        
        # Technical keywords
        technical_keywords = ["restart", "reboot", "service", "system", "error", "bug", "crash", "slow", "performance", "technical"]
        if any(keyword in user_lower for keyword in technical_keywords):
            return IssueType.TECHNICAL
        
        # Default to general
        return IssueType.GENERAL
    
    def _update_premium_status(self, context: UserContext, user_input: str):
        """Update premium status based on user input"""
        user_lower = user_input.lower()
        premium_keywords = ["premium", "vip", "pro", "paid", "subscription"]
        
        if any(keyword in user_lower for keyword in premium_keywords):
            context.is_premium_user = True
            console.print(Panel("⭐ Premium user detected", style="gold"))
    
    def _extract_user_name(self, context: UserContext, user_input: str):
        """Extract user name if mentioned"""
        # Simple name extraction - look for "I am", "my name is", etc.
        name_patterns = [
            r"my name is (\w+)",
            r"i am (\w+)",
            r"i'm (\w+)",
            r"call me (\w+)",
            r"this is (\w+)"
        ]
        
        for pattern in name_patterns:
            match = re.search(pattern, user_input.lower())
            if match:
                context.name = match.group(1).title()
                console.print(Panel(f"👤 User name: {context.name}", style="cyan"))
                break 