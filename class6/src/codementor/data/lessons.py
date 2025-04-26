PYTHON_LESSONS = {
    'beginner': [
        {
            'title': 'Introduction to Python',
            'content': '''
            Python is a high-level, interpreted programming language known for its simplicity and readability.
            It was created by Guido van Rossum and first released in 1991.
            
            Key Features:
            - Easy to learn and use
            - Extensive standard library
            - Cross-platform compatibility
            - Strong community support
            
            Python is widely used in:
            - Web Development
            - Data Science
            - Machine Learning
            - Automation
            - And many more!
            
            Example:
            ```python
            print("Hello, World!")
            ```
            ''',
            'language': 'python',
            'difficulty': 'beginner'
        },
        {
            'title': 'Variables and Data Types',
            'content': '''
            In Python, variables are used to store data values. Unlike other languages, Python variables don't need explicit declaration.
            
            Basic Data Types:
            - Integers (int): 1, 2, 3
            - Floating-point numbers (float): 1.0, 2.5, 3.14
            - Strings (str): "Hello", 'World'
            - Booleans (bool): True, False
            
            Example:
            ```python
            x = 5          # integer
            y = 3.14       # float
            name = "John"  # string
            is_valid = True # boolean
            ```
            ''',
            'language': 'python',
            'difficulty': 'beginner'
        },
        {
            'title': 'Operators and Expressions',
            'content': '''
            Python supports various types of operators:
            
            Arithmetic Operators:
            - Addition (+)
            - Subtraction (-)
            - Multiplication (*)
            - Division (/)
            - Modulus (%)
            - Exponentiation (**)
            
            Comparison Operators:
            - Equal to (==)
            - Not equal to (!=)
            - Greater than (>)
            - Less than (<)
            
            Example:
            ```python
            a = 10
            b = 3
            print(a + b)   # 13
            print(a - b)   # 7
            print(a * b)   # 30
            print(a / b)   # 3.333...
            print(a % b)   # 1
            print(a ** b)  # 1000
            ```
            ''',
            'language': 'python',
            'difficulty': 'beginner'
        },
        {
            'title': 'Control Flow: if-else',
            'content': '''
            Control flow statements allow you to make decisions in your code.
            
            if-else Syntax:
            ```python
            if condition:
                # code to execute if condition is True
            elif another_condition:
                # code to execute if another_condition is True
            else:
                # code to execute if all conditions are False
            ```
            
            Example:
            ```python
            age = 18
            if age >= 18:
                print("You are an adult")
            else:
                print("You are a minor")
            ```
            ''',
            'language': 'python',
            'difficulty': 'beginner'
        },
        {
            'title': 'Loops: for and while',
            'content': '''
            Loops allow you to execute a block of code repeatedly.
            
            for loop:
            ```python
            for i in range(5):
                print(i)  # prints 0, 1, 2, 3, 4
            ```
            
            while loop:
            ```python
            count = 0
            while count < 5:
                print(count)
                count += 1
            ```
            
            Loop Control:
            - break: Exit the loop
            - continue: Skip to next iteration
            - else: Execute when loop completes normally
            ''',
            'language': 'python',
            'difficulty': 'beginner'
        }
    ],
    'intermediate': [
        {
            'title': 'Functions and Modules',
            'content': '''
            Functions are reusable blocks of code that perform a specific task.
            Modules are files containing Python code that can be imported and used in other programs.
            
            Function Definition:
            ```python
            def greet(name):
                return f"Hello, {name}!"
            
            print(greet("Alice"))  # Output: Hello, Alice!
            ```
            
            Module Usage:
            ```python
            import math
            print(math.sqrt(16))  # Output: 4.0
            ```
            
            Function Arguments:
            - Positional arguments
            - Keyword arguments
            - Default arguments
            - Variable-length arguments
            ''',
            'language': 'python',
            'difficulty': 'intermediate'
        },
        {
            'title': 'Lists and List Comprehensions',
            'content': '''
            Lists are ordered, mutable collections of items.
            
            Basic List Operations:
            ```python
            numbers = [1, 2, 3, 4, 5]
            numbers.append(6)      # Add item
            numbers.remove(3)      # Remove item
            numbers[0] = 10        # Modify item
            ```
            
            List Comprehensions:
            ```python
            squares = [x**2 for x in range(10)]
            even_numbers = [x for x in range(20) if x % 2 == 0]
            ```
            
            List Methods:
            - append()
            - extend()
            - insert()
            - remove()
            - pop()
            - sort()
            - reverse()
            ''',
            'language': 'python',
            'difficulty': 'intermediate'
        },
        {
            'title': 'Dictionaries and Sets',
            'content': '''
            Dictionaries store key-value pairs, while sets store unique elements.
            
            Dictionary Example:
            ```python
            person = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            print(person["name"])  # Output: John
            ```
            
            Set Example:
            ```python
            fruits = {"apple", "banana", "cherry"}
            fruits.add("orange")
            fruits.remove("banana")
            ```
            
            Dictionary Methods:
            - keys()
            - values()
            - items()
            - get()
            - update()
            ''',
            'language': 'python',
            'difficulty': 'intermediate'
        },
        {
            'title': 'File Handling',
            'content': '''
            Python provides built-in functions for file operations.
            
            Reading Files:
            ```python
            with open("file.txt", "r") as file:
                content = file.read()
            ```
            
            Writing Files:
            ```python
            with open("file.txt", "w") as file:
                file.write("Hello, World!")
            ```
            
            File Modes:
            - 'r': Read
            - 'w': Write
            - 'a': Append
            - 'b': Binary mode
            ''',
            'language': 'python',
            'difficulty': 'intermediate'
        },
        {
            'title': 'Error Handling',
            'content': '''
            Python uses try-except blocks for error handling.
            
            Basic Error Handling:
            ```python
            try:
                result = 10 / 0
            except ZeroDivisionError:
                print("Cannot divide by zero!")
            ```
            
            Multiple Exceptions:
            ```python
            try:
                # code that might raise exceptions
            except (TypeError, ValueError) as e:
                print(f"Error occurred: {e}")
            ```
            
            Finally Block:
            ```python
            try:
                # code
            except:
                # handle exception
            finally:
                # code that always executes
            ```
            ''',
            'language': 'python',
            'difficulty': 'intermediate'
        }
    ],
    'advanced': [
        {
            'title': 'Object-Oriented Programming',
            'content': '''
            Object-Oriented Programming (OOP) is a programming paradigm based on the concept of "objects".
            
            Key Concepts:
            - Classes and Objects
            - Inheritance
            - Encapsulation
            - Polymorphism
            
            Example:
            ```python
            class Animal:
                def __init__(self, name):
                    self.name = name
                
                def speak(self):
                    pass
            
            class Dog(Animal):
                def speak(self):
                    return "Woof!"
            
            dog = Dog("Buddy")
            print(dog.speak())  # Output: Woof!
            ```
            ''',
            'language': 'python',
            'difficulty': 'advanced'
        },
        {
            'title': 'Decorators',
            'content': '''
            Decorators are functions that modify the behavior of other functions.
            
            Basic Decorator:
            ```python
            def my_decorator(func):
                def wrapper():
                    print("Something is happening before the function is called.")
                    func()
                    print("Something is happening after the function is called.")
                return wrapper
            
            @my_decorator
            def say_hello():
                print("Hello!")
            ```
            
            Decorator with Arguments:
            ```python
            def repeat(num_times):
                def decorator_repeat(func):
                    def wrapper(*args, **kwargs):
                        for _ in range(num_times):
                            result = func(*args, **kwargs)
                        return result
                    return wrapper
                return decorator_repeat
            ```
            ''',
            'language': 'python',
            'difficulty': 'advanced'
        },
        {
            'title': 'Generators and Iterators',
            'content': '''
            Generators are functions that return an iterator.
            
            Generator Function:
            ```python
            def count_up_to(max):
                count = 1
                while count <= max:
                    yield count
                    count += 1
            
            counter = count_up_to(5)
            for num in counter:
                print(num)
            ```
            
            Generator Expression:
            ```python
            squares = (x**2 for x in range(10))
            ```
            
            Iterator Protocol:
            - __iter__()
            - __next__()
            ''',
            'language': 'python',
            'difficulty': 'advanced'
        },
        {
            'title': 'Context Managers',
            'content': '''
            Context managers help manage resources properly.
            
            Using with Statement:
            ```python
            with open('file.txt', 'r') as file:
                content = file.read()
            ```
            
            Custom Context Manager:
            ```python
            class MyContextManager:
                def __enter__(self):
                    print("Entering context")
                    return self
                
                def __exit__(self, exc_type, exc_val, exc_tb):
                    print("Exiting context")
            ```
            
            Using contextlib:
            ```python
            from contextlib import contextmanager
            
            @contextmanager
            def my_context():
                print("Entering")
                yield
                print("Exiting")
            ```
            ''',
            'language': 'python',
            'difficulty': 'advanced'
        },
        {
            'title': 'Metaclasses',
            'content': '''
            Metaclasses are classes that create other classes.
            
            Basic Metaclass:
            ```python
            class Meta(type):
                def __new__(cls, name, bases, dct):
                    print(f"Creating class {name}")
                    return super().__new__(cls, name, bases, dct)
            
            class MyClass(metaclass=Meta):
                pass
            ```
            
            Metaclass Use Cases:
            - Class registration
            - Attribute validation
            - Method wrapping
            - API creation
            ''',
            'language': 'python',
            'difficulty': 'advanced'
        }
    ]
}

