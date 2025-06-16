"""
Summarizer Agent module.
Handles text summarization using LiteLLM.
"""

from typing import Optional
from litellm_setup import get_chat_completion

class SummarizerAgent:
    """Agent responsible for summarizing text content."""
    
    def __init__(self):
        self.system_prompt = """You are a professional summarizer. Your task is to create concise, 
        informative summaries of the provided text. Focus on key points and main ideas while 
        maintaining clarity and coherence. Keep the summary objective and factual."""
    
    def summarize(
        self,
        text: str,
        max_length: Optional[int] = None,
        style: str = "concise"
    ) -> str:
        """
        Generate a summary of the provided text.
        
        Args:
            text: The text to summarize
            max_length: Optional maximum length for the summary
            style: Style of summary (concise, detailed, bullet_points)
            
        Returns:
            The generated summary
        """
        # Construct the prompt based on style
        style_instructions = {
            "concise": "Provide a brief, concise summary focusing on the main points.",
            "detailed": "Provide a detailed summary that captures all important aspects.",
            "bullet_points": "Provide a summary in bullet points, highlighting key information."
        }
        
        prompt = f"""Please summarize the following text in a {style} style:
        {style_instructions.get(style, style_instructions['concise'])}
        
        Text to summarize:
        {text}
        
        {f'Keep the summary under {max_length} words.' if max_length else ''}"""
        
        try:
            summary = get_chat_completion(
                prompt=prompt,
                system_prompt=self.system_prompt,
                temperature=0.3  # Lower temperature for more focused summaries
            )
            return summary
        except Exception as e:
            raise Exception(f"Error generating summary: {str(e)}")

# Create a singleton instance
summarizer_agent = SummarizerAgent() 