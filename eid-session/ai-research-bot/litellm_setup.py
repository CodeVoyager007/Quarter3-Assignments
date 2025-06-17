"""
LiteLLM configuration and setup module.
Provides a wrapper around LiteLLM for OpenAI-compatible API calls.
"""

import os
from typing import Dict, Any, List, Optional
from litellm import completion
from dotenv import load_dotenv
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

class LiteLLMConfig:
    """Configuration class for LiteLLM."""
    
    def __init__(self):
        # Ensure API key is properly formatted
        api_key = os.getenv("OPENROUTER_API_KEY", "").strip()
        if not api_key:
            raise ValueError("OPENROUTER_API_KEY not found in environment variables")
        
        
        self.api_key = api_key.strip('"\'')
        logger.info(f"API Key found: {'Yes' if self.api_key else 'No'}")
        logger.info(f"API Key length: {len(self.api_key)}")
            
        self.model_name = os.getenv("LITELLM_MODEL_NAME", "openai/gpt-3.5-turbo")
        self.api_base = os.getenv("LITELLM_API_BASE", "https://openrouter.ai/api/v1")
        self.max_tokens = int(os.getenv("MAX_TOKENS", "1000"))
        self.temperature = float(os.getenv("TEMPERATURE", "0.7"))
        logger.info(f"Configuration loaded - Model: {self.model_name}, API Base: {self.api_base}")

class LiteLLMClient:
    """Client for interacting with LiteLLM."""
    
    def __init__(self):
        self.config = LiteLLMConfig()
    
    def generate_completion(
        self,
        messages: List[Dict[str, str]],
        model: Optional[str] = None,
        max_tokens: Optional[int] = None,
        temperature: Optional[float] = None,
        **kwargs: Any
    ) -> Dict[str, Any]:
        """
        Generate a completion using LiteLLM.
        
        Args:
            messages: List of message dictionaries with 'role' and 'content'
            model: Model to use (defaults to config model)
            max_tokens: Maximum tokens to generate
            temperature: Sampling temperature
            **kwargs: Additional parameters to pass to LiteLLM
            
        Returns:
            Dict containing the completion response
        """
        try:
           
            kwargs["api_key"] = self.config.api_key
            kwargs["api_base"] = self.config.api_base
            
            kwargs["headers"] = {
                "HTTP-Referer": "https://github.com/CodeVoyager007/AI-Research-Bot",
                "X-Title": "AI Research Bot",
                "Authorization": f"Bearer {self.config.api_key}"  
            }
            
            logger.info(f"Making API call to {self.config.api_base} with model {model or self.config.model_name}")
            
            # Set the model provider explicitly
            kwargs["provider"] = "openrouter"
            
            response = completion(
                model=model or self.config.model_name,
                messages=messages,
                max_tokens=max_tokens or self.config.max_tokens,
                temperature=temperature or self.config.temperature,
                **kwargs
            )
            return response
        except Exception as e:
            logger.error(f"Error in generate_completion: {str(e)}")
            raise Exception(f"Error calling LiteLLM: {str(e)}")

# Create a singleton instance
litellm_client = LiteLLMClient()

def get_chat_completion(
    prompt: str,
    system_prompt: Optional[str] = None,
    **kwargs: Any
) -> str:
    """
    Helper function to get a chat completion using LiteLLM.
    
    Args:
        prompt: The user's input prompt
        system_prompt: Optional system prompt to set context
        **kwargs: Additional parameters to pass to generate_completion
        
    Returns:
        The generated text response
    """
    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": prompt})
    
    response = litellm_client.generate_completion(messages, **kwargs)
    return response.choices[0].message.content 