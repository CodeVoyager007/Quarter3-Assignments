import streamlit as st

FREE_COURSES = [
    # Harvard 
    {
        "title": "CS50: Introduction to Computer Science",
        "provider": "Harvard (edX)",
        "description": "An entry-level course taught by David Malan, CS50 teaches students how to think algorithmically and solve problems efficiently.",
        "url": "https://www.edx.org/course/cs50s-introduction-to-computer-science"
    },
    {
        "title": "CS50's Web Programming with Python and JavaScript",
        "provider": "Harvard (edX)",
        "description": "Dive into web app design and implementation with Python, JavaScript, and SQL using frameworks like Flask and Django.",
        "url": "https://www.edx.org/course/cs50s-web-programming-with-python-and-javascript"
    },
    {
        "title": "CS50's Introduction to Artificial Intelligence with Python",
        "provider": "Harvard (edX)",
        "description": "Learn to use machine learning in Python in this introductory course on artificial intelligence.",
        "url": "https://www.edx.org/course/cs50s-introduction-to-artificial-intelligence-with-python"
    },
    {
        "title": "CS50's Introduction to Game Development",
        "provider": "Harvard (edX)",
        "description": "Learn about the development of 2D and 3D interactive games using frameworks like Unity and languages like Lua and C#.",
        "url": "https://www.edx.org/course/cs50s-introduction-to-game-development"
    },
    {
        "title": "CS50's Understanding Technology",
        "provider": "Harvard (edX)",
        "description": "A gentle introduction to technology for students who use computers every day but don't necessarily understand how they work.",
        "url": "https://www.edx.org/course/cs50s-understanding-technology"
    },
    {
        "title": "CS50's Computer Science for Business Professionals",
        "provider": "Harvard (edX)",
        "description": "For managers, product managers, founders, and decision-makers who want to understand what's possible and what's not in technology.",
        "url": "https://www.edx.org/course/cs50s-computer-science-for-business-professionals"
    },
    {
        "title": "CS50's Introduction to Programming with Scratch",
        "provider": "Harvard (edX)",
        "description": "A gentle introduction to programming that prepares you for future courses in computer science.",
        "url": "https://www.edx.org/course/cs50s-introduction-to-programming-with-scratch"
    },
    {
        "title": "CS50's AP® Computer Science Principles",
        "provider": "Harvard (edX)",
        "description": "A free online course for high school students preparing for the AP® Computer Science Principles exam.",
        "url": "https://www.edx.org/course/cs50s-ap-computer-science-principles"
    },
    {
        "title": "CS50's Introduction to Cybersecurity",
        "provider": "Harvard (edX)",
        "description": "Learn how to protect your data, devices, and yourself online.",
        "url": "https://www.edx.org/course/cs50s-introduction-to-cybersecurity"
    },
    {
        "title": "CS50's Introduction to Programming with Python",
        "provider": "Harvard (edX)",
        "description": "A gentle introduction to programming using Python.",
        "url": "https://www.edx.org/course/cs50s-introduction-to-programming-with-python"
    },
    # freeCodeCamp
    {
        "title": "freeCodeCamp Responsive Web Design Certification",
        "provider": "freeCodeCamp",
        "description": "Learn HTML, CSS, and build 15 responsive web projects.",
        "url": "https://www.freecodecamp.org/learn/2022/responsive-web-design/"
    },
    {
        "title": "freeCodeCamp JavaScript Algorithms and Data Structures",
        "provider": "freeCodeCamp",
        "description": "Learn JavaScript, ES6, regular expressions, data structures, and algorithms.",
        "url": "https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/"
    },
    {
        "title": "freeCodeCamp Front End Development Libraries",
        "provider": "freeCodeCamp",
        "description": "Learn React, Redux, Bootstrap, jQuery, and Sass.",
        "url": "https://www.freecodecamp.org/learn/front-end-development-libraries/"
    },
    {
        "title": "freeCodeCamp Data Visualization",
        "provider": "freeCodeCamp",
        "description": "Learn D3.js and JSON APIs to create data visualizations.",
        "url": "https://www.freecodecamp.org/learn/data-visualization/"
    },
    {
        "title": "freeCodeCamp Back End Development and APIs",
        "provider": "freeCodeCamp",
        "description": "Learn Node.js, Express, MongoDB, and build APIs.",
        "url": "https://www.freecodecamp.org/learn/back-end-development-and-apis/"
    },
    {
        "title": "freeCodeCamp Scientific Computing with Python",
        "provider": "freeCodeCamp",
        "description": "Learn Python, NumPy, Pandas, Matplotlib, and build scientific computing projects.",
        "url": "https://www.freecodecamp.org/learn/scientific-computing-with-python/"
    },
    {
        "title": "freeCodeCamp Machine Learning with Python",
        "provider": "freeCodeCamp",
        "description": "Learn machine learning concepts and libraries in Python.",
        "url": "https://www.freecodecamp.org/learn/machine-learning-with-python/"
    },
    {
        "title": "freeCodeCamp Information Security Certification",
        "provider": "freeCodeCamp",
        "description": "Learn about information security, cryptography, and secure web development.",
        "url": "https://www.freecodecamp.org/learn/information-security/"
    },
    {
        "title": "freeCodeCamp Quality Assurance Certification",
        "provider": "freeCodeCamp",
        "description": "Learn about testing, Chai, Mocha, and build quality assurance projects.",
        "url": "https://www.freecodecamp.org/learn/quality-assurance/"
    },
    {
        "title": "freeCodeCamp Relational Database Certification",
        "provider": "freeCodeCamp",
        "description": "Learn SQL, PostgreSQL, and build database-backed applications.",
        "url": "https://www.freecodecamp.org/learn/relational-database/"
    }
]

def free_courses_page():
    st.header("🌐 Free Programming Courses (Harvard & freeCodeCamp)")
    st.write(
        "Below are free programming courses from Harvard (edX) and freeCodeCamp. "
        "These courses are provided by their respective organizations, and I have permission to list and link to them here. "
        "**All course content and rights belong to Harvard and freeCodeCamp.**"
    )

    search = st.text_input("Search courses by keyword (e.g., Python, web, AI, React):").lower()

    filtered_courses = [
        course for course in FREE_COURSES
        if search in course["title"].lower() or search in course["description"].lower() or search in course["provider"].lower()
    ] if search else FREE_COURSES

    if not filtered_courses:
        st.warning("No courses found for your search.")
    else:
        for course in filtered_courses:
            st.subheader(f"{course['title']} ({course['provider']})")
            st.write(course["description"])
            st.markdown(f"[Go to course]({course['url']})")
            st.markdown("---") 