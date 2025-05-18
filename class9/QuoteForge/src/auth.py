import streamlit as st
from typing import Optional, Dict, Any
import jwt
from datetime import datetime, timedelta
from dataclasses import dataclass

# User data model for storing user information and subscription status
@dataclass
class User:
    email: str
    name: str
    subscription: str
    password: str

# In-memory database simulation for user management
class UserDatabase:
    def __init__(self):
        self._users = {
            "demo@quoteforge.com": User(
                email="demo@quoteforge.com",
                password="demouser2314",
                name="Demo User",
                subscription="free"
            ),
            "pro@quoteforge.com": User(
                email="pro@quoteforge.com",
                password="prouser2134",
                name="Pro User",
                subscription="pro"
            )
        }
    
    def get_user(self, email: str) -> Optional[User]:
        return self._users.get(email)
    
    def verify_password(self, email: str, password: str) -> bool:
        user = self.get_user(email)
        return user and user.password == password

# Handles JWT token creation and validation for user sessions
class TokenManager:
    def __init__(self, secret: str):
        self._secret = secret
    
    def create_token(self, user: User) ->str:
        expiration = datetime.utcnow() + timedelta(hours=24)
        payload = {
            "email": user.email,
            "exp": expiration,
            "subscription": user.subscription
        }
        return jwt.encode(payload, self._secret, algorithm="HS256")
    
    def verify_token(self, token: str)-> Optional[Dict[str, Any]]:
        try:
            payload = jwt.decode(token, self._secret, algorithms=["HS256"])
            if datetime.fromtimestamp(payload["exp"]) > datetime.utcnow():
                return payload
        except:
            pass
        return None

# Main authentication class that coordinates user authentication and session management
class Auth:
    def __init__(self):
        self._db = UserDatabase()
        self._token_manager = TokenManager("your-jwt-secret")
    
    # Authenticates user credentials and returns session token if valid
    def login(self, email: str, password: str) -> Optional[Dict[str, Any]]:
        if self._db.verify_password(email, password):
            user = self._db.get_user(email)
            token = self._token_manager.create_token(user)
            return {
                "token": token,
                "user": {
                    "email": user.email,
                    "name": user.name,
                    "subscription": user.subscription
                }
            }
        return None
    def verify_token(self, token: str) -> Optional[Dict[str, Any]]:
        return self._token_manager.verify_token(token)
    
    def is_authenticated(self) -> bool:
        if "auth_token" not in st.session_state:
            return False
        
        result = self.verify_token(st.session_state["auth_token"])
        return result is not None
    
 # Returns user's subscription status, defaulting to "free" if not authenticated
    def get_user_subscription(self) -> str:
        if not self.is_authenticated():
            return "free"            
        payload = self.verify_token(st.session_state["auth_token"])
        return payload.get("subscription", "free") if payload else "free"    
    
    def logout(self):
        if "auth_token" in st.session_state:
            del st.session_state["auth_token"] 