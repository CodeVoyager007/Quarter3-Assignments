import streamlit as st

# Static list of popular free Harvard programming courses on edX
HARVARD_COURSES = [
    {
        "title": "CS50: Introduction to Computer Science",
        "description": "An entry-level course taught by David Malan, CS50 teaches students how to think algorithmically and solve problems efficiently.",
        "url": "https://www.edx.org/course/cs50s-introduction-to-computer-science"
    },
    {
        "title": "CS50's Web Programming with Python and JavaScript",
        "description": "This course dives more deeply into the design and implementation of web apps with Python, JavaScript, and SQL using frameworks like Flask, Django, and Bootstrap.",
        "url": "https://www.edx.org/course/cs50s-web-programming-with-python-and-javascript"
    },
    {
        "title": "CS50's Introduction to Artificial Intelligence with Python",
        "description": "Learn to use machine learning in Python in this introductory course on artificial intelligence.",
        "url": "https://www.edx.org/course/cs50s-introduction-to-artificial-intelligence-with-python"
    },
    {
        "title": "CS50's Introduction to Game Development",
        "description": "Learn about the development of 2D and 3D interactive games using frameworks like Unity and languages like Lua and C#.",
        "url": "https://www.edx.org/course/cs50s-introduction-to-game-development"
    },
    {
        "title": "CS50's Understanding Technology",
        "description": "A gentle introduction to technology for students who use computers every day but don't necessarily understand how they work.",
        "url": "https://www.edx.org/course/cs50s-understanding-technology"
    },
    {
        "title": "CS50's Computer Science for Business Professionals",
        "description": "This course is designed for managers, product managers, founders, and decision-makers who want to understand what's possible and what's not in technology.",
        "url": "https://www.edx.org/course/cs50s-computer-science-for-business-professionals"
    },
    {
        "title": "CS50's Introduction to Programming with Scratch",
        "description": "A gentle introduction to programming that prepares you for future courses in computer science.",
        "url": "https://www.edx.org/course/cs50s-introduction-to-programming-with-scratch"
    }
]

def harvard_courses_page():
    st.header("🎓 Harvard Free Programming Courses (edX)")
    st.write("Search and explore free online programming courses from Harvard University on edX.")

    search = st.text_input("Search courses by keyword (e.g., Python, AI, web, game):").lower()

    filtered_courses = [
        course for course in HARVARD_COURSES
        if search in course["title"].lower() or search in course["description"].lower()
    ] if search else HARVARD_COURSES

    if not filtered_courses:
        st.warning("No courses found for your search.")
    else:
        for course in filtered_courses:
            st.subheader(course["title"])
            st.write(course["description"])
            st.markdown(f"[Go to course on edX]({course['url']})")
            st.markdown("---") 