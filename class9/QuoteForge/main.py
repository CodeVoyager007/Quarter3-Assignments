import streamlit as st
from PIL import Image
import io
from src.poster import Poster, PosterThemes
from src.auth import Auth
from src.payment import Payment
from pathlib import Path

# Initialize authentication and payment
auth = Auth()
payment = Payment()

st.set_page_config(
    page_title="QuoteForge - Shape Words Into Art",
    page_icon="🎨",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    .main {
        padding: 2rem;
    }
    h1 {
        color: #1E88E5;
    }
    .css-1d391kg {
        padding-top: 1rem;
    }
</style>
""", unsafe_allow_html=True)

def login_page():
    st.title("🎨 QuoteForge")
    st.subheader("Login to Create Beautiful Quotes")
    
    with st.form("login_form"):
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Login")
        
        if submitted:
            result = auth.login(email, password)
            if result:
                st.session_state["auth_token"] = result["token"]
                st.success("Login successful!")
                st.rerun()
            else:
                st.error("Invalid credentials")
    
    st.markdown("---")
    st.markdown("""
    ### Demo Accounts:
    - Free User: demo@quoteforge.com / demo123
    - Pro User: pro@quoteforge.com / pro123
    """)

def main_app():
    # App Header
    col1, col2 = st.columns([3, 1])
    with col1:
        st.title("🎨 QuoteForge")
        st.subheader("Shape Words Into Art")
    with col2:
        if st.button("Logout"):
            auth.logout()
            st.rerun()

    # Sidebar Configuration
    st.sidebar.title("Customize Your Poster")

    # Quote Input
    quote = st.sidebar.text_area("Enter Your Quote", placeholder="Type your quote here...", height=100)
    author = st.sidebar.text_input("Author Name", placeholder="Anonymous")

    # Theme Selection
    theme_options = {
        "Minimal": PosterThemes.MINIMAL,
        "Elegant": PosterThemes.ELEGANT,
        "Bold": PosterThemes.BOLD
    }
    selected_theme = st.sidebar.selectbox("Choose Theme", list(theme_options.keys()))

    # Advanced Options
    with st.sidebar.expander("Advanced Options"):
        text_position = st.selectbox(
            "Text Position",
            ["middle", "top", "bottom"],
            index=0
        )
        
        blur_background = st.checkbox("Blur Background", value=True)
        
        # Get subscription status
        is_pro = auth.get_user_subscription() == "pro"
        if not is_pro:
            st.info("👉 Upgrade to Pro for HD quality and no watermarks!")
        
        resolution = (1080, 1080) if is_pro else (720, 720)

    # Background Options
    st.sidebar.markdown("---")
    st.sidebar.markdown("### Background Options")
    background_source = st.sidebar.radio(
        "Choose Background Source",
        ["Unsplash Random", "Upload Image"],
        index=0
    )

    background_image = None
    if background_source == "Upload Image":
        uploaded_file = st.sidebar.file_uploader("Upload Background Image", type=["png", "jpg", "jpeg"])
        if uploaded_file is not None:
            background_image = Image.open(uploaded_file)

    # Generate Button
    if st.sidebar.button("Generate Poster", type="primary"):
        if not quote:
            st.error("Please enter a quote!")
        else:
            try:
                # Create poster
                poster = Poster(
                    width=resolution[0],
                    height=resolution[1],
                    theme=theme_options[selected_theme]
                )
                
                # Generate image
                result = poster.generate(
                    quote=quote,
                    author=author,
                    background_image=background_image,
                    text_position=text_position,
                    blur_background=blur_background,
                    watermark=not is_pro
                )
                
                # Save to buffer
                buf = io.BytesIO()
                poster.save(result, buf)
                
                # Display preview
                st.image(buf, caption="Your Quote Poster", use_container_width=True)
                
                # Download button
                st.download_button(
                    label="Download Poster",
                    data=buf,
                    file_name=f"quoteforge_poster.png",
                    mime="image/png"
                )
                
            except Exception as e:
                st.error(f"Error generating poster: {str(e)}")

    # Show pricing for non-pro users
    if not is_pro:
        st.sidebar.markdown("---")
        payment.display_pricing()

# Main app flow
if not auth.is_authenticated():
    login_page()
else:
    main_app()
