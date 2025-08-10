import os
from dotenv import load_dotenv
from agents import (
    Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel,
    RunConfig, function_tool, RunContextWrapper,
    input_guardrail, output_guardrail, GuardrailFunctionOutput
)
from pydantic import BaseModel

# ===================== Environment Setup =====================
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("❌ GEMINI_API_KEY is not set in .env file.")

# ===================== Model Setup =====================
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client,
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True,
)

# ===================== Data Models =====================
class Account(BaseModel):
    """Represents a bank account holder."""
    name: str
    pin: int

class GuardrailOutput(BaseModel):
    """Output from guardrail agent to check if query is bank-related."""
    is_bank_related: bool
    reasoning: str

class OutputSafetyCheck(BaseModel):
    """Output guardrail to ensure safe and policy-compliant responses."""
    is_safe: bool
    reasoning: str

# ===================== Input Guardrail Agent =====================
guardrail_agent = Agent(
    name="Guardrail Agent",
    instructions="You are a guardrail agent. Determine if the user's query is bank-related. "
                 "Set is_bank_related = True if yes, otherwise False.",
    output_type=GuardrailOutput,
    model=model
)

@input_guardrail
async def check_bank_related(
    ctx: RunContextWrapper,
    agent: Agent,
    user_input: str
) -> GuardrailFunctionOutput:
    """Checks if the user query is related to banking."""
    result = await Runner.run(
        guardrail_agent,
        user_input,
        context=ctx.context
    )

    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=not result.final_output.is_bank_related
    )

# ===================== Output Guardrail Agent =====================
output_guardrail_agent = Agent(
    name="Output Guardrail Agent",
    instructions="You check if the AI's response is safe, policy-compliant, and non-offensive. "
                 "Return is_safe=True if everything is fine.",
    output_type=OutputSafetyCheck,
    model=model
)

@output_guardrail
async def check_output_safety(
    ctx: RunContextWrapper,
    agent: Agent,
    ai_output: str
) -> GuardrailFunctionOutput:
    """Ensures AI output is safe before sending to user."""
    result = await Runner.run(
        output_guardrail_agent,
        ai_output,
        context=ctx.context
    )

    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=not result.final_output.is_safe
    )

# ===================== Tools =====================
def check_user(ctx: RunContextWrapper[Account], agent: Agent) -> bool:
    """Validate account holder before tool access."""
    return ctx.context.name == "Ayesha Mughal" and ctx.context.pin == 2162009

@function_tool(is_enabled=check_user)
def balance_checker(account_number: str) -> str:
    return "The balance for your account is $10,000."

@function_tool(is_enabled=check_user)
def loan_status_checker(loan_id: str) -> str:
    return f"Loan application {loan_id} is approved and awaiting disbursement."

@function_tool(is_enabled=check_user)
def credit_card_checker(card_number: str) -> str:
    return "Your credit card limit is $5,000 and available balance is $3,200."

@function_tool(is_enabled=check_user)
def register_complaint(complaint_text: str) -> str:
    return "Your complaint has been registered successfully. Reference ID: CMP-9821."

# ===================== Agents =====================
bank_teller_agent = Agent(
    name="Bank Teller Agent",
    instructions="Handle general account-related queries: balance, deposits, withdrawals.",
    model=model,
    tools=[balance_checker],
    input_guardrails=[check_bank_related],
    output_guardrails=[check_output_safety],
)

loan_officer_agent = Agent(
    name="Loan Officer Agent",
    instructions="Handle loan-related queries: eligibility, status, repayments.",
    model=model,
    tools=[loan_status_checker],
    input_guardrails=[check_bank_related],
    output_guardrails=[check_output_safety],
)

credit_card_agent = Agent(
    name="Credit Card Agent",
    instructions="Handle credit card queries: balance, transactions, applications.",
    model=model,
    tools=[credit_card_checker],
    input_guardrails=[check_bank_related],
    output_guardrails=[check_output_safety],
)

customer_support_agent = Agent(
    name="Customer Support Agent",
    instructions="Handle customer support: branch timings, lost cards, complaints.",
    model=model,
    tools=[register_complaint],
    input_guardrails=[check_bank_related],
    output_guardrails=[check_output_safety],
)

# ===================== Router Agent (Handoff) =====================
router_agent = Agent(
    name="Router Agent",
    instructions="""
    You are a routing agent for a bank:
    - If query is about loans → Loan Officer Agent
    - If about credit cards → Credit Card Agent
    - If about complaints or general support → Customer Support Agent
    - Else → Bank Teller Agent
    """,
    model=model,
    handoffs=[bank_teller_agent, loan_officer_agent, credit_card_agent, customer_support_agent]
)

# ===================== Execution =====================
if __name__ == "__main__":
    user_context = Account(name="Ayesha Mughal", pin=2162009)

    queries = [
        "Check my account balance",
        "What is the status of my loan ID 12345?",
        "What is my credit card limit?",
        "I want to file a complaint about ATM cash not dispensing"
    ]

    for q in queries:
        print(f"\n=== Query: {q} ===")
        result = Runner.run_sync(
            router_agent,
            q,
            run_config=config,
            context=user_context,
        )
        print(result.final_output)
