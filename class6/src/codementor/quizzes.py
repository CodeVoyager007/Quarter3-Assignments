import streamlit as st
from typing import List, Dict, Optional
from data.quizzes import PYTHON_QUIZZES, JAVASCRIPT_QUIZZES, TYPESCRIPT_QUIZZES

class Quiz:
    def __init__(self, questions: List[Dict], language: str, difficulty: str):
        self.questions = questions
        self.language = language
        self.difficulty = difficulty
        self.score = 0

    def check_answer(self, question_index: int, user_answer: str) -> bool:
        return user_answer.lower() == self.questions[question_index]['correct_answer'].lower()

def get_quiz(language: str, difficulty: str) -> Optional[Quiz]:
    quizzes_data = {
        'python': PYTHON_QUIZZES,
        'javascript': JAVASCRIPT_QUIZZES,
        'typescript': TYPESCRIPT_QUIZZES
    }
    questions = quizzes_data.get(language.lower(), {}).get(difficulty.lower(), [])
    if questions:
        return Quiz(questions, language, difficulty)
    return None

def quizzes_page():
    st.header("Quizzes")
    language = st.selectbox("Select Language", ["Python", "JavaScript", "TypeScript"], key="quizzes_language")
    difficulty = st.selectbox("Select Difficulty", ["Beginner", "Intermediate", "Advanced"], key="quizzes_difficulty")
    st.subheader(f"{language} Quiz - {difficulty}")
    quiz = get_quiz(language.lower(), difficulty.lower())
    if quiz:
        quiz_key = f"{language}_{difficulty}_quiz"
        submit_key = f"{quiz_key}_submitted"
        score_key = f"{quiz_key}_score"

        # Initialize session state for answers and submission
        if quiz_key not in st.session_state:
            st.session_state[quiz_key] = [None] * len(quiz.questions)
        if submit_key not in st.session_state:
            st.session_state[submit_key] = False
        if score_key not in st.session_state:
            st.session_state[score_key] = 0

        # Show all questions
        for i, question in enumerate(quiz.questions):
            st.write(f"**Q{i+1}: {question['question']}**")
            answer_key = f"{quiz_key}_answer_{i}"
            if not st.session_state[submit_key]:
                # Save the answer to session state
                selected = st.radio(
                    "Select your answer:",
                    question['options'],
                    key=answer_key,
                    index=question['options'].index(st.session_state[quiz_key][i]) if st.session_state[quiz_key][i] in question['options'] else 0
                )
                st.session_state[quiz_key][i] = selected
            else:
                user_answer = st.session_state[quiz_key][i]
                correct = user_answer == question['correct_answer']
                if correct:
                    st.success(f"Your answer: {user_answer} ✅")
                else:
                    st.error(f"Your answer: {user_answer if user_answer else 'No answer selected'} ❌")
                    st.info(f"Correct answer: {question['correct_answer']}")
            st.markdown("---")

        # Submit button
        if not st.session_state[submit_key]:
            if st.button("Submit Quiz"):
                # Calculate score
                score = 0
                for i, question in enumerate(quiz.questions):
                    if st.session_state[quiz_key][i] == question['correct_answer']:
                        score += 1
                st.session_state[score_key] = score
                st.session_state[submit_key] = True
        else:
            st.success(f"Your Score: {st.session_state[score_key]} / {len(quiz.questions)}")
            if st.button("Reset Quiz"):
                st.session_state[quiz_key] = [None] * len(quiz.questions)
                st.session_state[submit_key] = False
                st.session_state[score_key] = 0 