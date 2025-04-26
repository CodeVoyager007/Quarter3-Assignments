import streamlit as st
import requests

def run_python_code(code: str):
    try:
        # Redirect stdout to capture print output
        import io, sys
        old_stdout = sys.stdout
        sys.stdout = mystdout = io.StringIO()
        exec(code, {})
        sys.stdout = old_stdout
        return mystdout.getvalue()
    except Exception as e:
        return f"Error: {e}"

def run_code_with_piston(language: str, code: str):
    lang_map = {
        "javascript": "javascript",
        "typescript": "typescript"
    }
    payload = {
        "language": lang_map[language],
        "version": "*",
        "files": [{"content": code}]
    }
    try:
        resp = requests.post("https://emkc.org/api/v2/piston/execute", json=payload, timeout=10)
        if resp.status_code == 200:
            result = resp.json()
            return result.get("run", {}).get("output", "No output")
        else:
            return f"Error: {resp.text}"
    except Exception as e:
        return f"Error: {e}"

def playground_page():
    st.header("🧑‍💻 Code Playground")
    st.write("Write and run code in Python, JavaScript, or TypeScript!")

    language = st.selectbox("Select Language", ["Python", "JavaScript", "TypeScript"], key="playground_language")
    default_code = {
        "Python": 'print("Hello, Python!")',
        "JavaScript": 'console.log("Hello, JavaScript!");',
        "TypeScript": 'console.log("Hello, TypeScript!");'
    }
    code = st.text_area("Your Code", value=default_code[language], height=200, key=f"playground_{language}")

    if st.button("Run Code"):
        with st.spinner("Running code..."):
            if language == "Python":
                output = run_python_code(code)
            else:
                output = run_code_with_piston(language.lower(), code)
        st.subheader("Output:")
        st.code(output) 