import streamlit as st
from PIL import Image
import io
from src.poster import Poster, PosterThemes
from pathlib import Path

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
</style>
""", unsafe_allow_html=True)

# App Header
st.title("🎨 QuoteForge")
st.subheader("Shape Words Into Art")

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
    
    blur_background = st.checkbox("Blur Background", value=False)
    
    # Resolution selection based on "pro" status
    is_pro = st.checkbox("Pro Version", value=False)
    resolution = (1080, 1080) if is_pro else (720, 720)

# Image Upload
uploaded_file = st.sidebar.file_uploader("Upload Background Image (Optional)", type=["png", "jpg", "jpeg"])
background_image = None
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
            st.image(buf, caption="Your Quote Poster", use_column_width=True)
            
            # Download button
            st.download_button(
                label="Download Poster",
                data=buf,
                file_name=f"quoteforge_poster.png",
                mime="image/png"
            )
            
        except Exception as e:
            st.error(f"Error generating poster: {str(e)}")

# Initial preview/instructions
if not quote:
    st.info("👈 Start by entering your quote in the sidebar!")
