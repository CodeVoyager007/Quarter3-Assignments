import streamlit as st
import requests
import html

class InterviewPrep:
    def __init__(self):
        self.api_url = "https://opentdb.com/api.php?amount=10&category=18&difficulty=easy"
        self.initialize_session_state()

    def initialize_session_state(self):
        if "interview_answers" not in st.session_state:
            st.session_state["interview_answers"] = []
        if "interview_submitted" not in st.session_state:
            st.session_state["interview_submitted"] = False
        if "interview_score" not in st.session_state:
            st.session_state["interview_score"] = 0

    def fetch_questions(self):
        try:
            resp = requests.get(self.api_url, timeout=10)
            data = resp.json()
            if data.get("response_code") == 0:
                return data.get("results", [])
            else:
                return []
        except Exception as e:
            return []

    def display_question(self, q: dict, index: int):
        st.write(f"**Q{index+1}: {html.unescape(q['question'])}**")
        options = q["incorrect_answers"] + [q["correct_answer"]]
        options = [html.unescape(opt) for opt in options]
        # Shuffle options for fairness
        import random
        random.shuffle(options)
        answer_key = f"interview_answer_{index}"
        
        if not st.session_state["interview_submitted"]:
            selected = st.radio(
                "Select your answer:",
                options,
                key=answer_key,
                index=options.index(st.session_state["interview_answers"][index]) if st.session_state["interview_answers"][index] in options else 0
            )
            st.session_state["interview_answers"][index] = selected
        else:
            user_answer = st.session_state["interview_answers"][index]
            correct = user_answer == html.unescape(q["correct_answer"])
            if correct:
                st.success(f"Your answer: {user_answer} ✅")
            else:
                st.error(f"Your answer: {user_answer if user_answer else 'No answer selected'} ❌")
                st.info(f"Correct answer: {html.unescape(q['correct_answer'])}")
        st.markdown("---")

    def calculate_score(self, questions: list) -> int:
        score = 0
        for i, q in enumerate(questions):
            if st.session_state["interview_answers"][i] == html.unescape(q["correct_answer"]):
                score += 1
        return score

    def reset_quiz(self, questions: list):
        st.session_state["interview_answers"] = [None] * len(questions)
        st.session_state["interview_submitted"] = False
        st.session_state["interview_score"] = 0
        st.experimental_rerun() if hasattr(st, "experimental_rerun") else None

    def render(self):
        st.header("🧑‍💼 Interview Prep: Computer Science")
        st.write("Practice with real interview-style questions!")

        questions = self.fetch_questions()
        if not questions:
            st.info("Could not fetch questions. Please try again later.")
            return

        # Initialize answers array if needed
        if len(st.session_state["interview_answers"]) != len(questions):
            st.session_state["interview_answers"] = [None] * len(questions)

        # Display questions
        for i, q in enumerate(questions):
            self.display_question(q, i)

        # Submit button
        if not st.session_state["interview_submitted"]:
            if st.button("Submit Interview Prep Quiz"):
                st.session_state["interview_score"] = self.calculate_score(questions)
                st.session_state["interview_submitted"] = True
                st.experimental_rerun() if hasattr(st, "experimental_rerun") else None
        else:
            st.success(f"Your Score: {st.session_state['interview_score']} / {len(questions)}")
            if st.button("Reset Interview Prep"):
                self.reset_quiz(questions)

def interview_prep_page():
    prep = InterviewPrep()
    prep.render() 