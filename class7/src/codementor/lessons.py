import streamlit as st
from data.lessons import PYTHON_LESSONS, JAVASCRIPT_LESSONS, TYPESCRIPT_LESSONS, NEXTJS_LESSONS
from data.progress import UserProgress

class Lesson:
    def __init__(self, title: str, content: str, language: str, difficulty: str):
        self.title = title
        self.content = content
        self.language = language
        self.difficulty = difficulty
        self.completed = False

    def mark_completed(self):
        self.completed = True
        if 'user_progress' in st.session_state:
            st.session_state.user_progress.add_completed_lesson(self.language, self.title)

def get_lessons(language: str, difficulty: str):
    # Map UI language names to data keys
    language_map = {
        'python': 'python',
        'javascript': 'javascript',
        'typescript': 'typescript',
        'next.js': 'nextjs'  # Map UI name to data key
    }
    
    lessons_data = {
        'python': PYTHON_LESSONS,
        'javascript': JAVASCRIPT_LESSONS,
        'typescript': TYPESCRIPT_LESSONS,
        'nextjs': NEXTJS_LESSONS
    }
    
    # Convert language name to lowercase and map to data key
    language_key = language_map.get(language.lower())
    if not language_key:
        return []
        
    # Get user progress
    user_progress = st.session_state.user_progress if 'user_progress' in st.session_state else None
    
    lessons = []
    for lesson_data in lessons_data.get(language_key, {}).get(difficulty.lower(), []):
        lesson = Lesson(**lesson_data)
        if user_progress and lesson.title in user_progress.completed_lessons.get(language_key, set()):
            lesson.completed = True
        lessons.append(lesson)
        
    return lessons

def lessons_page():
    st.header("Lessons")
    language = st.selectbox("Select Language", ["Python", "JavaScript", "TypeScript", "Next.js"], key="lessons_language")
    difficulty = st.selectbox("Select Difficulty", ["Beginner", "Intermediate", "Advanced"], key="lessons_difficulty")
    st.subheader(f"{language} Lessons - {difficulty}")
    
    lessons = get_lessons(language, difficulty)
    for lesson in lessons:
        with st.expander(f"{'✅ ' if lesson.completed else ''}{lesson.title}"):
            st.markdown(lesson.content)
            if not lesson.completed and st.button(f"Mark {lesson.title} as Completed", key=f"lesson_{lesson.title}"):
                lesson.mark_completed()
                st.success("Lesson marked as completed! 🎉")
                st.experimental_rerun() 