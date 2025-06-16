"""
OpenRouter configuration and setup module.
Handles API authentication and provides helper functions for making requests.
"""

import os
from typing import Dict, Any, Optional
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class OpenRouterConfig:
    """Configuration class for OpenRouter API."""
    
    def __init__(self):
        self.api_key = os.getenv("OPENROUTER_API_KEY")
        self.base_url = os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")
        
        if not self.api_key:
            raise ValueError("OPENROUTER_API_KEY not found in environment variables")
    
    def get_headers(self) -> Dict[str, str]:
        """Get headers required for OpenRouter API requests."""
        return {
            "Authorization": f"Bearer {self.api_key}",
            "HTTP-Referer": "https://github.com/yourusername/AI-Research-Bot",  # Replace with your repo
            "X-Title": "AI Research Bot",
            "Content-Type": "application/json"
        }

class OpenRouterClient:
    """Client for interacting with OpenRouter API."""
    
    def __init__(self):
        self.config = OpenRouterConfig()
    
    def generate_completion(
        self,
        prompt: str,
        model: str = "openai/gpt-3.5-turbo",
        max_tokens: int = 1000,
        temperature: float = 0.7,
        **kwargs: Any
    ) -> Dict[str, Any]:
        """
        Generate a completion using OpenRouter API.
        
        Args:
            prompt: The input prompt
            model: The model to use (default: gpt-3.5-turbo)
            max_tokens: Maximum tokens to generate
            temperature: Sampling temperature
            **kwargs: Additional parameters to pass to the API
            
        Returns:
            Dict containing the API response
        """
        url = f"{self.config.base_url}/chat/completions"
        
        payload = {
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": max_tokens,
            "temperature": temperature,
            **kwargs
        }
        
        try:
            response = requests.post(
                url,
                headers=self.config.get_headers(),
                json=payload,
                timeout=30
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error calling OpenRouter API: {str(e)}")

# Create a singleton instance
openrouter_client = OpenRouterClient()

def get_completion(prompt: str, **kwargs: Any) -> str:
    """
    Helper function to get a completion from OpenRouter.
    
    Args:
        prompt: The input prompt
        **kwargs: Additional parameters to pass to generate_completion
        
    Returns:
        The generated text response
    """
    response = openrouter_client.generate_completion(prompt, **kwargs)
    return response["choices"][0]["message"]["content"] 