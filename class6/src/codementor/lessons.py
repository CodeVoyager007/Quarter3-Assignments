import streamlit as st
from data.lessons import PYTHON_LESSONS, JAVASCRIPT_LESSONS, TYPESCRIPT_LESSONS

class Lesson:
    def __init__(self, title: str, content: str, language: str, difficulty: str):
        self.title = title
        self.content = content
        self.language = language
        self.difficulty = difficulty
        self.completed = False

    def mark_completed(self):
        self.completed = True

def get_lessons(language: str, difficulty: str):
    lessons_data = {
        'python': PYTHON_LESSONS,
        'javascript': JAVASCRIPT_LESSONS,
        'typescript': TYPESCRIPT_LESSONS
    }
    return [
        Lesson(**lesson_data)
        for lesson_data in lessons_data.get(language.lower(), {}).get(difficulty.lower(), [])
    ]

def lessons_page():
    st.header("Lessons")
    language = st.selectbox("Select Language", ["Python", "JavaScript", "TypeScript"], key="lessons_language")
    difficulty = st.selectbox("Select Difficulty", ["Beginner", "Intermediate", "Advanced"], key="lessons_difficulty")
    st.subheader(f"{language} Lessons - {difficulty}")
    lessons = get_lessons(language.lower(), difficulty.lower())
    for lesson in lessons:
        with st.expander(lesson.title):
            st.markdown(lesson.content)
            if st.button(f"Mark {lesson.title} as Completed", key=f"lesson_{lesson.title}"):
                lesson.mark_completed()
                st.success("Lesson marked as completed!") 