# Library Assistant (Assignment - August 11)

This project implements a **Library Assistant** using the OpenAI Agents SDK (with Gemini API).  
The assistant can search for books, check book availability (for registered members), provide library timings, and ignore non-library questions.

---

## Features

- **Search for Books:**  
  Ask if a book exists in the library.

- **Check Book Availability:**  
  Only registered members can check how many copies are available.

- **Library Timings:**  
  Get the library's opening hours.

- **Guardrails:**  
  Non-library-related queries are ignored.


---

## How It Works

- **User Context:**  
  Each user has a name and optional member ID.

- **Guardrail Agent:**  
  Filters out non-library queries using an input guardrail.

- **Function Tools:**  
  - `search_book`: Checks if a book exists.
  - `check_availability`: Checks available copies (members only).
  - `library_timings`: Returns library hours.

- **Dynamic Instructions:**  
  The agent greets the user by name and provides concise answers.

- **Book Database:**  
  Books and their available copies are stored in a Python dictionary.

---

## Setup & Usage

1. **Clone the repository**
2. **Create a virtual environment**
   ```sh
   uv venv
   ```
3. **Activate the virtual environment**
   - On Windows:
     ```sh
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```sh
     source venv/bin/activate
     ```
4. **Install dependencies**
   ```sh
   uv add -r requirements.txt
   ```

3. **Set up your `.env` file**
   ```
   GEMINI_API_KEY=your-gemini-api-key-here
   ```

4. **Run the assistant**
   ```sh
   uv main.py
   ```

---

## Example Queries

- `Search for Harry Potter and The Chamber of Secrets book`
- `Check availability of AI Revolution`
- `What are the library timings?`
- `Who is Imran Khan?` (will be ignored)

---
