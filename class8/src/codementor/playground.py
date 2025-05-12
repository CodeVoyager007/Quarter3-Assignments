import streamlit as st
import requests
import json
from datetime import datetime
import pyperclip  # Add this import for clipboard functionality

class CodePlayground:
    def __init__(self):
        self.PISTON_LANGUAGES = [
            "python", "javascript", "typescript", "java", "c", "cpp", "csharp", "go", "ruby", "php",
            "swift", "rust", "kotlin", "scala", "perl", "haskell", "lua", "r", "dart", "elixir",
            "clojure", "fsharp", "ocaml", "groovy", "bash", "powershell", "fortran", "zig", "nim"
        ]

        self.DEFAULT_CODE = {
            "python": 'print("Hello, Python!")',
            "javascript": 'console.log("Hello, JavaScript!");',
            "typescript": 'console.log("Hello, TypeScript!");',
            "java": 'public class Main { public static void main(String[] args) { System.out.println("Hello, Java!"); } }',
            "c": '#include <stdio.h>\nint main() { printf("Hello, C!\\n"); return 0; }',
            "cpp": '#include <iostream>\nint main() { std::cout << "Hello, C++!\\n"; return 0; }',
            "csharp": 'using System; class Program { static void Main() { Console.WriteLine("Hello, C#!"); } }',
            "go": 'package main\nimport "fmt"\nfunc main() { fmt.Println("Hello, Go!") }',
            "ruby": 'puts "Hello, Ruby!"',
            "php": '<?php echo "Hello, PHP!"; ?>',
            "swift": 'print("Hello, Swift!")',
            "rust": 'fn main() { println!("Hello, Rust!"); }',
            "kotlin": 'fun main() { println("Hello, Kotlin!") }',
            "scala": 'object Main extends App { println("Hello, Scala!") }',
            "perl": 'print "Hello, Perl!\\n";',
            "haskell": 'main = putStrLn "Hello, Haskell!"',
            "lua": 'print("Hello, Lua!")',
            "r": 'cat("Hello, R!\\n")',
            "dart": 'void main() { print("Hello, Dart!"); }',
            "elixir": 'IO.puts "Hello, Elixir!"',
            "clojure": '(println "Hello, Clojure!")',
            "fsharp": 'printfn "Hello, F#!"',
            "ocaml": 'print_endline "Hello, OCaml!";;',
            "groovy": 'println "Hello, Groovy!"',
            "bash": 'echo "Hello, Bash!"',
            "powershell": 'Write-Output "Hello, PowerShell!"',
            "fortran": 'program hello\nprint *, "Hello, Fortran!"\nend program hello',
            "zig": 'const std = @import("std");\npub fn main() void { std.debug.print("Hello, Zig!\\n", .{}); }',
            "nim": 'echo "Hello, Nim!"'
        }

        # Initialize code snippets storage
        if "saved_snippets" not in st.session_state:
            st.session_state.saved_snippets = {}

    def run_python_code(self, code: str):
        try:
            import io, sys
            old_stdout = sys.stdout
            sys.stdout = mystdout = io.StringIO()
            exec(code, {})
            sys.stdout = old_stdout
            return mystdout.getvalue()
        except Exception as e:
            return f"Error: {e}"

    def run_code_with_piston(self, language: str, code: str):
        payload = {
            "language": language,
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

    def copy_to_clipboard(self, text: str) -> bool:
        try:
            pyperclip.copy(text)
            return True
        except Exception:
            return False

    def render_code_editor(self):
        st.subheader("📝 Code Editor")
        language = st.selectbox("Select Language", sorted(self.PISTON_LANGUAGES), key="playground_language")
        code = st.text_area("Your Code", value=self.DEFAULT_CODE.get(language, ""), height=200, key=f"playground_{language}")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Run Code"):
                with st.spinner("Running code..."):
                    output = self.run_code_with_piston(language, code)
                st.subheader("Output:")
                st.code(output)

        with col2:
            if st.button("📋 Copy Code"):
                if self.copy_to_clipboard(code):
                    st.success("Code copied to clipboard!")
                else:
                    st.error("Failed to copy code. Please try again.")

    def render_snippets(self):
        st.subheader("💾 Saved Snippets")
        if not st.session_state.saved_snippets:
            st.info("No saved snippets yet. Save your code to see it here!")
            return

        for name, snippet in st.session_state.saved_snippets.items():
            with st.expander(f"{name} ({snippet['language']}) - {snippet['timestamp']}"):
                st.code(snippet['code'], language=snippet['language'])
                if st.button("Load", key=f"load_{name}"):
                    st.session_state.playground_language = snippet['language']
                    st.session_state[f"playground_{snippet['language']}"] = snippet['code']
                    st.rerun()

    def render(self):
        st.header("🧑‍💻 Code Playground")
        st.write("Write and run code in your favorite language!")

        # Create tabs for different features
        tab1, tab2 = st.tabs(["Code Editor", "Saved Snippets"])
        
        with tab1:
            self.render_code_editor()
        
        with tab2:
            self.render_snippets()

def playground_page():
    playground = CodePlayground()
    playground.render() 