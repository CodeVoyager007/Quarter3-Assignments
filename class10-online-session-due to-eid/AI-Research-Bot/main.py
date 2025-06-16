"""
Main Streamlit interface for the AI Research Assistant.
"""

import streamlit as st
from orchestrator.swarm_controller import swarm_controller
from dotenv import load_dotenv
import os
import json
from datetime import datetime
import tempfile
from fpdf import FPDF
from fpdf.enums import XPos, YPos
import markdown
import base64
from typing import Dict, Any
import re

# Load environment variables
load_dotenv()

# Page config
st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="🤖",
    layout="wide"
)

# Initialize session state
if "qa_history" not in st.session_state:
    st.session_state.qa_history = []
if "current_paper" not in st.session_state:
    st.session_state.current_paper = None

def create_pdf(paper_data: Dict[str, Any]) -> bytes:
    """Create a PDF from the research paper data."""
    pdf = FPDF()
    pdf.add_page()
    
    # Set margins (left, top, right) in mm
    pdf.set_margins(20, 20, 20)
    
    # Set up fonts - using core fonts
    pdf.set_font("helvetica", "B", 16)
    
    # Title
    pdf.cell(0, 10, paper_data['title'], new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')
    pdf.ln(10)
    
    # Metadata
    pdf.set_font("helvetica", "I", 10)
    pdf.cell(0, 5, f"Topic: {paper_data['topic']}", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.cell(0, 5, f"Generated on: {datetime.fromisoformat(paper_data['date_generated']).strftime('%Y-%m-%d %H:%M:%S')}", 
             new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(10)
    
    # Content
    pdf.set_font("helvetica", "", 12)
    for section in paper_data['sections']:
        # Section title
        pdf.set_font("helvetica", "B", 14)
        pdf.cell(0, 10, section['title'], new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        pdf.ln(5)
        
        # Section content
        pdf.set_font("helvetica", "", 12)
        # Convert markdown to plain text and clean it
        content = markdown.markdown(section['content'])
        content = re.sub(r'<[^>]+>', '', content)  # Remove HTML tags
        content = re.sub(r'\s+', ' ', content)  # Normalize whitespace
        
        # Split content into words and create lines that fit the page width
        words = content.split()
        line = []
        line_width = 0
        max_width = pdf.w - 40  # Page width minus margins
        
        for word in words:
            word_width = pdf.get_string_width(word + ' ')
            if line_width + word_width <= max_width:
                line.append(word)
                line_width += word_width
            else:
                # Write the current line and start a new one
                pdf.cell(0, 5, ' '.join(line), new_x=XPos.LMARGIN, new_y=YPos.NEXT)
                line = [word]
                line_width = word_width
        
        # Write the last line if any
        if line:
            pdf.cell(0, 5, ' '.join(line), new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        
        pdf.ln(5)
        
        # Subsections
        for subsection in section.get('subsections', []):
            pdf.set_font("helvetica", "B", 12)
            pdf.cell(0, 10, subsection['title'], new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            pdf.ln(2)
            
            pdf.set_font("helvetica", "", 12)
            content = markdown.markdown(subsection['content'])
            content = re.sub(r'<[^>]+>', '', content)
            content = re.sub(r'\s+', ' ', content)
            
            # Split content into words and create lines that fit the page width
            words = content.split()
            line = []
            line_width = 0
            
            for word in words:
                word_width = pdf.get_string_width(word + ' ')
                if line_width + word_width <= max_width:
                    line.append(word)
                    line_width += word_width
                else:
                    pdf.cell(0, 5, ' '.join(line), new_x=XPos.LMARGIN, new_y=YPos.NEXT)
                    line = [word]
                    line_width = word_width
            
            if line:
                pdf.cell(0, 5, ' '.join(line), new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            
            pdf.ln(5)
    
    # Get PDF bytes using the correct method
    try:
        # First try the new method
        pdf_bytes = pdf.output()
        if isinstance(pdf_bytes, bytearray):
            return bytes(pdf_bytes)
        return pdf_bytes
    except Exception as e:
        # Fallback to the old method if needed
        try:
            return pdf.output(dest='S').encode('latin1')
        except Exception as e2:
            raise Exception(f"Failed to generate PDF: {str(e)} / {str(e2)}")

def get_download_link(pdf_bytes: bytes, filename: str) -> str:
    """Generate a download link for the PDF."""
    try:
        b64 = base64.b64encode(pdf_bytes).decode('utf-8')
        return f'<a href="data:application/pdf;base64,{b64}" download="{filename}">Download PDF</a>'
    except Exception as e:
        raise Exception(f"Failed to create download link: {str(e)}")

def show_research_paper_ui():
    """Show the research paper generation interface."""
    st.header("📚 Research Paper Generator")
    
    # Input
    topic = st.text_input("Enter your research topic")
    
    # Options
    col1, col2 = st.columns(2)
    with col1:
        num_pages = st.number_input(
            "Number of Pages",
            min_value=3,
            max_value=20,
            value=5,
            step=1
        )
    with col2:
        # Define available sections - using a tuple for immutability
        available_sections = (
            "Abstract",
            "Introduction",
            "Literature Review",
            "Methodology",
            "Results",  # Individual sections instead of combined
            "Discussion",
            "Conclusion",
            "References",
            "Appendices"
        )
        
        # Define default sections - must be a subset of available_sections
        default_sections = (
            "Abstract",
            "Introduction",
            "Literature Review",
            "Methodology",
            "Results",  # Using individual sections
            "Discussion",
            "Conclusion",
            "References"
        )
        
        custom_sections = st.multiselect(
            "Custom Sections (Optional)",
            options=available_sections,
            default=default_sections,
            key="paper_sections"  # Adding a unique key
        )
    
    if st.button("Generate Research Paper", key="generate_paper"):
        if topic:
            with st.spinner("Generating research paper... This may take a few minutes."):
                # Convert sections to list for processing
                sections_to_use = list(custom_sections) if custom_sections else list(default_sections)
                
                result = swarm_controller.process_task(
                    "research_paper",
                    topic,
                    num_pages=num_pages,
                    custom_sections=sections_to_use
                )
                
                if result["status"] == "success":
                    st.session_state.current_paper = result["result"]
                    st.success("Research paper generated successfully!")
                    
                    # Display the paper
                    st.subheader(result["result"]["title"])
                    st.write(f"Topic: {result['result']['topic']}")
                    st.write(f"Generated on: {datetime.fromisoformat(result['result']['date_generated']).strftime('%Y-%m-%d %H:%M:%S')}")
                    
                    # Show each section in an expander
                    for section in result["result"]["sections"]:
                        with st.expander(section["title"]):
                            st.markdown(section["content"])
                            
                            # Show subsections if any
                            for subsection in section.get("subsections", []):
                                st.markdown(f"### {subsection['title']}")
                                st.markdown(subsection["content"])
                    
                    try:
                        # Generate and offer PDF download
                        pdf_bytes = create_pdf(result["result"])
                        st.markdown(
                            get_download_link(
                                pdf_bytes,
                                f"research_paper_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
                            ),
                            unsafe_allow_html=True
                        )
                    except Exception as e:
                        st.error(f"Error generating PDF: {str(e)}")
                        st.info("You can still view the paper content above.")
                else:
                    st.error(f"Error: {result['error']}")
        else:
            st.warning("Please enter a research topic.")

def main():
    """Main Streamlit interface."""
    
    st.title("🤖 AI Research Assistant")
    st.markdown("""
    Welcome to the AI Research Assistant! This tool can help you with:
    - 📝 Text summarization
    - 🌐 English-Urdu translation
    - ❓ Question answering
    - 📚 Research paper generation
    """)
    
    # Task selection
    task_type = st.sidebar.selectbox(
        "Select Task",
        list(swarm_controller.get_available_tasks().keys()),
        format_func=lambda x: x.replace("_", " ").title()
    )
    
    # Task-specific UI
    if task_type == "summarize":
        show_summarizer_ui()
    elif task_type == "translate":
        show_translator_ui()
    elif task_type == "qa":
        show_qa_ui()
    elif task_type == "research_paper":
        show_research_paper_ui()

def show_summarizer_ui():
    """Show the summarizer interface."""
    st.header("📝 Text Summarizer")
    
    # Input
    text = st.text_area("Enter text to summarize", height=200)
    
    # Options
    col1, col2 = st.columns(2)
    with col1:
        style = st.selectbox(
            "Summary Style",
            ["concise", "detailed", "bullet_points"],
            format_func=lambda x: x.replace("_", " ").title()
        )
    with col2:
        max_length = st.number_input(
            "Maximum Length (words)",
            min_value=50,
            max_value=1000,
            value=200,
            step=50
        )
    
    if st.button("Generate Summary"):
        if text:
            with st.spinner("Generating summary..."):
                result = swarm_controller.process_task(
                    "summarize",
                    text,
                    style=style,
                    max_length=max_length
                )
                
                if result["status"] == "success":
                    st.success("Summary generated!")
                    st.write(result["result"])
                else:
                    st.error(f"Error: {result['error']}")
        else:
            st.warning("Please enter some text to summarize.")

def show_translator_ui():
    """Show the translator interface."""
    st.header("🌐 English-Urdu Translator")
    
    # Input
    text = st.text_area("Enter text to translate", height=200)
    
    # Translation options
    target_lang = st.radio(
        "Translate to",
        ["en", "ur"],
        format_func=lambda x: "English" if x == "en" else "Urdu",
        horizontal=True
    )
    
    preserve_formality = st.checkbox("Preserve formality level", value=True)
    
    if st.button("Translate"):
        if text:
            with st.spinner("Translating..."):
                result = swarm_controller.process_task(
                    "translate",
                    text,
                    target_language=target_lang,
                    preserve_formality=preserve_formality
                )
                
                if result["status"] == "success":
                    st.success("Translation complete!")
                    st.write(result["result"])
                else:
                    st.error(f"Error: {result['error']}")
        else:
            st.warning("Please enter some text to translate.")

def show_qa_ui():
    """Show the question answering interface."""
    st.header("❓ Question Answering")
    
    # Context input
    context = st.text_area(
        "Optional: Provide context for the question",
        height=150,
        help="You can provide additional context to help answer the question"
    )
    
    # Question input
    question = st.text_input("Enter your question")
    
    # Options
    use_history = st.checkbox("Use conversation history", value=True)
    if use_history:
        max_history = st.slider("Maximum history length", 1, 10, 5)
    
    if st.button("Get Answer"):
        if question:
            with st.spinner("Thinking..."):
                result = swarm_controller.process_task(
                    "qa",
                    question,
                    context=context if context else None,
                    use_history=use_history,
                    max_history=max_history if use_history else None
                )
                
                if result["status"] == "success":
                    st.success("Answer generated!")
                    st.write(result["result"])
                    
                    # Update history
                    if use_history:
                        st.session_state.qa_history.append({
                            "question": question,
                            "answer": result["result"]
                        })
                else:
                    st.error(f"Error: {result['error']}")
        else:
            st.warning("Please enter a question.")
    
    # Show conversation history
    if st.session_state.qa_history:
        st.subheader("Conversation History")
        for i, exchange in enumerate(st.session_state.qa_history):
            with st.expander(f"Q&A {i+1}"):
                st.write("Q:", exchange["question"])
                st.write("A:", exchange["answer"])
        
        if st.button("Clear History"):
            st.session_state.qa_history = []
            st.rerun()

if __name__ == "__main__":
    main()