JAVASCRIPT_LESSONS = {
    'beginner': [
        {
            'title': 'Introduction to JavaScript',
            'content': '''
JavaScript is a versatile, high-level programming language that enables interactive web pages and dynamic user experiences. It is one of the core technologies of the World Wide Web, alongside HTML and CSS.

**Key Features:**
- Runs in all modern web browsers
- Supports event-driven, functional, and object-oriented programming styles
- Used for both client-side and server-side development (Node.js)
- Large ecosystem and community

**What can you do with JavaScript?**
- Manipulate web page content and structure (DOM)
- Respond to user actions (clicks, keypresses, etc.)
- Communicate with servers (AJAX, fetch API)
- Create games, web apps, and more

**Example:**
```javascript
console.log("Hello, World!"); // Prints a message to the browser console
```
''',
            'language': 'javascript',
            'difficulty': 'beginner'
        },
        {
            'title': 'Variables and Data Types',
            'content': '''
Variables are containers for storing data values. In JavaScript, you can declare variables using `var`, `let`, or `const`.

**Variable Declarations:**
- `var`: Function-scoped, can be redeclared and updated (older, less recommended)
- `let`: Block-scoped, can be updated but not redeclared in the same scope
- `const`: Block-scoped, cannot be updated or redeclared (must be initialized)

**Data Types:**
- Number: `let age = 25;`
- String: `let name = "Alice";`
- Boolean: `let isActive = true;`
- Null: `let data = null;`
- Undefined: `let value;`
- Object: `let person = { name: "Bob", age: 30 };`
- Array: `let numbers = [1, 2, 3];`

**Example:**
```javascript
let city = "New York";
const pi = 3.14159;
var isStudent = false;
```
''',
            'language': 'javascript',
            'difficulty': 'beginner'
        },
        {
            'title': 'Operators and Expressions',
            'content': '''
Operators are used to perform operations on variables and values.

**Arithmetic Operators:**
- Addition: `+`
- Subtraction: `-`
- Multiplication: `*`
- Division: `/`
- Modulus (remainder): `%`
- Exponentiation: `**`

**Comparison Operators:**
- Equal to: `==` (loose), `===` (strict)
- Not equal to: `!=`, `!==`
- Greater than: `>`
- Less than: `<`
- Greater than or equal to: `>=`
- Less than or equal to: `<=`

**Logical Operators:**
- AND: `&&`
- OR: `||`
- NOT: `!`

**Example:**
```javascript
let a = 10, b = 3;
console.log(a + b);   // 13
console.log(a === b); // false
console.log(a > b && b > 0); // true
```
''',
            'language': 'javascript',
            'difficulty': 'beginner'
        },
        {
            'title': 'Control Flow',
            'content': '''
Control flow statements allow you to make decisions and repeat actions in your code.

**if-else Statement:**
```javascript
let age = 18;
if (age >= 18) {
    console.log("Adult");
} else {
    console.log("Minor");
}
```

**switch Statement:**
```javascript
let day = "Monday";
switch(day) {
    case "Monday":
        console.log("Start of week");
        break;
    case "Friday":
        console.log("End of week");
        break;
    default:
        console.log("Mid week");
}
```
''',
            'language': 'javascript',
            'difficulty': 'beginner'
        },
        {
            'title': 'Loops',
            'content': '''
Loops allow you to execute a block of code multiple times.

**for Loop:**
```javascript
for (let i = 0; i < 5; i++) {
    console.log(i); // 0, 1, 2, 3, 4
}
```

**while Loop:**
```javascript
let i = 0;
while (i < 5) {
    console.log(i);
    i++;
}
```

**for...of Loop (for arrays):**
```javascript
const arr = [1, 2, 3];
for (const item of arr) {
    console.log(item);
}
```

**Loop Control:**
- `break`: Exit the loop early
- `continue`: Skip to the next iteration
''',
            'language': 'javascript',
            'difficulty': 'beginner'
        }
    ],
    'intermediate': [
        {
            'title': 'Functions',
            'content': '''
            Functions are first-class citizens in JavaScript.
            
            Function Declaration:
            ```javascript
            function greet(name) {
                return `Hello, ${name}!`;
            }
            ```
            
            Arrow Functions:
            ```javascript
            const greet = (name) => `Hello, ${name}!`;
            ```
            
            Function Parameters:
            ```javascript
            function sum(...numbers) {
                return numbers.reduce((a, b) => a + b);
            }
            ```
            ''',
            'language': 'javascript',
            'difficulty': 'intermediate'
        },
        {
            'title': 'Objects and Classes',
            'content': '''
            JavaScript is a prototype-based language.
            
            Object Literal:
            ```javascript
            const person = {
                name: "John",
                age: 30,
                greet() {
                    console.log(`Hello, I'm ${this.name}`);
                }
            };
            ```
            
            Class Definition:
            ```javascript
            class Person {
                constructor(name, age) {
                    this.name = name;
                    this.age = age;
                }
                
                greet() {
                    console.log(`Hello, I'm ${this.name}`);
                }
            }
            ```
            ''',
            'language': 'javascript',
            'difficulty': 'intermediate'
        },
        {
            'title': 'Arrays and Array Methods',
            'content': '''
            Arrays are ordered collections of values.
            
            Array Methods:
            ```javascript
            const numbers = [1, 2, 3, 4, 5];
            
            // Map
            const doubled = numbers.map(x => x * 2);
            
            // Filter
            const evens = numbers.filter(x => x % 2 === 0);
            
            // Reduce
            const sum = numbers.reduce((a, b) => a + b);
            ```
            ''',
            'language': 'javascript',
            'difficulty': 'intermediate'
        },
        {
            'title': 'Asynchronous JavaScript',
            'content': '''
            JavaScript handles asynchronous operations using callbacks, promises, and async/await.
            
            Promises:
            ```javascript
            const promise = new Promise((resolve, reject) => {
                setTimeout(() => resolve("Done!"), 1000);
            });
            
            promise.then(result => console.log(result));
            ```
            
            Async/Await:
            ```javascript
            async function fetchData() {
                const response = await fetch('url');
                const data = await response.json();
                return data;
            }
            ```
            ''',
            'language': 'javascript',
            'difficulty': 'intermediate'
        },
        {
            'title': 'DOM Manipulation',
            'content': '''
            The Document Object Model (DOM) represents the structure of a web page.
            
            Selecting Elements:
            ```javascript
            const element = document.getElementById('id');
            const elements = document.querySelectorAll('.class');
            ```
            
            Modifying Elements:
            ```javascript
            element.textContent = 'New text';
            element.style.color = 'red';
            element.classList.add('new-class');
            ```
            ''',
            'language': 'javascript',
            'difficulty': 'intermediate'
        }
    ],
    'advanced': [
        {
            'title': 'Closures and Scope',
            'content': '''
            Closures are functions that remember their lexical scope.
            
            Example:
            ```javascript
            function createCounter() {
                let count = 0;
                return function() {
                    return ++count;
                };
            }
            
            const counter = createCounter();
            console.log(counter()); // 1
            console.log(counter()); // 2
            ```
            ''',
            'language': 'javascript',
            'difficulty': 'advanced'
        },
        {
            'title': 'Prototypes and Inheritance',
            'content': '''
            JavaScript uses prototypal inheritance.
            
            Prototype Chain:
            ```javascript
            function Animal(name) {
                this.name = name;
            }
            
            Animal.prototype.speak = function() {
                console.log(`${this.name} makes a sound.`);
            };
            
            function Dog(name) {
                Animal.call(this, name);
            }
            
            Dog.prototype = Object.create(Animal.prototype);
            ```
            ''',
            'language': 'javascript',
            'difficulty': 'advanced'
        },
        {
            'title': 'Modules and Bundlers',
            'content': '''
            JavaScript modules help organize code.
            
            ES6 Modules:
            ```javascript
            // math.js
            export function add(a, b) {
                return a + b;
            }
            
            // main.js
            import { add } from './math.js';
            ```
            
            CommonJS:
            ```javascript
            // math.js
            module.exports = {
                add: function(a, b) {
                    return a + b;
                }
            };
            
            // main.js
            const math = require('./math.js');
            ```
            ''',
            'language': 'javascript',
            'difficulty': 'advanced'
        },
        {
            'title': 'Design Patterns',
            'content': '''
            Common JavaScript design patterns.
            
            Singleton:
            ```javascript
            const Singleton = (function() {
                let instance;
                
                function createInstance() {
                    return {
                        // singleton properties and methods
                    };
                }
                
                return {
                    getInstance: function() {
                        if (!instance) {
                            instance = createInstance();
                        }
                        return instance;
                    }
                };
            })();
            ```
            ''',
            'language': 'javascript',
            'difficulty': 'advanced'
        },
        {
            'title': 'Performance Optimization',
            'content': '''
            Techniques for optimizing JavaScript performance.
            
            Debouncing:
            ```javascript
            function debounce(func, wait) {
                let timeout;
                return function executedFunction(...args) {
                    const later = () => {
                        clearTimeout(timeout);
                        func(...args);
                    };
                    clearTimeout(timeout);
                    timeout = setTimeout(later, wait);
                };
            }
            ```
            
            Memoization:
            ```javascript
            function memoize(fn) {
                const cache = {};
                return function(...args) {
                    const key = JSON.stringify(args);
                    if (cache[key]) {
                        return cache[key];
                    }
                    const result = fn.apply(this, args);
                    cache[key] = result;
                    return result;
                };
            }
            ```
            ''',
            'language': 'javascript',
            'difficulty': 'advanced'
        }
    ]
}

