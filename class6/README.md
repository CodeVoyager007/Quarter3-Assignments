# CodeMentor - Interactive Programming Learning Platform

CodeMentor is an interactive learning platform designed to help beginners learn programming languages in a structured and engaging way. It provides lessons, challenges, and quizzes for multiple programming languages with different difficulty levels.

## Features

- Interactive lessons for Python, JavaScript, and Java
- Three difficulty levels: Beginner, Intermediate, and Advanced
- Practice challenges with instant feedback
- Interactive quizzes to test your knowledge
- Progress tracking
- Beautiful and intuitive UI built with Streamlit

## Installation

1. Clone this repository
2. Create a virtual environment using UV:
```bash
uv init codementor
uv add streamlit
uv add pandas
uv add numpy
```

3. Run the application:
```bash
streamlit run main.py
```

## Project Structure

- `main.py`: Main application entry point
- `models/`: Contains OOP classes for lessons, challenges, and quizzes
- `data/`: Contains lesson content and quiz questions
- `utils/`: Helper functions and utilities

## How to Use

1. Launch the application using the command above
2. Select your preferred programming language
3. Choose your difficulty level
4. Start with lessons or jump straight to challenges
5. Take quizzes to test your knowledge
6. Track your progress as you learn

## Contributing

Feel free to contribute to this project by adding more lessons, challenges, or improving the existing content. 