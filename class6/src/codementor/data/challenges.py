PYTHON_CHALLENGES = {
    'beginner': [
        {
            'title': 'Hello World',
            'description': 'Write a program that prints "Hello, World!" to the console.',
            'solution': 'print("Hello, World!")',
            'language': 'python',
            'difficulty': 'beginner'
        },
        {
            'title': 'Sum of Two Numbers',
            'description': 'Write a function that takes two numbers as input and returns their sum.',
            'solution': 'def add(a, b):\n    return a + b',
            'language': 'python',
            'difficulty': 'beginner'
        },
        {
            'title': 'Factorial Calculator',
            'description': 'Write a function that calculates the factorial of a number.',
            'solution': 'def factorial(n):\n    if n == 0:\n        return 1\n    return n * factorial(n-1)',
            'language': 'python',
            'difficulty': 'beginner'
        }
    ],
    'intermediate': [
        {
            'title': 'Palindrome Checker',
            'description': 'Write a function that checks if a string is a palindrome.',
            'solution': 'def is_palindrome(s):\n    return s == s[::-1]',
            'language': 'python',
            'difficulty': 'intermediate'
        },
        {
            'title': 'Prime Number Generator',
            'description': 'Write a function that generates a list of prime numbers up to a given number.',
            'solution': 'def generate_primes(n):\n    primes = []\n    for num in range(2, n+1):\n        if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):\n            primes.append(num)\n    return primes',
            'language': 'python',
            'difficulty': 'intermediate'
        }
    ],
    'advanced': [
        {
            'title': 'Binary Search Tree',
            'description': 'Implement a binary search tree with insert, search, and delete operations.',
            'solution': '''class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root''',
            'language': 'python',
            'difficulty': 'advanced'
        }
    ]
}

JAVASCRIPT_CHALLENGES = {
    'beginner': [
        {
            'title': 'Hello World',
            'description': 'Write a program that prints "Hello, World!" to the console.',
            'solution': 'console.log("Hello, World!");',
            'language': 'javascript',
            'difficulty': 'beginner'
        }
    ]
}

JAVA_CHALLENGES = {
    'beginner': [
        {
            'title': 'Hello World',
            'description': 'Write a program that prints "Hello, World!" to the console.',
            'solution': 'public class HelloWorld {\n    public static void main(String[] args) {\n        System.out.println("Hello, World!");\n    }\n}',
            'language': 'java',
            'difficulty': 'beginner'
        }
    ]
} 