JAVA_LESSONS = {
    'beginner': [
        {
            'title': 'Introduction to Java',
            'content': '''
            Java is a class-based, object-oriented programming language.
            It is designed to be platform-independent and secure.
            
            Key Features:
            - Write Once, Run Anywhere (WORA)
            - Strong type checking
            - Automatic memory management
            - Rich standard library
            
            Example:
            ```java
            public class HelloWorld {
                public static void main(String[] args) {
                    System.out.println("Hello, World!");
                }
            }
            ```
            ''',
            'language': 'java',
            'difficulty': 'beginner'
        },
        {
            'title': 'Variables and Data Types',
            'content': '''
            Java is a statically-typed language.
            
            Primitive Types:
            - byte
            - short
            - int
            - long
            - float
            - double
            - char
            - boolean
            
            Example:
            ```java
            int age = 25;
            double price = 19.99;
            char grade = 'A';
            boolean isStudent = true;
            ```
            ''',
            'language': 'java',
            'difficulty': 'beginner'
        },
        {
            'title': 'Operators and Expressions',
            'content': '''
            Java supports various operators.
            
            Arithmetic Operators:
            ```java
            int x = 10;
            int y = 5;
            System.out.println(x + y);  // 15
            System.out.println(x - y);  // 5
            System.out.println(x * y);  // 50
            System.out.println(x / y);  // 2
            ```
            
            Comparison Operators:
            ```java
            System.out.println(10 > 5);   // true
            System.out.println(10 == 10); // true
            ```
            ''',
            'language': 'java',
            'difficulty': 'beginner'
        },
        {
            'title': 'Control Flow',
            'content': '''
            Java provides several control flow statements.
            
            if-else:
            ```java
            if (age >= 18) {
                System.out.println("Adult");
            } else {
                System.out.println("Minor");
            }
            ```
            
            switch:
            ```java
            switch(day) {
                case "Monday":
                    System.out.println("Start of week");
                    break;
                case "Friday":
                    System.out.println("End of week");
                    break;
                default:
                    System.out.println("Mid week");
            }
            ```
            ''',
            'language': 'java',
            'difficulty': 'beginner'
        },
        {
            'title': 'Loops',
            'content': '''
            Java provides several types of loops.
            
            for loop:
            ```java
            for (int i = 0; i < 5; i++) {
                System.out.println(i);
            }
            ```
            
            while loop:
            ```java
            int i = 0;
            while (i < 5) {
                System.out.println(i);
                i++;
            }
            ```
            
            for-each loop:
            ```java
            int[] numbers = {1, 2, 3};
            for (int number : numbers) {
                System.out.println(number);
            }
            ```
            ''',
            'language': 'java',
            'difficulty': 'beginner'
        }
    ],
    'intermediate': [
        {
            'title': 'Classes and Objects',
            'content': '''
            Java is an object-oriented language.
            
            Class Definition:
            ```java
            public class Person {
                private String name;
                private int age;
                
                public Person(String name, int age) {
                    this.name = name;
                    this.age = age;
                }
                
                public void greet() {
                    System.out.println("Hello, I'm " + name);
                }
            }
            ```
            ''',
            'language': 'java',
            'difficulty': 'intermediate'
        },
        {
            'title': 'Inheritance and Polymorphism',
            'content': '''
            Java supports inheritance and polymorphism.
            
            Inheritance:
            ```java
            class Animal {
                public void makeSound() {
                    System.out.println("Some sound");
                }
            }
            
            class Dog extends Animal {
                @Override
                public void makeSound() {
                    System.out.println("Woof!");
                }
            }
            ```
            ''',
            'language': 'java',
            'difficulty': 'intermediate'
        },
        {
            'title': 'Interfaces and Abstract Classes',
            'content': '''
            Interfaces and abstract classes provide abstraction.
            
            Interface:
            ```java
            interface Drawable {
                void draw();
            }
            
            class Circle implements Drawable {
                public void draw() {
                    System.out.println("Drawing circle");
                }
            }
            ```
            
            Abstract Class:
            ```java
            abstract class Shape {
                abstract void draw();
                
                void move() {
                    System.out.println("Moving shape");
                }
            }
            ```
            ''',
            'language': 'java',
            'difficulty': 'intermediate'
        },
        {
            'title': 'Exception Handling',
            'content': '''
            Java uses try-catch blocks for exception handling.
            
            Basic Exception Handling:
            ```java
            try {
                int result = 10 / 0;
            } catch (ArithmeticException e) {
                System.out.println("Cannot divide by zero!");
            }
            ```
            
            Multiple Exceptions:
            ```java
            try {
                // code that might throw exceptions
            } catch (IOException | SQLException e) {
                System.out.println("Error occurred: " + e.getMessage());
            }
            ```
            ''',
            'language': 'java',
            'difficulty': 'intermediate'
        },
        {
            'title': 'Collections Framework',
            'content': '''
            Java provides a rich collections framework.
            
            List:
            ```java
            List<String> names = new ArrayList<>();
            names.add("John");
            names.add("Alice");
            ```
            
            Map:
            ```java
            Map<String, Integer> ages = new HashMap<>();
            ages.put("John", 25);
            ages.put("Alice", 30);
            ```
            
            Set:
            ```java
            Set<String> uniqueNames = new HashSet<>();
            uniqueNames.add("John");
            uniqueNames.add("Alice");
            ```
            ''',
            'language': 'java',
            'difficulty': 'intermediate'
        }
    ],
    'advanced': [
        {
            'title': 'Generics',
            'content': '''
            Generics provide type safety and code reuse.
            
            Generic Class:
            ```java
            class Box<T> {
                private T content;
                
                public void setContent(T content) {
                    this.content = content;
                }
                
                public T getContent() {
                    return content;
                }
            }
            ```
            
            Generic Methods:
            ```java
            public <T> void printArray(T[] array) {
                for (T element : array) {
                    System.out.println(element);
                }
            }
            ```
            ''',
            'language': 'java',
            'difficulty': 'advanced'
        },
        {
            'title': 'Multithreading',
            'content': '''
            Java supports concurrent programming through threads.
            
            Thread Creation:
            ```java
            class MyThread extends Thread {
                public void run() {
                    System.out.println("Thread running");
                }
            }
            
            // Using Runnable
            Thread thread = new Thread(() -> {
                System.out.println("Thread running");
            });
            ```
            
            Synchronization:
            ```java
            synchronized void increment() {
                count++;
            }
            ```
            ''',
            'language': 'java',
            'difficulty': 'advanced'
        },
        {
            'title': 'Streams and Lambda Expressions',
            'content': '''
            Java 8 introduced functional programming features.
            
            Stream Operations:
            ```java
            List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5);
            
            // Filter
            List<Integer> evens = numbers.stream()
                .filter(n -> n % 2 == 0)
                .collect(Collectors.toList());
            
            // Map
            List<Integer> squares = numbers.stream()
                .map(n -> n * n)
                .collect(Collectors.toList());
            ```
            ''',
            'language': 'java',
            'difficulty': 'advanced'
        },
        {
            'title': 'Reflection',
            'content': '''
            Reflection allows runtime inspection of classes.
            
            Example:
            ```java
            Class<?> clazz = MyClass.class;
            
            // Get methods
            Method[] methods = clazz.getDeclaredMethods();
            
            // Get fields
            Field[] fields = clazz.getDeclaredFields();
            
            // Create instance
            Object instance = clazz.newInstance();
            ```
            ''',
            'language': 'java',
            'difficulty': 'advanced'
        },
        {
            'title': 'Design Patterns',
            'content': '''
            Common Java design patterns.
            
            Singleton:
            ```java
            public class Singleton {
                private static Singleton instance;
                
                private Singleton() {}
                
                public static Singleton getInstance() {
                    if (instance == null) {
                        instance = new Singleton();
                    }
                    return instance;
                }
            }
            ```
            
            Factory:
            ```java
            interface Shape {
                void draw();
            }
            
            class ShapeFactory {
                public Shape getShape(String type) {
                    if (type.equals("circle")) {
                        return new Circle();
                    }
                    return new Rectangle();
                }
            }
            ```
            ''',
            'language': 'java',
            'difficulty': 'advanced'
        }
    ]
}

