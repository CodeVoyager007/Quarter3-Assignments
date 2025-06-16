"""
Research Paper Generator Agent module.
Handles generation of structured research papers with proper formatting.
"""

from typing import Dict, Any, List, Optional
from dataclasses import dataclass
from litellm_setup import get_chat_completion
import json
import re
from datetime import datetime

@dataclass
class PaperSection:
    """Represents a section in the research paper."""
    title: str
    content: str
    subsections: List['PaperSection'] = None
    
    def __init__(self, title: str, content: str, subsections: List['PaperSection'] = None):
        self.title = title
        self.content = content
        self.subsections = subsections or []

class ResearchPaperAgent:
    """Agent responsible for generating structured research papers."""
    
    def __init__(self):
        self.system_prompt = """You are an expert research paper writer. Your task is to create 
        well-structured, academically rigorous research papers. Follow these guidelines:
        1. Use clear, academic language
        2. Include proper citations and references
        3. Structure content logically with appropriate headings
        4. Include relevant examples and evidence
        5. Maintain academic tone and style
        6. Use bullet points and lists where appropriate
        7. Include a proper abstract, introduction, methodology, results, and conclusion
        8. Add relevant tables and figures where needed"""
        
        self.default_sections = [
            "Abstract",
            "Introduction",
            "Literature Review",
            "Methodology",
            "Results and Discussion",
            "Conclusion",
            "References"
        ]
    
    def generate_outline(
        self,
        topic: str,
        num_pages: int,
        custom_sections: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """
        Generate a detailed outline for the research paper.
        
        Args:
            topic: The research topic
            num_pages: Target number of pages
            custom_sections: Optional custom section structure
            
        Returns:
            Dict containing the paper outline
        """
        sections = custom_sections or self.default_sections
        
        prompt = f"""Create a detailed outline for a {num_pages}-page research paper on '{topic}'.
        Include the following sections: {', '.join(sections)}
        
        For each section, provide:
        1. Main points to cover
        2. Key subtopics
        3. Important aspects to address
        4. Suggested length (in paragraphs)
        
        Format the response as a JSON object with this structure:
        {{
            "title": "Paper Title",
            "sections": [
                {{
                    "title": "Section Title",
                    "main_points": ["point1", "point2", ...],
                    "subtopics": ["subtopic1", "subtopic2", ...],
                    "key_aspects": ["aspect1", "aspect2", ...],
                    "suggested_length": "X paragraphs"
                }},
                ...
            ]
        }}"""
        
        try:
            response = get_chat_completion(
                prompt=prompt,
                system_prompt="You are an expert at creating research paper outlines. Respond with valid JSON only.",
                temperature=0.7
            )
            return json.loads(response)
        except Exception as e:
            raise Exception(f"Error generating outline: {str(e)}")
    
    def generate_section(
        self,
        topic: str,
        section: Dict[str, Any],
        previous_sections: List[Dict[str, Any]] = None
    ) -> PaperSection:
        """
        Generate content for a specific section of the paper.
        
        Args:
            topic: The research topic
            section: Section details from the outline
            previous_sections: Content of previously generated sections
            
        Returns:
            PaperSection object with generated content
        """
        context = ""
        if previous_sections:
            context = "Previous sections for context:\n" + "\n".join(
                f"{s['title']}:\n{s['content']}" for s in previous_sections
            )
        
        prompt = f"""Write the '{section['title']}' section for a research paper on '{topic}'.
        
        Section requirements:
        - Main points to cover: {', '.join(section['main_points'])}
        - Subtopics to include: {', '.join(section['subtopics'])}
        - Key aspects to address: {', '.join(section['key_aspects'])}
        - Target length: {section['suggested_length']}
        
        {context}
        
        Format the response with:
        1. Clear headings and subheadings
        2. Bullet points where appropriate
        3. Proper academic citations
        4. Relevant examples or evidence
        5. Smooth transitions between ideas"""
        
        try:
            content = get_chat_completion(
                prompt=prompt,
                system_prompt=self.system_prompt,
                temperature=0.7
            )
            
            # Parse the content into subsections
            subsections = self._parse_subsections(content)
            
            return PaperSection(
                title=section['title'],
                content=content,
                subsections=subsections
            )
        except Exception as e:
            raise Exception(f"Error generating section: {str(e)}")
    
    def _parse_subsections(self, content: str) -> List[PaperSection]:
        """Parse content into subsections based on headings."""
        subsections = []
        current_title = None
        current_content = []
        
        for line in content.split('\n'):
            if line.startswith('#'):
                if current_title:
                    subsections.append(PaperSection(
                        title=current_title,
                        content='\n'.join(current_content)
                    ))
                current_title = line.lstrip('#').strip()
                current_content = []
            else:
                current_content.append(line)
        
        if current_title:
            subsections.append(PaperSection(
                title=current_title,
                content='\n'.join(current_content)
            ))
        
        return subsections
    
    def generate_paper(
        self,
        topic: str,
        num_pages: int,
        custom_sections: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """
        Generate a complete research paper.
        
        Args:
            topic: The research topic
            num_pages: Target number of pages
            custom_sections: Optional custom section structure
            
        Returns:
            Dict containing the complete paper
        """
        # Generate outline
        outline = self.generate_outline(topic, num_pages, custom_sections)
        
        # Generate each section
        sections = []
        for section_outline in outline['sections']:
            section = self.generate_section(topic, section_outline, sections)
            sections.append({
                'title': section.title,
                'content': section.content,
                'subsections': [
                    {'title': sub.title, 'content': sub.content}
                    for sub in section.subsections
                ]
            })
        
        return {
            'title': outline['title'],
            'topic': topic,
            'date_generated': datetime.now().isoformat(),
            'sections': sections
        }

# Create a singleton instance
research_paper_agent = ResearchPaperAgent() 