import streamlit as st
from data.challenges import PYTHON_CHALLENGES, JAVASCRIPT_CHALLENGES, TYPESCRIPT_CHALLENGES, NEXTJS_CHALLENGES

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
        is_correct = user_solution.strip() == self.solution.strip()
        if is_correct and not self.completed:
            self.completed = True
            if 'user_progress' in st.session_state:
                st.session_state.user_progress.add_completed_challenge(self.language, self.title)
        return is_correct

def get_challenges(language: str, difficulty: str):
    challenges_data = {
        'python': PYTHON_CHALLENGES,
        'javascript': JAVASCRIPT_CHALLENGES,
        'typescript': TYPESCRIPT_CHALLENGES,
        'nextjs': NEXTJS_CHALLENGES
    }
    return [
        Challenge(**challenge_data)
        for challenge_data in challenges_data.get(language.lower(), {}).get(difficulty.lower(), [])
    ]

def challenges_page():
    st.header("Challenges")
    language = st.selectbox("Select Language", ["Python", "JavaScript", "TypeScript", "Next.js"], key="challenges_language")
    difficulty = st.selectbox("Select Difficulty", ["Beginner", "Intermediate", "Advanced"], key="challenges_difficulty")
    st.subheader(f"{language} Challenges - {difficulty}")
    
    challenges = get_challenges(language.lower(), difficulty.lower())
    if not challenges:
        st.info("No challenges available for this selection.")
    else:
        # Load user progress to check completion status
        if 'user_progress' in st.session_state:
            user_progress = st.session_state.user_progress
            for challenge in challenges:
                challenge.completed = challenge.title in user_progress.completed_challenges.get(challenge.language, set())
        
        for idx, challenge in enumerate(challenges, 1):
            with st.expander(f"{'✅ ' if challenge.completed else ''}Challenge {idx} of {len(challenges)}: {challenge.title}"):
                color = {"Beginner": "green", "Intermediate": "orange", "Advanced": "red"}[difficulty]
                st.markdown(f'<span style="background-color:{color}; color:white; padding:2px 8px; border-radius:8px;">{difficulty}</span>', unsafe_allow_html=True)
                st.write(challenge.description)
                
                key_prefix = f"{language}_{difficulty}_{idx}"
                input_key = f"challenge_input_{key_prefix}"
                attempts_key = f"challenge_attempts_{key_prefix}"
                show_solution_key = f"show_solution_{key_prefix}"

                # Initialize session state for the input and attempts if not already set
                if input_key not in st.session_state:
                    st.session_state[input_key] = ""
                if attempts_key not in st.session_state:
                    st.session_state[attempts_key] = 0
                if show_solution_key not in st.session_state:
                    st.session_state[show_solution_key] = False

                user_solution = st.text_area(
                    "Your Solution",
                    key=input_key,
                    value=st.session_state[input_key]
                )

                col1, col2 = st.columns([1,1])
                with col1:
                    check = st.button("Check Solution", key=f"check_{key_prefix}")
                with col2:
                    # Only enable "Show Solution" after 3 wrong attempts
                    show = st.button(
                        "Show Solution",
                        key=f"show_{key_prefix}",
                        disabled=st.session_state[attempts_key] < 3
                    )

                if check:
                    if challenge.check_solution(user_solution):
                        st.success("✅ Correct! Well done!")
                        st.session_state[attempts_key] = 0  # Reset attempts on success
                        st.session_state[show_solution_key] = False
                        st.rerun()  # Rerun to update the UI
                    else:
                        st.session_state[attempts_key] += 1
                        st.error("❌ Try again!")
                        if challenge.hint:
                            st.info(f"Hint: {challenge.hint}")

                if show:
                    st.code(challenge.solution, language=challenge.language) 