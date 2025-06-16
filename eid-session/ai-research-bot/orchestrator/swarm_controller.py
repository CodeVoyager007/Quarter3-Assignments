"""
Swarm Controller module.
Manages and routes tasks to appropriate agents.
"""

from typing import Dict, Any, Optional, Literal, List
from agents.summarizer_agent import summarizer_agent
from agents.translator_agent import translator_agent
from agents.qa_agent import qa_agent
from agents.research_paper_agent import research_paper_agent

class SwarmController:
    """Controller class that manages and routes tasks to appropriate agents."""
    
    def __init__(self):
        self.agents = {
            "summarize": summarizer_agent,
            "translate": translator_agent,
            "qa": qa_agent,
            "research_paper": research_paper_agent
        }
    
    def process_task(
        self,
        task_type: Literal["summarize", "translate", "qa", "research_paper"],
        input_text: str,
        **kwargs: Any
    ) -> Dict[str, Any]:
        """
        Process a task by routing it to the appropriate agent.
        
        Args:
            task_type: Type of task to process
            input_text: Input text for the task
            **kwargs: Additional parameters specific to each task type
            
        Returns:
            Dict containing the task result and metadata
        """
        if task_type not in self.agents:
            raise ValueError(f"Unknown task type: {task_type}")
        
        agent = self.agents[task_type]
        
        try:
            # Route the task to the appropriate agent
            if task_type == "summarize":
                result = agent.summarize(
                    text=input_text,
                    max_length=kwargs.get("max_length"),
                    style=kwargs.get("style", "concise")
                )
            elif task_type == "translate":
                # Auto-detect language if not specified
                target_lang = kwargs.get("target_language")
                if not target_lang:
                    detected_lang = agent.detect_language(input_text)
                    target_lang = "ur" if detected_lang == "en" else "en"
                
                result = agent.translate(
                    text=input_text,
                    target_language=target_lang,
                    preserve_formality=kwargs.get("preserve_formality", True)
                )
            elif task_type == "qa":
                result = agent.answer_question(
                    question=input_text,
                    context=kwargs.get("context"),
                    use_history=kwargs.get("use_history", True),
                    max_history=kwargs.get("max_history", 5)
                )
            elif task_type == "research_paper":
                result = agent.generate_paper(
                    topic=input_text,
                    num_pages=kwargs.get("num_pages", 5),
                    custom_sections=kwargs.get("custom_sections")
                )
            
            return {
                "status": "success",
                "task_type": task_type,
                "result": result,
                "metadata": {
                    "input_length": len(input_text),
                    "output_length": len(str(result)) if isinstance(result, (str, dict)) else 0,
                    **kwargs
                }
            }
            
        except Exception as e:
            return {
                "status": "error",
                "task_type": task_type,
                "error": str(e),
                "metadata": kwargs
            }
    
    def get_available_tasks(self) -> Dict[str, str]:
        """Get a dictionary of available tasks and their descriptions."""
        return {
            "summarize": "Summarize text with optional style and length constraints",
            "translate": "Translate between English and Urdu",
            "qa": "Answer questions based on context and conversation history",
            "research_paper": "Generate a structured research paper on a given topic"
        }

# Create a singleton instance
swarm_controller = SwarmController() 