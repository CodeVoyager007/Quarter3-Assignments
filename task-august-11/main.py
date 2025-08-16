
from openai import OpenAI
from agents import (
    Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel,
    RunConfig, function_tool, RunContextWrapper,
    input_guardrail, GuardrailFunctionOutput, InputGuardrailTripwireTriggered
)
from pydantic import BaseModel
from typing import Optional
from dotenv import load_dotenv
import os
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
class UserContext(BaseModel):
    name: str
    member_id: Optional[str] = None

class GuardrailOutput(BaseModel):
    is_library_related: bool
    reasoning: str

# ===================== Book Database =====================
books = {
    "Harry Potter": 3,
    "Python Basics": 5,
    "AI Revolution": 0
}

# ===================== Input Guardrail Agent =====================
guardrail_agent = Agent(
    name="Library Guardrail Agent",
    instructions="Analyze the query. Set is_library_related=True if it involves books, library services, timings, or availability. Otherwise, set is_library_related=False and provide reasoning.",
    output_type=GuardrailOutput,
    model=model
)

@input_guardrail
async def check_library_related(
    ctx: RunContextWrapper,
    agent: Agent,
    user_input: str
) -> GuardrailFunctionOutput:
    result = await Runner.run(
        guardrail_agent,
        user_input,
        context=ctx.context
    )
    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=not result.final_output.is_library_related
    )

# ===================== Tools =====================
def is_member(ctx: RunContextWrapper, agent: Agent) -> bool:
    user_context = ctx.context.get("user")
    return user_context and user_context.member_id is not None

@function_tool(is_enabled=is_member)
def check_availability(title: str) -> str:
    global current_ctx
    user_context = current_ctx.context.get("user") if current_ctx else None
    member_id = user_context.member_id if user_context else None

    if not member_id:
        return "❌ Only registered members can check availability."
    if title not in books:
        return f"❌ Book '{title}' not found."
    copies = books[title]
    return f"📚 Book '{title}' has {copies} copies available." if copies > 0 else f"⚠️ Book '{title}' is out of stock."

@function_tool
def library_timings() -> str:
    return "🕒 The library is open from 9 AM to 5 PM, Monday to Saturday."

@function_tool
def search_book(title: str) -> str:
    if title in books:
        return f"✅ Book '{title}' exists in library."
    return f"❌ Book '{title}' not found."

# ===================== Dynamic Instruction =====================
def personalized_instruction(ctx: RunContextWrapper, agent: Agent) -> str:
    user: UserContext = ctx.context["user"]
    return f"You are a helpful Library Assistant. Always greet {user.name} by name and provide concise, accurate responses about library services."

# ===================== Library Agent =====================
agent = Agent(
    name="library-agent",
    instructions=personalized_instruction,
    tools=[search_book, check_availability, library_timings],
    input_guardrails=[check_library_related],
    model=model,
)

# ===================== Runner Test =====================
if __name__ == "__main__":
    user = UserContext(name="Ayesha", member_id="12345")
    ctx = RunContextWrapper({"user": user})
    global current_ctx
    current_ctx = ctx  # Set the global context for tool access

    queries = [
        "Search for Harry Potter and The Chamber of Secrets book",
        "Check availability of AI Revolution",
        "What are the library timings?",
        "Who is Imran Khan?"  # should be ignored using guardrail
    ]

    for q in queries:
        print("\n🔹 Query:", q)
        try:
            result = Runner.run_sync(agent, q, context=ctx.context)
            print("➡️ Response:", result.final_output)
        except InputGuardrailTripwireTriggered:
            print("➡️ Response: Query ignored (non-library related).")