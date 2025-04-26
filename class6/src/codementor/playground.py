import streamlit as st
import requests

# List of languages supported by Piston API (as of 2024)
PISTON_LANGUAGES = [
    "python", "javascript", "typescript", "java", "c", "cpp", "csharp", "go", "ruby", "php",
    "swift", "rust", "kotlin", "scala", "perl", "haskell", "lua", "r", "dart", "elixir",
    "clojure", "fsharp", "ocaml", "groovy", "bash", "powershell", "fortran", "zig", "nim"
]

DEFAULT_CODE = {
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

def playground_page():
    st.header("🧑‍💻 Code Playground")
    st.write("Write and run code in your favorite language!")

    language = st.selectbox("Select Language", sorted(PISTON_LANGUAGES), key="playground_language")
    code = st.text_area("Your Code", value=DEFAULT_CODE.get(language, ""), height=200, key=f"playground_{language}")

    if st.button("Run Code"):
        with st.spinner("Running code..."):
            output = run_code_with_piston(language, code)
        st.subheader("Output:")
        st.code(output) 