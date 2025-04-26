import streamlit as st
import requests
import html

def fetch_interview_questions():
    url = "https://opentdb.com/api.php?amount=10&category=18&difficulty=easy"
    try:
        resp = requests.get(url, timeout=10)
        data = resp.json()
        if data.get("response_code") == 0:
            return data.get("results", [])
        else:
            return []
    except Exception as e:
        return []

def interview_prep_page():
    st.header("🧑‍💼 Interview Prep: Computer Science")
    st.write("Practice with real interview-style questions!")

    questions = fetch_interview_questions()
    if not questions:
        st.info("Could not fetch questions. Please try again later.")
        return

    # Session state for answers and submission
    if "interview_answers" not in st.session_state:
        st.session_state["interview_answers"] = [None] * len(questions)
    if "interview_submitted" not in st.session_state:
        st.session_state["interview_submitted"] = False
    if "interview_score" not in st.session_state:
        st.session_state["interview_score"] = 0

    for i, q in enumerate(questions):
        st.write(f"**Q{i+1}: {html.unescape(q['question'])}**")
        options = q["incorrect_answers"] + [q["correct_answer"]]
        options = [html.unescape(opt) for opt in options]
        # Shuffle options for fairness
        import random
        random.shuffle(options)
        answer_key = f"interview_answer_{i}"
        if not st.session_state["interview_submitted"]:
            selected = st.radio(
                "Select your answer:",
                options,
                key=answer_key,
                index=options.index(st.session_state["interview_answers"][i]) if st.session_state["interview_answers"][i] in options else 0
            )
            st.session_state["interview_answers"][i] = selected
        else:
            user_answer = st.session_state["interview_answers"][i]
            correct = user_answer == html.unescape(q["correct_answer"])
            if correct:
                st.success(f"Your answer: {user_answer} ✅")
            else:
                st.error(f"Your answer: {user_answer if user_answer else 'No answer selected'} ❌")
                st.info(f"Correct answer: {html.unescape(q['correct_answer'])}")
        st.markdown("---")

    # Submit button
    if not st.session_state["interview_submitted"]:
        if st.button("Submit Interview Prep Quiz"):
            score = 0
            for i, q in enumerate(questions):
                if st.session_state["interview_answers"][i] == html.unescape(q["correct_answer"]):
                    score += 1
            st.session_state["interview_score"] = score
            st.session_state["interview_submitted"] = True
            st.experimental_rerun() if hasattr(st, "experimental_rerun") else None
    else:
        st.success(f"Your Score: {st.session_state['interview_score']} / {len(questions)}")
        if st.button("Reset Interview Prep"):
            st.session_state["interview_answers"] = [None] * len(questions)
            st.session_state["interview_submitted"] = False
            st.session_state["interview_score"] = 0
            st.experimental_rerun() if hasattr(st, "experimental_rerun") else None 