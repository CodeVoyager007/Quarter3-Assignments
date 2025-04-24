import streamlit as st
import pandas as pd
import numpy as np
from typing import List, Dict, Optional
from data.lessons import PYTHON_LESSONS, JAVASCRIPT_LESSONS, JAVA_LESSONS
from data.challenges import PYTHON_CHALLENGES, JAVASCRIPT_CHALLENGES, JAVA_CHALLENGES
from data.quizzes import PYTHON_QUIZZES, JAVASCRIPT_QUIZZES, JAVA_QUIZZES

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
    def __init__(self, title: str, description: str, language: str, difficulty: str, solution: str):
        self.title = title
        self.description = description
        self.language = language
        self.difficulty = difficulty
        self.solution = solution
        self.completed = False

    def check_solution(self, user_solution: str) -> bool:
        return user_solution.strip() == self.solution.strip()

class Quiz:
    def __init__(self, questions: List[Dict], language: str, difficulty: str):
        self.questions = questions
        self.language = language
        self.difficulty = difficulty
        self.score = 0

    def check_answer(self, question_index: int, user_answer: str) -> bool:
        return user_answer.lower() == self.questions[question_index]['correct_answer'].lower()

class UserProgress:
    def __init__(self):
        self.completed_lessons = set()
        self.completed_challenges = set()
        self.quiz_scores = {}

    def add_completed_lesson(self, lesson_id: str):
        self.completed_lessons.add(lesson_id)

    def add_completed_challenge(self, challenge_id: str):
        self.completed_challenges.add(challenge_id)

    def add_quiz_score(self, quiz_id: str, score: int):
        self.quiz_scores[quiz_id] = score

def get_lessons(language: str, difficulty: str) -> List[Lesson]:
    lessons_data = {
        'python': PYTHON_LESSONS,
        'javascript': JAVASCRIPT_LESSONS,
        'java': JAVA_LESSONS
    }
    return [
        Lesson(**lesson_data)
        for lesson_data in lessons_data.get(language.lower(), {}).get(difficulty.lower(), [])
    ]

def get_challenges(language: str, difficulty: str) -> List[Challenge]:
    challenges_data = {
        'python': PYTHON_CHALLENGES,
        'javascript': JAVASCRIPT_CHALLENGES,
        'java': JAVA_CHALLENGES
    }
    return [
        Challenge(**challenge_data)
        for challenge_data in challenges_data.get(language.lower(), {}).get(difficulty.lower(), [])
    ]

def get_quiz(language: str, difficulty: str) -> Optional[Quiz]:
    quizzes_data = {
        'python': PYTHON_QUIZZES,
        'javascript': JAVASCRIPT_QUIZZES,
        'java': JAVA_QUIZZES
    }
    questions = quizzes_data.get(language.lower(), {}).get(difficulty.lower(), [])
    if questions:
        return Quiz(questions, language, difficulty)
    return None

def main():
    st.set_page_config(page_title="CodeMentor", layout="wide")
    
    st.title("CodeMentor - Interactive Programming Learning Platform")
    
    # Sidebar for language and difficulty selection
    st.sidebar.title("Navigation")
    language = st.sidebar.selectbox("Select Language", ["Python", "JavaScript", "Java"])
    difficulty = st.sidebar.selectbox("Select Difficulty", ["Beginner", "Intermediate", "Advanced"])
    
    # Main content area
    tab1, tab2, tab3 = st.tabs(["Lessons", "Challenges", "Quizzes"])
    
    with tab1:
        st.header(f"{language} Lessons - {difficulty}")
        lessons = get_lessons(language.lower(), difficulty.lower())
        for lesson in lessons:
            with st.expander(lesson.title):
                st.markdown(lesson.content)
                if st.button(f"Mark {lesson.title} as Completed"):
                    lesson.mark_completed()
                    st.success("Lesson marked as completed!")
    
    with tab2:
        st.header(f"{language} Challenges - {difficulty}")
        challenges = get_challenges(language.lower(), difficulty.lower())
        for challenge in challenges:
            with st.expander(challenge.title):
                st.write(challenge.description)
                user_solution = st.text_area("Your Solution", key=f"challenge_{challenge.title}")
                if st.button("Check Solution", key=f"check_{challenge.title}"):
                    if challenge.check_solution(user_solution):
                        st.success("Correct! Well done!")
                    else:
                        st.error("Try again!")
    
    with tab3:
        st.header(f"{language} Quiz - {difficulty}")
        quiz = get_quiz(language.lower(), difficulty.lower())
        if quiz:
            for i, question in enumerate(quiz.questions):
                st.write(f"Question {i+1}: {question['question']}")
                user_answer = st.radio("Select your answer:", question['options'], key=f"quiz_{i}")
                if st.button("Check Answer", key=f"check_quiz_{i}"):
                    if quiz.check_answer(i, user_answer):
                        st.success("Correct!")
                    else:
                        st.error("Incorrect. Try again!")

if __name__ == "__main__":
    main() 