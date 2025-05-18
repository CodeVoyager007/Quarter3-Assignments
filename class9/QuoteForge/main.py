import streamlit as st
from PIL import Image
import io
import base64
from src.poster import Poster, PosterThemes
from src.auth import Auth
from src.payment import Payment
from pathlib import Path

# Initialize authentication and payment
auth = Auth()
payment = Payment()

# Load and encode logo image
logo_path = Path(__file__).parent / "assets" / "QuoteForge.png"
if logo_path.exists():
    with open(logo_path, "rb") as f:
        logo_base64 = base64.b64encode(f.read()).decode()
else:
    logo_base64 = ""

st.set_page_config(
    page_title="QuoteForge - Shape Words Into Art",
    page_icon="🎨",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom CSS with dark theme
st.markdown("""
<style>
    /* Dark theme colors */
    :root {
        --background-color: #0A0F1C;
        --text-color: #D1D5DB;
        --accent-color: #00E1FF;
        --secondary-bg: #1E293B;
    }

    .stApp {
        background-color: var(--background-color);
        color: var(--text-color);
        max-width: 1200px;
        margin: 0 auto;
    }
    
    .main {
        padding: 2rem;
    }
    
    h1, h2, h3 {
        color: var(--text-color) !important;
    }
    
    .stButton>button {
        background-color: var(--accent-color);
        color: var(--background-color);
        border: none;
        font-weight: bold;
    }
    
    .stTextInput>div>div>input, .stTextArea>div>div>textarea {
        background-color: var(--secondary-bg);
        color: var(--text-color);
        border: 1px solid var(--accent-color);
    }
    
    .stSelectbox>div>div {
        background-color: var(--secondary-bg);
        color: var(--text-color);
    }
    
    .sidebar .sidebar-content {
        background-color: var(--secondary-bg);
    }
    
    /* Custom header with logo */
    .header-container {
        display: flex;
        align-items: center;
        gap: 1rem;
        margin-bottom: 1rem;
    }
    
    .header-container img {
        width: 50px;
        height: auto;
    }
</style>
""", unsafe_allow_html=True)

def login_page():
    st.markdown(f"""
        <div class="header-container">
            <img src="data:image/png;base64,{logo_base64}" alt="QuoteForge Logo"/>
            <h1>QuoteForge</h1>
        </div>
    """, unsafe_allow_html=True)
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
    - Free User: demo@quoteforge.com / demouser2314
    - Pro User: pro@quoteforge.com / prouser2134
    """)

def main_app():
    # App Header with Logo
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown(f"""
            <div class="header-container">
                <img src="data:image/png;base64,{logo_base64}" alt="QuoteForge Logo"/>
                <h1>QuoteForge</h1>
            </div>
        """, unsafe_allow_html=True)
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
