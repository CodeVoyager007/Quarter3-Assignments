import streamlit as st
from data.progress import UserProgress
import plotly.express as px
import plotly.graph_objects as go
from typing import Dict

def get_achievement_icon(achievement: str) -> str:
    icons = {
        'python_master': '🐍',
        'javascript_master': '⚡',
        'typescript_master': '📘',
        'nextjs_master': '🚀',
        'python_challenge_master': '🏆',
        'javascript_challenge_master': '🏆',
        'typescript_challenge_master': '🏆',
        'dedicated_learner': '📚',
        'knowledge_seeker': '🎓'
    }
    return icons.get(achievement, '🏅')

def get_achievement_description(achievement: str) -> str:
    descriptions = {
        'python_master': 'Completed 10+ Python lessons',
        'javascript_master': 'Completed 10+ JavaScript lessons',
        'typescript_master': 'Completed 10+ TypeScript lessons',
        'nextjs_master': 'Completed 10+ Next.js lessons',
        'python_challenge_master': 'Completed 5+ Python challenges',
        'javascript_challenge_master': 'Completed 5+ JavaScript challenges',
        'typescript_challenge_master': 'Completed 5+ TypeScript challenges',
        'dedicated_learner': 'Completed 20+ lessons across all languages',
        'knowledge_seeker': 'Completed 50+ lessons across all languages'
    }
    return descriptions.get(achievement, 'Achievement unlocked!')

def create_progress_chart(stats: Dict) -> go.Figure:
    languages = ['Python', 'JavaScript', 'TypeScript', 'Next.js']
    completed_lessons = [
        len(stats['completed_lessons'].get(lang.lower(), set()))
        for lang in languages
    ]
    
    fig = go.Figure(data=[
        go.Bar(
            name='Completed Lessons',
            x=languages,
            y=completed_lessons,
            marker_color='#4CAF50'
        )
    ])
    
    fig.update_layout(
        title='Lessons Completed by Language',
        xaxis_title='Language',
        yaxis_title='Number of Lessons',
        template='plotly_white',
        height=400
    )
    
    return fig

def progress_dashboard():
    st.title("📊 Your Learning Progress")
    
    # Get user ID from session state or create a new one
    if 'user_id' not in st.session_state:
        st.session_state.user_id = "default_user"
    
    # Load user progress
    user_progress = UserProgress.load_progress(st.session_state.user_id)
    stats = user_progress.get_progress_stats()
    
    # Create columns for the main stats
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            label="Total Lessons Completed",
            value=stats['total_lessons_completed'],
            delta=f"{stats['total_lessons_completed']} lessons"
        )
    
    with col2:
        st.metric(
            label="Total Challenges Completed",
            value=stats['total_challenges_completed'],
            delta=f"{stats['total_challenges_completed']} challenges"
        )
    
    with col3:
        avg_score = sum(stats['average_quiz_score'].values()) / len(stats['average_quiz_score']) if stats['average_quiz_score'] else 0
        st.metric(
            label="Average Quiz Score",
            value=f"{avg_score:.1f}%",
            delta="across all languages"
        )
    
    # Display progress chart
    st.plotly_chart(create_progress_chart(user_progress.__dict__), use_container_width=True)
    
    # Display achievements
    st.header("🏆 Your Achievements")
    
    if not stats['achievements']:
        st.info("Complete lessons and challenges to earn achievements!")
    else:
        cols = st.columns(3)
        for i, achievement in enumerate(stats['achievements']):
            with cols[i % 3]:
                st.markdown(f"""
                <div style="
                    background: linear-gradient(145deg, #f0f0f0, #ffffff);
                    border-radius: 10px;
                    padding: 20px;
                    text-align: center;
                    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                    margin-bottom: 20px;
                ">
                    <h2 style="font-size: 2em; margin: 0;">{get_achievement_icon(achievement)}</h2>
                    <h3 style="margin: 10px 0;">{achievement.replace('_', ' ').title()}</h3>
                    <p style="color: #666;">{get_achievement_description(achievement)}</p>
                </div>
                """, unsafe_allow_html=True)
    
    # Display language-specific progress
    st.header("📚 Language Progress")
    
    for language in ['python', 'javascript', 'typescript', 'nextjs']:
        with st.expander(f"{language.title()} Progress"):
            col1, col2 = st.columns(2)
            
            with col1:
                lessons_completed = len(user_progress.completed_lessons.get(language, set()))
                st.metric(
                    label="Lessons Completed",
                    value=lessons_completed,
                    delta=f"out of {len(user_progress.completed_lessons.get(language, set()))} lessons"
                )
            
            with col2:
                if language != 'nextjs':  # Next.js doesn't have challenges
                    challenges_completed = len(user_progress.completed_challenges.get(language, set()))
                    st.metric(
                        label="Challenges Completed",
                        value=challenges_completed,
                        delta=f"out of {len(user_progress.completed_challenges.get(language, set()))} challenges"
                    )
            
            if language in user_progress.quiz_scores:
                quiz_scores = user_progress.quiz_scores[language]
                if quiz_scores:
                    avg_score = sum(quiz_scores.values()) / len(quiz_scores)
                    st.metric(
                        label="Average Quiz Score",
                        value=f"{avg_score:.1f}%",
                        delta=f"across {len(quiz_scores)} quizzes"
                    ) 