TYPESCRIPT_LESSONS = {
    'beginner': [
        {
            'title': 'Introduction to TypeScript',
            'content': '''
TypeScript is a superset of JavaScript that adds static typing and other features to the language.

Key Features:
- Optional static typing
- Interfaces and type aliases
- Enums
- Generics
- Compiles to JavaScript

Example:
```typescript
let message: string = "Hello, TypeScript!";
console.log(message);
```
''',
            'language': 'typescript',
            'difficulty': 'beginner'
        },
        {
            'title': 'Basic Types',
            'content': '''
TypeScript provides several basic types:

- number
- string
- boolean
- any
- void
- null and undefined

Example:
```typescript
let age: number = 30;
let name: string = "Alice";
let isActive: boolean = true;
```
''',
            'language': 'typescript',
            'difficulty': 'beginner'
        },
        {
            'title': 'Arrays and Tuples',
            'content': '''
Arrays and tuples allow you to store multiple values.

Example:
```typescript
let numbers: number[] = [1, 2, 3];
let person: [string, number] = ["Alice", 30];
```
''',
            'language': 'typescript',
            'difficulty': 'beginner'
        },
        {
            'title': 'Enums',
            'content': '''
Enums allow you to define a set of named constants.

Example:
```typescript
enum Color { Red, Green, Blue }
let c: Color = Color.Green;
```
''',
            'language': 'typescript',
            'difficulty': 'beginner'
        },
        {
            'title': 'Type Annotations',
            'content': '''
Type annotations allow you to specify the type of a variable, function parameter, or return value.

Example:
```typescript
function greet(name: string): string {
    return "Hello, " + name;
}
```
''',
            'language': 'typescript',
            'difficulty': 'beginner'
        },
        {
            'title': 'Union and Literal Types',
            'content': '''
Union types allow a variable to be one of several types.

Example:
```typescript
let id: number | string;
id = 10;
id = "A123";
```
''',
            'language': 'typescript',
            'difficulty': 'beginner'
        },
        {
            'title': 'Type Assertions',
            'content': '''
Type assertions tell the compiler to treat a value as a specific type.

Example:
```typescript
let someValue: any = "this is a string";
let strLength: number = (someValue as string).length;
```
''',
            'language': 'typescript',
            'difficulty': 'beginner'
        },
        {
            'title': 'Functions',
            'content': '''
Functions can have typed parameters and return types.

Example:
```typescript
function add(a: number, b: number): number {
    return a + b;
}
```
''',
            'language': 'typescript',
            'difficulty': 'beginner'
        },
        {
            'title': 'Any and Unknown Types',
            'content': '''
The `any` type disables type checking, while `unknown` is a safer alternative.

Example:
```typescript
let data: any = 5;
let value: unknown = "hello";
```
''',
            'language': 'typescript',
            'difficulty': 'beginner'
        },
        {
            'title': 'Void, Null, and Undefined',
            'content': '''
`void` is used for functions that do not return a value. `null` and `undefined` are their own types.

Example:
```typescript
function log(message: string): void {
    console.log(message);
}
let n: null = null;
let u: undefined = undefined;
```
''',
            'language': 'typescript',
            'difficulty': 'beginner'
        }
    ],
    'intermediate': [
        {
            'title': 'Interfaces',
            'content': '''
Interfaces define the shape of an object.

Example:
```typescript
interface User {
    name: string;
    age: number;
}
let user: User = { name: "Alice", age: 25 };
```
''',
            'language': 'typescript',
            'difficulty': 'intermediate'
        },
        {
            'title': 'Type Aliases',
            'content': '''
Type aliases create a new name for a type.

Example:
```typescript
type Point = { x: number; y: number; };
let p: Point = { x: 10, y: 20 };
```
''',
            'language': 'typescript',
            'difficulty': 'intermediate'
        },
        {
            'title': 'Optional and Readonly Properties',
            'content': '''
Properties can be optional or readonly.

Example:
```typescript
interface Car {
    readonly id: number;
    model: string;
    color?: string;
}
```
''',
            'language': 'typescript',
            'difficulty': 'intermediate'
        },
        {
            'title': 'Function Types and Call Signatures',
            'content': '''
You can define types for functions.

Example:
```typescript
type Add = (a: number, b: number) => number;
const add: Add = (x, y) => x + y;
```
''',
            'language': 'typescript',
            'difficulty': 'intermediate'
        },
        {
            'title': 'Generics',
            'content': '''
Generics allow you to write flexible, reusable functions and types.

Example:
```typescript
function identity<T>(arg: T): T {
    return arg;
}
```
''',
            'language': 'typescript',
            'difficulty': 'intermediate'
        },
        {
            'title': 'Intersection Types',
            'content': '''
Intersection types combine multiple types into one.

Example:
```typescript
type A = { a: number };
type B = { b: string };
type C = A & B;
let obj: C = { a: 1, b: "hi" };
```
''',
            'language': 'typescript',
            'difficulty': 'intermediate'
        },
        {
            'title': 'Literal Types',
            'content': '''
Literal types allow variables to have exact values.

Example:
```typescript
let direction: "left" | "right";
direction = "left";
```
''',
            'language': 'typescript',
            'difficulty': 'intermediate'
        },
        {
            'title': 'Enums (Advanced)',
            'content': '''
Enums can have custom values and be used in switch statements.

Example:
```typescript
enum Status { Success = 1, Error = -1 }
let s: Status = Status.Success;
```
''',
            'language': 'typescript',
            'difficulty': 'intermediate'
        },
        {
            'title': 'Type Guards',
            'content': '''
Type guards help narrow down the type of a variable.

Example:
```typescript
function isString(x: any): x is string {
    return typeof x === "string";
}
```
''',
            'language': 'typescript',
            'difficulty': 'intermediate'
        },
        {
            'title': 'Keyof and Index Types',
            'content': '''
`keyof` gets the keys of a type, and index types allow dynamic property access.

Example:
```typescript
type Person = { name: string; age: number; };
type PersonKeys = keyof Person; // "name" | "age"
function getValue<T, K extends keyof T>(obj: T, key: K): T[K] {
    return obj[key];
}
```
''',
            'language': 'typescript',
            'difficulty': 'intermediate'
        }
    ],
    'advanced': [
        {
            'title': 'Mapped Types',
            'content': '''
Mapped types create new types by transforming properties.

Example:
```typescript
type Readonly<T> = { readonly [P in keyof T]: T[P] };
type User = { name: string; age: number; };
type ReadonlyUser = Readonly<User>;
```
''',
            'language': 'typescript',
            'difficulty': 'advanced'
        },
        {
            'title': 'Conditional Types',
            'content': '''
Conditional types choose one type or another based on a condition.

Example:
```typescript
type IsString<T> = T extends string ? true : false;
```
''',
            'language': 'typescript',
            'difficulty': 'advanced'
        },
        {
            'title': 'Infer Keyword',
            'content': '''
The `infer` keyword lets you infer a type within a conditional type.

Example:
```typescript
type ReturnType<T> = T extends (...args: any[]) => infer R ? R : any;
```
''',
            'language': 'typescript',
            'difficulty': 'advanced'
        },
        {
            'title': 'Discriminated Unions',
            'content': '''
Discriminated unions use a common property to distinguish types.

Example:
```typescript
type Circle = { kind: "circle"; radius: number; };
type Square = { kind: "square"; side: number; };
type Shape = Circle | Square;
```
''',
            'language': 'typescript',
            'difficulty': 'advanced'
        },
        {
            'title': 'Utility Types',
            'content': '''
TypeScript provides built-in utility types like Partial, Required, and Readonly.

Example:
```typescript
interface User { name: string; age: number; }
type PartialUser = Partial<User>;
```
''',
            'language': 'typescript',
            'difficulty': 'advanced'
        },
        {
            'title': 'Index Signatures',
            'content': '''
Index signatures allow you to define types for properties with dynamic keys.

Example:
```typescript
interface Dictionary { [key: string]: number; }
let dict: Dictionary = { apples: 5, oranges: 10 };
```
''',
            'language': 'typescript',
            'difficulty': 'advanced'
        },
        {
            'title': 'Never Type',
            'content': '''
The `never` type represents values that never occur.

Example:
```typescript
function fail(message: string): never {
    throw new Error(message);
}
```
''',
            'language': 'typescript',
            'difficulty': 'advanced'
        },
        {
            'title': 'Recursive Types',
            'content': '''
Recursive types reference themselves.

Example:
```typescript
type NestedArray = number | NestedArray[];
```
''',
            'language': 'typescript',
            'difficulty': 'advanced'
        },
        {
            'title': 'Advanced Generics',
            'content': '''
Generics can have constraints and default types.

Example:
```typescript
function merge<T extends object, U extends object>(a: T, b: U): T & U {
    return { ...a, ...b };
}
```
''',
            'language': 'typescript',
            'difficulty': 'advanced'
        },
        {
            'title': 'Declaration Merging',
            'content': '''
Declaration merging allows you to merge multiple declarations.

Example:
```typescript
interface Box { height: number; }
interface Box { width: number; }
let box: Box = { height: 10, width: 20 };
```
''',
            'language': 'typescript',
            'difficulty': 'advanced'
        }
    ]
} 