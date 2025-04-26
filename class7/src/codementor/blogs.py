import streamlit as st
import requests

def fetch_blogs():
    url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=126457c4b51548baaab61e1e1651aa1e"
    try:
        response = requests.get(url)
        data = response.json()
        if data.get("status") == "ok":
            return data.get("articles", [])
        else:
            return []
    except Exception as e:
        return []

def blogs_page():
    st.header("📰 Daily TechCrunch Blogs")
    blogs = fetch_blogs()
    if not blogs:
        st.info("No blogs available or failed to fetch blogs. Please check your API key or try again later.")
    else:
        for blog in blogs:
            st.subheader(blog.get("title", "No Title"))
            st.write(blog.get("description", "No Description"))
            if blog.get("urlToImage"):
                st.image(blog["urlToImage"], width=400)
            st.markdown(f"[Read more]({blog.get('url', '#')})")
            st.markdown("---") 