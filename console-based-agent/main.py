import os
import sys
from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.text import Text
from models import UserContext, AgentConfig
from agents.triage_agent import TriageAgent
from agents.billing_agent import BillingAgent
from agents.technical_agent import TechnicalAgent
from agents.general_agent import GeneralAgent

# Load environment variables
load_dotenv()

console = Console()


class SupportAgentSystem:
    """Main system that orchestrates all agents"""
    
    def __init__(self):
        # Get API key from environment
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            console.print(Panel("❌ GEMINI_API_KEY not found in environment variables!", style="red"))
            console.print("Please set your Gemini API key in a .env file or environment variable.")
            sys.exit(1)
        
        # Initialize configuration
        self.config = AgentConfig(gemini_api_key=api_key)
        
        # Initialize agents
        self.triage_agent = TriageAgent(self.config)
        self.billing_agent = BillingAgent(self.config)
        self.technical_agent = TechnicalAgent(self.config)
        self.general_agent = GeneralAgent(self.config)
        
        # Initialize user context
        self.context = UserContext()
    
    def run(self):
        """Main loop for the support system"""
        console.print(Panel.fit(
            "🎓 Console-Based Support Agent System\n"
            "Using OpenAI Agents SDK with Gemini API",
            style="bold blue"
        ))
        
        console.print("\n" + "="*60)
        console.print("Available features:")
        console.print("• Billing support (refunds, payments)")
        console.print("• Technical support (service restarts, troubleshooting)")
        console.print("• General support (information, guidance)")
        console.print("• Dynamic tool gating based on user context")
        console.print("• Agent-to-agent handoffs")
        console.print("="*60 + "\n")
        
        while True:
            try:
                # Get user input
                user_input = Prompt.ask("💬 How can I help you today?")
                
                if user_input.lower() in ['quit', 'exit', 'bye']:
                    console.print(Panel("👋 Thank you for using our support system!", style="green"))
                    break
                
                # Process through triage agent
                triage_response, issue_type = self.triage_agent.analyze_and_route(user_input, self.context)
                
                # Route to appropriate specialized agent
                if issue_type.value == "billing":
                    response = self.billing_agent.process_query(user_input, self.context)
                elif issue_type.value == "technical":
                    response = self.technical_agent.process_query(user_input, self.context)
                else: # general
                    response = self.general_agent.process_query(user_input, self.context)
                
                # Display response
                console.print(Panel(response, title="🤖 Response", style="green"))
                
                # Show context information
                self._display_context()
                
            except KeyboardInterrupt:
                console.print("\n👋 Goodbye!")
                break
            except Exception as e:
                console.print(Panel(f"❌ Error: {str(e)}", style="red"))
    
    def _display_context(self):
        """Display current context information"""
        context_info = f"""
        📋 Current Context:
        • User: {self.context.name or 'Unknown'}
        • Premium: {'Yes' if self.context.is_premium_user else 'No'}
        • Issue Type: {self.context.issue_type.value if self.context.issue_type else 'None'}
        """
        console.print(Panel(context_info, style="dim"))


def main():
    """Main entry point"""
    system = SupportAgentSystem()
    system.run()


if __name__ == "__main__":
    main()
