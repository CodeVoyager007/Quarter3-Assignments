from pydantic import BaseModel
from typing import Optional, Dict, Any
from enum import Enum


class IssueType(str, Enum):
    BILLING = "billing"
    TECHNICAL = "technical"
    GENERAL = "general"


class UserContext(BaseModel):
    """Context model to store user information and state"""
    name: Optional[str] = None
    is_premium_user: bool = False
    issue_type: Optional[IssueType] = None
    user_id: Optional[str] = None
    session_data: Dict[str, Any] = {}


class AgentConfig(BaseModel):
    """Configuration for the agent system"""
    gemini_api_key: str
    model_name: str = "gemini-1.5-flash"
    max_tokens: int = 1000
    temperature: float = 0.7 