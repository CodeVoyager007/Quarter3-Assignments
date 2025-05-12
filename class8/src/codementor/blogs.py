import streamlit as st
import requests

class TechBlogs:
    def __init__(self):
        self.api_url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=126457c4b51548baaab61e1e1651aa1e"

    def fetch_blogs(self):
        try:
            response = requests.get(self.api_url)
            data = response.json()
            if data.get("status") == "ok":
                return data.get("articles", [])
            else:
                return []
        except Exception as e:
            return []

    def display_blog(self, blog: dict):
        st.subheader(blog.get("title", "No Title"))
        st.write(blog.get("description", "No Description"))
        if blog.get("urlToImage"):
            st.image(blog["urlToImage"], width=400)
        st.markdown(f"[Read more]({blog.get('url', '#')})")
        st.markdown("---")

    def render(self):
        st.header("📰 Daily TechCrunch Blogs")
        blogs = self.fetch_blogs()
        if not blogs:
            st.info("No blogs available or failed to fetch blogs. Please check your API key or try again later.")
        else:
            for blog in blogs:
                self.display_blog(blog)

def blogs_page():
    blogs = TechBlogs()
    blogs.render() 