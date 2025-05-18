import streamlit as st
from typing import Optional, Dict, Any
import jwt
from datetime import datetime, timedelta

# Simulated Auth0 user database (in production, use Auth0's actual service)
DUMMY_USERS = {
    "demo@quoteforge.com": {
        "password": "demo123",
        "name": "Demo User",
        "subscription": "free"
    },
    "pro@quoteforge.com": {
        "password": "pro123",
        "name": "Pro User",
        "subscription": "pro"
    }
}

class Auth:
    def __init__(self):
        self._secret = "your-jwt-secret"  # In production, use a proper secret
        
    def _create_token(self, email: str) -> str:
        """Create a JWT token for the user."""
        expiration = datetime.utcnow() + timedelta(hours=24)
        payload = {
            "email": email,
            "exp": expiration,
            "subscription": DUMMY_USERS[email]["subscription"]
        }
        return jwt.encode(payload, self._secret, algorithm="HS256")
    
    def login(self, email: str, password: str) -> Optional[Dict[str, Any]]:
        """Simulate Auth0 login."""
        if email in DUMMY_USERS and DUMMY_USERS[email]["password"] == password:
            token = self._create_token(email)
            return {
                "token": token,
                "user": {
                    "email": email,
                    "name": DUMMY_USERS[email]["name"],
                    "subscription": DUMMY_USERS[email]["subscription"]
                }
            }
        return None
    
    def verify_token(self, token: str) -> Optional[Dict[str, Any]]:
        """Verify JWT token."""
        try:
            payload = jwt.decode(token, self._secret, algorithms=["HS256"])
            if datetime.fromtimestamp(payload["exp"]) > datetime.utcnow():
                return payload
        except:
            pass
        return None
    
    def is_authenticated(self) -> bool:
        """Check if user is authenticated."""
        if "auth_token" not in st.session_state:
            return False
        
        result = self.verify_token(st.session_state["auth_token"])
        return result is not None
    
    def get_user_subscription(self) -> str:
        """Get user's subscription level."""
        if not self.is_authenticated():
            return "free"
            
        payload = self.verify_token(st.session_state["auth_token"])
        return payload.get("subscription", "free") if payload else "free"
    
    def logout(self):
        """Log out the user."""
        if "auth_token" in st.session_state:
            del st.session_state["auth_token"] 