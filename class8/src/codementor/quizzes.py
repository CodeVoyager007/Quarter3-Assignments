import streamlit as st
from typing import List, Dict, Optional
from data.quizzes import PYTHON_QUIZZES, JAVASCRIPT_QUIZZES, TYPESCRIPT_QUIZZES

class Quiz:
    def __init__(self, questions: List[Dict], language: str, difficulty: str):
        self.questions = questions
        self.language = language
        self.difficulty = difficulty
        self.score = 0
        self.completed = False

    def check_answers(self, answers: List[str]) -> int:
        correct = 0
        for i, (question, answer) in enumerate(zip(self.questions, answers)):
            if answer == question['correct_answer']:
                correct += 1
        self.score = (correct / len(self.questions)) * 100
        if not self.completed:
            self.completed = True
            if 'user_progress' in st.session_state:
                st.session_state.user_progress.add_quiz_score(
                    self.language,
                    f"{self.difficulty}_quiz",
                    self.score
                )
        return self.score

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
    language = st.selectbox("Select Language", ["Python", "JavaScript", "TypeScript", "Next.js"], key="quizzes_language")
    difficulty = st.selectbox("Select Difficulty", ["Beginner", "Intermediate", "Advanced"], key="quizzes_difficulty")
    st.subheader(f"{language} Quiz - {difficulty}")
    
    quiz = get_quiz(language.lower(), difficulty.lower())
    if quiz:
        quiz_key = f"{language}_{difficulty}_quiz"
        submit_key = f"{quiz_key}_submitted"
        score_key = f"{quiz_key}_score"

        # Check if quiz is completed
        if 'user_progress' in st.session_state:
            quiz_id = f"{difficulty.lower()}_quiz"
            if quiz_id in st.session_state.user_progress.quiz_scores.get(language.lower(), {}):
                quiz.completed = True
                quiz.score = st.session_state.user_progress.quiz_scores[language.lower()][quiz_id]

        # Initialize session state for answers and submission
        if quiz_key not in st.session_state:
            st.session_state[quiz_key] = [None] * len(quiz.questions)
        if submit_key not in st.session_state:
            st.session_state[submit_key] = False
        if score_key not in st.session_state:
            st.session_state[score_key] = 0

        # Display completion status
        if quiz.completed:
            st.success(f"✅ Quiz completed! Your score: {quiz.score:.1f}%")

        # Display questions
        for i, question in enumerate(quiz.questions):
            st.write(f"**{i+1}. {question['question']}**")
            options = question['options']
            answer = st.radio(
                "Select your answer:",
                options,
                key=f"{quiz_key}_q{i}",
                index=None if st.session_state[quiz_key][i] is None else options.index(st.session_state[quiz_key][i])
            )
            st.session_state[quiz_key][i] = answer

        # Submit button
        if not quiz.completed and st.button("Submit Quiz", key=f"{quiz_key}_submit"):
            if None in st.session_state[quiz_key]:
                st.error("Please answer all questions before submitting.")
            else:
                score = quiz.check_answers(st.session_state[quiz_key])
                st.session_state[score_key] = score
                st.session_state[submit_key] = True
                st.success(f"Quiz submitted! Your score: {score:.1f}%")
                st.rerun()  # Rerun to update the UI

        # Show results if submitted
        if st.session_state[submit_key]:
            st.write("### Results")
            for i, (question, answer) in enumerate(zip(quiz.questions, st.session_state[quiz_key])):
                is_correct = answer == question['correct_answer']
                st.write(f"**{i+1}. {question['question']}**")
                st.write(f"Your answer: {answer}")
                st.write(f"Correct answer: {question['correct_answer']}")
                st.write("✅ Correct!" if is_correct else "❌ Incorrect")
                st.write("---")
    else:
        st.info("No quiz available for this selection.") 