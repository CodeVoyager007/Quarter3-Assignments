"""
Translator Agent module.
Handles translation between English and Urdu using LiteLLM.
"""

from typing import Literal
from litellm_setup import get_chat_completion

class TranslatorAgent:
    """Agent responsible for translation between English and Urdu."""
    
    def __init__(self):
        self.system_prompt = """You are a professional translator specializing in English and Urdu. 
        Your task is to provide accurate translations while maintaining the original meaning, tone, 
        and cultural context. Pay special attention to idiomatic expressions and cultural nuances."""
    
    def translate(
        self,
        text: str,
        target_language: Literal["en", "ur"],
        preserve_formality: bool = True
    ) -> str:
        """
        Translate text between English and Urdu.
        
        Args:
            text: The text to translate
            target_language: Target language code ('en' for English, 'ur' for Urdu)
            preserve_formality: Whether to maintain the formality level of the original text
            
        Returns:
            The translated text
        """
        # Determine source language from target
        source_language = "ur" if target_language == "en" else "en"
        
        # Language names for the prompt
        lang_names = {
            "en": "English",
            "ur": "Urdu"
        }
        
        prompt = f"""Please translate the following text from {lang_names[source_language]} to {lang_names[target_language]}.
        {'Maintain the same level of formality as the original text.' if preserve_formality else ''}
        
        Text to translate:
        {text}
        
        Provide only the translation, without any additional explanations or notes."""
        
        try:
            translation = get_chat_completion(
                prompt=prompt,
                system_prompt=self.system_prompt,
                temperature=0.3  # Lower temperature for more accurate translations
            )
            return translation.strip()
        except Exception as e:
            raise Exception(f"Error during translation: {str(e)}")
    
    def detect_language(self, text: str) -> Literal["en", "ur"]:
        """
        Detect if the text is in English or Urdu.
        
        Args:
            text: The text to analyze
            
        Returns:
            Language code ('en' or 'ur')
        """
        prompt = f"""Analyze the following text and determine if it's in English or Urdu.
        Respond with only 'en' for English or 'ur' for Urdu.
        
        Text to analyze:
        {text}"""
        
        try:
            result = get_chat_completion(
                prompt=prompt,
                system_prompt="You are a language detection expert. Respond only with 'en' or 'ur'.",
                temperature=0.1
            )
            return result.strip().lower()[:2]  # Get first two characters and ensure lowercase
        except Exception as e:
            raise Exception(f"Error detecting language: {str(e)}")

# Create a singleton instance
translator_agent = TranslatorAgent() 