"""
Q&A Agent module.
Handles question answering using LiteLLM.
"""

from typing import Optional, List, Dict
from litellm_setup import get_chat_completion

class QAAgent:
    """Agent responsible for answering questions based on provided context."""
    
    def __init__(self):
        self.system_prompt = """You are a knowledgeable and helpful AI assistant. Your task is to 
        answer questions based on the provided context. If the answer cannot be found in the context, 
        say so clearly. Be concise but thorough in your responses."""
        
        # Store conversation history for context
        self.conversation_history: List[Dict[str, str]] = []
    
    def answer_question(
        self,
        question: str,
        context: Optional[str] = None,
        use_history: bool = True,
        max_history: int = 5
    ) -> str:
        """
        Answer a question based on provided context and conversation history.
        
        Args:
            question: The question to answer
            context: Optional context to use for answering
            use_history: Whether to use conversation history
            max_history: Maximum number of previous exchanges to include
            
        Returns:
            The answer to the question
        """
        # Prepare the prompt with context and history
        prompt_parts = []
        
        if context:
            prompt_parts.append(f"Context:\n{context}\n")
        
        if use_history and self.conversation_history:
            # Include recent conversation history
            history_text = "\n".join([
                f"{'User' if msg['role'] == 'user' else 'Assistant'}: {msg['content']}"
                for msg in self.conversation_history[-max_history:]
            ])
            prompt_parts.append(f"Previous conversation:\n{history_text}\n")
        
        prompt_parts.append(f"Question: {question}")
        
        prompt = "\n".join(prompt_parts)
        
        try:
            answer = get_chat_completion(
                prompt=prompt,
                system_prompt=self.system_prompt,
                temperature=0.7
            )
            
            # Update conversation history
            if use_history:
                self.conversation_history.extend([
                    {"role": "user", "content": question},
                    {"role": "assistant", "content": answer}
                ])
                # Trim history if it gets too long
                if len(self.conversation_history) > max_history * 2:
                    self.conversation_history = self.conversation_history[-max_history * 2:]
            
            return answer
        except Exception as e:
            raise Exception(f"Error answering question: {str(e)}")
    
    def clear_history(self) -> None:
        """Clear the conversation history."""
        self.conversation_history = []

# Create a singleton instance
qa_agent = QAAgent() 