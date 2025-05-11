import streamlit as st
from typing import List, Dict, Optional
from data.lessons import PYTHON_LESSONS, JAVASCRIPT_LESSONS, TYPESCRIPT_LESSONS, NEXTJS_LESSONS
from data.challenges import PYTHON_CHALLENGES, JAVASCRIPT_CHALLENGES, TYPESCRIPT_CHALLENGES
from data.progress import UserProgress
from quizzes import quizzes_page
from playground import playground_page
from interview_prep import interview_prep_page
from harvard_courses import harvard_courses_page
from free_courses import free_courses_page
from blogs import blogs_page
from lessons import lessons_page
from challenges import challenges_page
from progress_dashboard import progress_dashboard

class Lesson:
    def __init__(self, title: str, content: str, language: str, difficulty: str):
        self.title = title
        self.content = content
        self.language = language
        self.difficulty = difficulty
        self.completed = False

    def mark_completed(self):
        self.completed = True

class Challenge:
    def __init__(self, title: str, description: str, language: str, difficulty: str, solution: str, hint: str = None):
        self.title = title
        self.description = description
        self.language = language
        self.difficulty = difficulty
        self.solution = solution
        self.hint = hint
        self.completed = False

    def check_solution(self, user_solution: str) -> bool:
        return user_solution.strip() == self.solution.strip()

class UserProgress:
    def __init__(self):
        self.completed_lessons = {
            'python': set(),
            'javascript': set(),
            'typescript': set(),
            'nextjs': set()
        }
        self.completed_challenges = {
            'python': set(),
            'javascript': set(),
            'typescript': set(),
            'nextjs': set()
        }
        self.quiz_scores = {}

    def add_completed_lesson(self, language: str, lesson_id: str):
        self.completed_lessons[language].add(lesson_id)

    def add_completed_challenge(self, language: str, challenge_id: str):
        self.completed_challenges[language].add(challenge_id)

    def add_quiz_score(self, language: str, quiz_id: str, score: int):
        if language not in self.quiz_scores:
            self.quiz_scores[language] = {}
        self.quiz_scores[language][quiz_id] = score

    @classmethod
    def load_progress(cls, user_id: str):
        progress = cls()
        # Implementation of loading progress from database
        return progress

def get_lessons(language: str, difficulty: str) -> List[Lesson]:
    lessons_data = {
        'python': PYTHON_LESSONS,
        'javascript': JAVASCRIPT_LESSONS,
        'typescript': TYPESCRIPT_LESSONS,
        'nextjs': NEXTJS_LESSONS
    }
    return [
        Lesson(**lesson_data)
        for lesson_data in lessons_data.get(language.lower(), {}).get(difficulty.lower(), [])
    ]

def get_challenges(language: str, difficulty: str) -> List[Challenge]:
    challenges_data = {
        'python': PYTHON_CHALLENGES,
        'javascript': JAVASCRIPT_CHALLENGES,
        'typescript': TYPESCRIPT_CHALLENGES
    }
    return [
        Challenge(**challenge_data)
        for challenge_data in challenges_data.get(language.lower(), {}).get(difficulty.lower(), [])
    ]

def initialize_session_state():
    if 'user_id' not in st.session_state:
        st.session_state.user_id = "default_user"
    if 'user_progress' not in st.session_state:
        st.session_state.user_progress = UserProgress.load_progress(st.session_state.user_id)

def main():
    st.set_page_config(page_title="CodeMentor", layout="wide")
    st.title("CodeMentor - Interactive Programming Learning Platform")
    
    # Initialize session state
    initialize_session_state()
    
    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs([
        "Lessons", "Challenges", "Quizzes", "Daily Blogs", "Code Playground", 
        "Interview Prep", "Free Courses", "Progress Dashboard"
    ])
    
    with tab1:
        lessons_page()
    
    with tab2:
        challenges_page()
    
    with tab3:
        quizzes_page()

    with tab4:
        blogs_page()

    with tab5:
        playground_page()

    with tab6:
        interview_prep_page()

    with tab7:
        free_courses_page()
        
    with tab8:
        progress_dashboard()

if __name__ == "__main__":
    main() 
    st.markdown(
        """
        <hr>
        <div style='text-align: center; font-size: 16px; margin-top: 30px;'>
            Coded with 💗 by <b>Ayesha Mughal</b><br>
            <a href="mailto:ayeshamughal216@gmail.com">ayeshamughal216@gmail.com</a>
        </div>
        """,
        unsafe_allow_html=True
    ) 