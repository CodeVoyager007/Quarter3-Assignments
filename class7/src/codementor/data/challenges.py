PYTHON_CHALLENGES = {
    'beginner': [
        {
            'title': 'Hello World',
            'description': 'Write a program that prints "Hello, World!" to the console.',
            'solution': 'print("Hello, World!")',
            'hint': 'Use the print function.',
            'language': 'python',
            'difficulty': 'beginner'
        },
        {
            'title': 'Sum of Two Numbers',
            'description': 'Write a function that takes two numbers as input and returns their sum.',
            'solution': 'def add(a, b):\n    return a + b',
            'hint': 'Define a function and use the + operator.',
            'language': 'python',
            'difficulty': 'beginner'
        },
        {
            'title': 'Factorial Calculator',
            'description': 'Write a function that calculates the factorial of a number.',
            'solution': 'def factorial(n):\n    if n == 0:\n        return 1\n    return n * factorial(n-1)',
            'hint': 'Use recursion or a loop. Remember factorial(0) is 1.',
            'language': 'python',
            'difficulty': 'beginner'
        },
        {
            'title': 'Even or Odd',
            'description': 'Write a function that checks if a number is even or odd.',
            'solution': 'def even_or_odd(n):\n    return "Even" if n % 2 == 0 else "Odd"',
            'hint': 'Use the modulus operator (%) to check divisibility by 2.',
            'language': 'python',
            'difficulty': 'beginner'
        },
        {
            'title': 'Find Maximum',
            'description': 'Write a function that returns the maximum of three numbers.',
            'solution': 'def find_max(a, b, c):\n    return max(a, b, c)',
            'hint': 'Use the built-in max() function.',
            'language': 'python',
            'difficulty': 'beginner'
        },
        {
            'title': 'Reverse String',
            'description': 'Write a function that reverses a string.',
            'solution': 'def reverse_string(s):\n    return s[::-1]',
            'hint': 'Use Python slicing to reverse the string.',
            'language': 'python',
            'difficulty': 'beginner'
        },
        {
            'title': 'Count Vowels',
            'description': 'Write a function that counts the number of vowels in a string.',
            'solution': 'def count_vowels(s):\n    return sum(1 for c in s.lower() if c in "aeiou")',
            'hint': 'Iterate through the string and check if each character is a vowel.',
            'language': 'python',
            'difficulty': 'beginner'
        },
        {
            'title': 'List Sum',
            'description': 'Write a function that returns the sum of all elements in a list.',
            'solution': 'def list_sum(lst):\n    return sum(lst)',
            'hint': 'Use the built-in sum() function.',
            'language': 'python',
            'difficulty': 'beginner'
        },
        {
            'title': 'Fibonacci Sequence',
            'description': 'Write a function that returns the first n numbers of the Fibonacci sequence.',
            'solution': 'def fibonacci(n):\n    seq = [0, 1]\n    for i in range(2, n):\n        seq.append(seq[-1] + seq[-2])\n    return seq[:n]',
            'hint': 'Start with [0, 1] and add the last two numbers to get the next.',
            'language': 'python',
            'difficulty': 'beginner'
        },
        {
            'title': 'Square Numbers',
            'description': 'Write a function that returns a list of squares of numbers from 1 to n.',
            'solution': 'def squares(n):\n    return [i*i for i in range(1, n+1)]',
            'hint': 'Use a list comprehension and the ** operator.',
            'language': 'python',
            'difficulty': 'beginner'
        }
    ],
    'intermediate': [
        {
            'title': 'Palindrome Checker',
            'description': 'Write a function that checks if a string is a palindrome.',
            'solution': 'def is_palindrome(s):\n    return s == s[::-1]',
            'hint': 'A palindrome reads the same forwards and backwards.',
            'language': 'python',
            'difficulty': 'intermediate'
        },
        {
            'title': 'Prime Number Generator',
            'description': 'Write a function that generates a list of prime numbers up to a given number.',
            'solution': 'def generate_primes(n):\n    primes = []\n    for num in range(2, n+1):\n        if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):\n            primes.append(num)\n    return primes',
            'hint': 'A prime number is only divisible by 1 and itself.',
            'language': 'python',
            'difficulty': 'intermediate'
        },
        {
            'title': 'Anagram Checker',
            'description': 'Write a function that checks if two strings are anagrams.',
            'solution': 'def are_anagrams(s1, s2):\n    return sorted(s1.lower()) == sorted(s2.lower())',
            'hint': 'Sort both strings and compare them.',
            'language': 'python',
            'difficulty': 'intermediate'
        },
        {
            'title': 'Matrix Transpose',
            'description': 'Write a function that transposes a 2D matrix.',
            'solution': 'def transpose(matrix):\n    return [list(row) for row in zip(*matrix)]',
            'hint': 'Use zip and unpack the matrix with *.',
            'language': 'python',
            'difficulty': 'intermediate'
        },
        {
            'title': 'Find Duplicates',
            'description': 'Write a function that finds duplicate elements in a list.',
            'solution': 'def find_duplicates(lst):\n    return list(set([x for x in lst if lst.count(x) > 1]))',
            'hint': 'Check if count of an element is more than 1.',
            'language': 'python',
            'difficulty': 'intermediate'
        },
        {
            'title': 'GCD Calculator',
            'description': 'Write a function that calculates the greatest common divisor (GCD) of two numbers.',
            'solution': 'def gcd(a, b):\n    while b:\n        a, b = b, a % b\n    return a',
            'hint': 'Use the Euclidean algorithm.',
            'language': 'python',
            'difficulty': 'intermediate'
        },
        {
            'title': 'Caesar Cipher',
            'description': 'Write a function that encrypts a string using Caesar cipher with a given shift.',
            'solution': 'def caesar_cipher(s, shift):\n    result = ""\n    for char in s:\n        if char.isalpha():\n            start = ord("A") if char.isupper() else ord("a")\n            result += chr((ord(char) - start + shift) % 26 + start)\n        else:\n            result += char\n    return result',
            'hint': 'Shift each letter by the given amount.',
            'language': 'python',
            'difficulty': 'intermediate'
        },
        {
            'title': 'Flatten List',
            'description': 'Write a function that flattens a nested list.',
            'solution': 'def flatten(lst):\n    return [item for sublist in lst for item in sublist]',
            'hint': 'Use a nested list comprehension.',
            'language': 'python',
            'difficulty': 'intermediate'
        },
        {
            'title': 'Unique Elements',
            'description': 'Write a function that returns unique elements from a list.',
            'solution': 'def unique_elements(lst):\n    return list(set(lst))',
            'hint': 'Convert the list to a set and back.',
            'language': 'python',
            'difficulty': 'intermediate'
        },
        {
            'title': 'Second Largest',
            'description': 'Write a function that returns the second largest number in a list.',
            'solution': 'def second_largest(lst):\n    return sorted(set(lst))[-2]',
            'hint': 'Sort the set of numbers and pick the second last.',
            'language': 'python',
            'difficulty': 'intermediate'
        },
        {
            'title': 'Merge Dictionaries',
            'description': 'Write a function that merges two dictionaries.',
            'solution': 'def merge_dicts(d1, d2):\n    return {**d1, **d2}',
            'hint': 'Use the ** unpacking operator.',
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
            'hint': 'Use recursion for insert/search. Compare keys to decide left/right.',
            'language': 'python',
            'difficulty': 'advanced'
        },
        {
            'title': 'LRU Cache',
            'description': 'Implement a Least Recently Used (LRU) cache.',
            'solution': '''from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity
    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]
    def put(self, key, value):
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)''',
            'hint': 'Use OrderedDict to keep track of usage order.',
            'language': 'python',
            'difficulty': 'advanced'
        },
        {
            'title': 'Dijkstra Algorithm',
            'description': 'Implement Dijkstra\'s algorithm for shortest path in a graph.',
            'solution': '''import heapq
def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    pq = [(0, start)]
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return distances''',
            'hint': 'Use a priority queue (heapq) to always expand the closest node.',
            'language': 'python',
            'difficulty': 'advanced'
        },
        {
            'title': 'Decorator Function',
            'description': 'Write a decorator that logs the execution time of a function.',
            'solution': '''import time
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start}")
        return result
    return wrapper''',
            'hint': 'Use time.time() before and after the function call.',
            'language': 'python',
            'difficulty': 'advanced'
        },
        {
            'title': 'Threaded Counter',
            'description': 'Create a counter that increments in multiple threads safely.',
            'solution': '''import threading
class Counter:
    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()
    def increment(self):
        with self.lock:
            self.value += 1''',
            'hint': 'Use threading.Lock to prevent race conditions.',
            'language': 'python',
            'difficulty': 'advanced'
        },
        {
            'title': 'Metaclass Example',
            'description': 'Create a metaclass that prints the name of any class it creates.',
            'solution': '''class PrintNameMeta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class {name}")
        return super().__new__(cls, name, bases, dct)''',
            'hint': 'Override __new__ in the metaclass.',
            'language': 'python',
            'difficulty': 'advanced'
        },
        {
            'title': 'Async HTTP Request',
            'description': 'Write an async function to fetch data from a URL using aiohttp.',
            'solution': '''import aiohttp
import asyncio
async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()''',
            'hint': 'Use async/await and aiohttp.ClientSession.',
            'language': 'python',
            'difficulty': 'advanced'
        },
        {
            'title': 'Custom Context Manager',
            'description': 'Create a custom context manager using a class.',
            'solution': '''class MyContext:
    def __enter__(self):
        print("Entering context")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting context")''',
            'hint': 'Implement __enter__ and __exit__ methods.',
            'language': 'python',
            'difficulty': 'advanced'
        },
        {
            'title': 'JSON Validator',
            'description': 'Write a function that validates if a string is a valid JSON.',
            'solution': '''import json
def is_json(myjson):
    try:
        json.loads(myjson)
        return True
    except ValueError:
        return False''',
            'hint': 'Use json.loads() inside a try/except block.',
            'language': 'python',
            'difficulty': 'advanced'
        },
        {
            'title': 'Singleton Pattern',
            'description': 'Implement the Singleton design pattern in Python.',
            'solution': '''class Singleton:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance''',
            'hint': 'Override __new__ to ensure only one instance.',
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
            'hint': 'Use console.log().',
            'language': 'javascript',
            'difficulty': 'beginner'
        },
        {
            'title': 'Sum of Two Numbers',
            'description': 'Write a function that returns the sum of two numbers.',
            'solution': 'function add(a, b) { return a + b; }',
            'hint': 'Use the + operator inside a function.',
            'language': 'javascript',
            'difficulty': 'beginner'
        },
        {
            'title': 'Even or Odd',
            'description': 'Write a function that checks if a number is even or odd.',
            'solution': 'function evenOrOdd(n) { return n % 2 === 0 ? "Even" : "Odd"; }',
            'hint': 'Use the modulus operator (%) and a ternary.',
            'language': 'javascript',
            'difficulty': 'beginner'
        },
        {
            'title': 'Find Maximum',
            'description': 'Write a function that returns the maximum of three numbers.',
            'solution': 'function findMax(a, b, c) { return Math.max(a, b, c); }',
            'hint': 'Use Math.max().',
            'language': 'javascript',
            'difficulty': 'beginner'
        },
        {
            'title': 'Reverse String',
            'description': 'Write a function that reverses a string.',
            'solution': 'function reverseString(s) { return s.split("").reverse().join(""); }',
            'hint': 'Use split, reverse, and join.',
            'language': 'javascript',
            'difficulty': 'beginner'
        },
        {
            'title': 'Count Vowels',
            'description': 'Write a function that counts the number of vowels in a string.',
            'solution': 'function countVowels(s) { return (s.match(/[aeiou]/gi) || []).length; }',
            'hint': 'Use a regular expression with match().',
            'language': 'javascript',
            'difficulty': 'beginner'
        },
        {
            'title': 'Array Sum',
            'description': 'Write a function that returns the sum of all elements in an array.',
            'solution': 'function arraySum(arr) { return arr.reduce((a, b) => a + b, 0); }',
            'hint': 'Use reduce().',
            'language': 'javascript',
            'difficulty': 'beginner'
        },
        {
            'title': 'Fibonacci Sequence',
            'description': 'Write a function that returns the first n numbers of the Fibonacci sequence.',
            'solution': 'function fibonacci(n) { let seq = [0, 1]; for(let i=2;i<n;i++){ seq.push(seq[i-1]+seq[i-2]); } return seq.slice(0, n); }',
            'hint': 'Start with [0,1] and add the last two numbers.',
            'language': 'javascript',
            'difficulty': 'beginner'
        },
        {
            'title': 'Square Numbers',
            'description': 'Write a function that returns an array of squares from 1 to n.',
            'solution': 'function squares(n) { let arr = []; for(let i=1;i<=n;i++){ arr.push(i*i); } return arr; }',
            'hint': 'Use a for loop and push i*i.',
            'language': 'javascript',
            'difficulty': 'beginner'
        },
        {
            'title': 'Capitalize Words',
            'description': 'Write a function that capitalizes the first letter of each word in a sentence.',
            'solution': 'function capitalizeWords(str) { return str.split(" ").map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(" "); }',
            'hint': 'Use split, map, and join.',
            'language': 'javascript',
            'difficulty': 'beginner'
        }
    ],
    'intermediate': [
        {
            'title': 'Palindrome Checker',
            'description': 'Write a function that checks if a string is a palindrome.',
            'solution': 'function isPalindrome(s) { s = s.toLowerCase(); return s === s.split("").reverse().join(""); }',
            'hint': 'Compare the string to its reverse.',
            'language': 'javascript',
            'difficulty': 'intermediate'
        },
        {
            'title': 'Prime Number Generator',
            'description': 'Write a function that generates an array of prime numbers up to n.',
            'solution': 'function generatePrimes(n) { let primes = []; for(let i=2;i<=n;i++){ if(primes.every(p=>i%p!==0)) primes.push(i); } return primes; }',
            'hint': 'Check divisibility for each number.',
            'language': 'javascript',
            'difficulty': 'intermediate'
        },
        {
            'title': 'Anagram Checker',
            'description': 'Write a function that checks if two strings are anagrams.',
            'solution': 'function areAnagrams(a, b) { return a.split("").sort().join("") === b.split("").sort().join(""); }',
            'hint': 'Sort both strings and compare.',
            'language': 'javascript',
            'difficulty': 'intermediate'
        },
        {
            'title': 'Matrix Transpose',
            'description': 'Write a function that transposes a 2D array (matrix).',
            'solution': 'function transpose(matrix) { return matrix[0].map((_,i)=>matrix.map(row=>row[i])); }',
            'hint': 'Use map and index swapping.',
            'language': 'javascript',
            'difficulty': 'intermediate'
        },
        {
            'title': 'Find Duplicates',
            'description': 'Write a function that finds duplicate elements in an array.',
            'solution': 'function findDuplicates(arr) { return arr.filter((v,i,a)=>a.indexOf(v)!==i).filter((v,i,a)=>a.indexOf(v)===i); }',
            'hint': 'Use filter and indexOf.',
            'language': 'javascript',
            'difficulty': 'intermediate'
        },
        {
            'title': 'GCD Calculator',
            'description': 'Write a function that calculates the greatest common divisor (GCD) of two numbers.',
            'solution': 'function gcd(a, b) { while(b){ [a, b] = [b, a % b]; } return a; }',
            'hint': 'Use the Euclidean algorithm.',
            'language': 'javascript',
            'difficulty': 'intermediate'
        },
        {
            'title': 'Caesar Cipher',
            'description': 'Write a function that encrypts a string using Caesar cipher with a given shift.',
            'solution': 'function caesarCipher(s, shift) { return s.replace(/[a-z]/gi, c => String.fromCharCode((c.charCodeAt(0) - (c<="Z"?65:97) + shift) % 26 + (c<="Z"?65:97))); }',
            'hint': 'Use charCodeAt and fromCharCode.',
            'language': 'javascript',
            'difficulty': 'intermediate'
        },
        {
            'title': 'Flatten Array',
            'description': 'Write a function that flattens a nested array (one level deep).',
            'solution': 'function flatten(arr) { return [].concat(...arr); }',
            'hint': 'Use concat and spread operator.',
            'language': 'javascript',
            'difficulty': 'intermediate'
        },
        {
            'title': 'Unique Elements',
            'description': 'Write a function that returns unique elements from an array.',
            'solution': 'function uniqueElements(arr) { return [...new Set(arr)]; }',
            'hint': 'Use Set and spread operator.',
            'language': 'javascript',
            'difficulty': 'intermediate'
        },
        {
            'title': 'Second Largest',
            'description': 'Write a function that returns the second largest number in an array.',
            'solution': 'function secondLargest(arr) { return [...new Set(arr)].sort((a,b)=>b-a)[1]; }',
            'hint': 'Sort unique values in descending order.',
            'language': 'javascript',
            'difficulty': 'intermediate'
        },
        {
            'title': 'Merge Objects',
            'description': 'Write a function that merges two objects.',
            'solution': 'function mergeObjects(a, b) { return {...a, ...b}; }',
            'hint': 'Use the spread operator.',
            'language': 'javascript',
            'difficulty': 'intermediate'
        }
    ],
    'advanced': [
        {
            'title': 'Binary Search Tree',
            'description': 'Implement a binary search tree with insert and search operations.',
            'solution': '''class Node {
    constructor(val) {
        this.val = val;
        this.left = null;
        this.right = null;
    }
}
function insert(root, val) {
    if (!root) return new Node(val);
    if (val < root.val) root.left = insert(root.left, val);
    else root.right = insert(root.right, val);
    return root;
}''',
            'hint': 'Use recursion and compare values.',
            'language': 'javascript',
            'difficulty': 'advanced'
        },
        {
            'title': 'LRU Cache',
            'description': 'Implement a Least Recently Used (LRU) cache.',
            'solution': '''class LRUCache {
    constructor(capacity) {
        this.capacity = capacity;
        this.cache = new Map();
    }
    get(key) {
        if (!this.cache.has(key)) return -1;
        const val = this.cache.get(key);
        this.cache.delete(key);
        this.cache.set(key, val);
        return val;
    }
    put(key, value) {
        if (this.cache.has(key)) this.cache.delete(key);
        this.cache.set(key, value);
        if (this.cache.size > this.capacity) this.cache.delete(this.cache.keys().next().value);
    }
}''',
            'hint': 'Use a Map to keep order and size.',
            'language': 'javascript',
            'difficulty': 'advanced'
        },
        {
            'title': 'Dijkstra Algorithm',
            'description': 'Implement Dijkstra\'s algorithm for shortest path in a graph.',
            'solution': '''function dijkstra(graph, start) {
    const distances = {};
    const visited = {};
    for (let node in graph) distances[node] = Infinity;
    distances[start] = 0;
    while (true) {
        let closest = null;
        for (let node in distances) {
            if (!visited[node] && (closest === null || distances[node] < distances[closest])) closest = node;
        }
        if (closest === null) break;
        visited[closest] = true;
        for (let neighbor in graph[closest]) {
            let dist = distances[closest] + graph[closest][neighbor];
            if (dist < distances[neighbor]) distances[neighbor] = dist;
        }
    }
    return distances;
}''',
            'hint': 'Track distances and visited nodes.',
            'language': 'javascript',
            'difficulty': 'advanced'
        },
        {
            'title': 'Debounce Function',
            'description': 'Write a debounce function that delays invoking a function until after wait ms have elapsed.',
            'solution': '''function debounce(fn, wait) {
    let timeout;
    return function(...args) {
        clearTimeout(timeout);
        timeout = setTimeout(() => fn.apply(this, args), wait);
    };
}''',
            'hint': 'Use setTimeout and clearTimeout.',
            'language': 'javascript',
            'difficulty': 'advanced'
        },
        {
            'title': 'Throttle Function',
            'description': 'Write a throttle function that only allows a function to be called once every wait ms.',
            'solution': '''function throttle(fn, wait) {
    let last = 0;
    return function(...args) {
        const now = Date.now();
        if (now - last >= wait) {
            last = now;
            fn.apply(this, args);
        }
    };
}''',
            'hint': 'Track last call time with Date.now().',
            'language': 'javascript',
            'difficulty': 'advanced'
        },
        {
            'title': 'Deep Clone Object',
            'description': 'Write a function to deep clone an object.',
            'solution': 'function deepClone(obj) { return JSON.parse(JSON.stringify(obj)); }',
            'hint': 'Use JSON.stringify and JSON.parse for simple objects.',
            'language': 'javascript',
            'difficulty': 'advanced'
        },
        {
            'title': 'Promise All',
            'description': 'Implement a function similar to Promise.all.',
            'solution': '''function promiseAll(promises) {
    return new Promise((resolve, reject) => {
        let results = [], completed = 0;
        promises.forEach((p, i) => {
            Promise.resolve(p).then(val => {
                results[i] = val;
                completed++;
                if (completed === promises.length) resolve(results);
            }, reject);
        });
    });
}''',
            'hint': 'Track completion and resolve when all are done.',
            'language': 'javascript',
            'difficulty': 'advanced'
        },
        {
            'title': 'Event Emitter',
            'description': 'Implement a simple EventEmitter class.',
            'solution': '''class EventEmitter {
    constructor() { this.events = {}; }
    on(event, listener) {
        (this.events[event] = this.events[event] || []).push(listener);
    }
    emit(event, ...args) {
        (this.events[event] || []).forEach(fn => fn(...args));
    }
}''',
            'hint': 'Store listeners in an object by event name.',
            'language': 'javascript',
            'difficulty': 'advanced'
        },
        {
            'title': 'Memoization',
            'description': 'Write a memoize function for single-argument functions.',
            'solution': '''function memoize(fn) {
    const cache = {};
    return function(arg) {
        if (cache[arg] !== undefined) return cache[arg];
        return cache[arg] = fn(arg);
    };
}''',
            'hint': 'Use a cache object to store results.',
            'language': 'javascript',
            'difficulty': 'advanced'
        },
        {
            'title': 'Singleton Pattern',
            'description': 'Implement the Singleton design pattern in JavaScript.',
            'solution': '''class Singleton {
    constructor() {
        if (Singleton.instance) return Singleton.instance;
        Singleton.instance = this;
    }
}''',
            'hint': 'Store the instance as a static property.',
            'language': 'javascript',
            'difficulty': 'advanced'
        }
    ]
}

TYPESCRIPT_CHALLENGES = {
    'beginner': [
        {
            'title': 'Basic Type Annotation',
            'description': 'Declare a variable "age" of type number and assign it the value 25.',
            'solution': 'let age: number = 25;',
            'hint': 'Use : number after the variable name.',
            'language': 'typescript',
            'difficulty': 'beginner'
        },
        {
            'title': 'String Type',
            'description': 'Declare a variable "username" of type string and assign it "Alice".',
            'solution': 'let username: string = "Alice";',
            'hint': 'Use : string after the variable name.',
            'language': 'typescript',
            'difficulty': 'beginner'
        },
        {
            'title': 'Boolean Type',
            'description': 'Declare a variable "isActive" of type boolean and assign it true.',
            'solution': 'let isActive: boolean = true;',
            'hint': 'Use : boolean after the variable name.',
            'language': 'typescript',
            'difficulty': 'beginner'
        },
        {
            'title': 'Array of Numbers',
            'description': 'Declare an array "scores" that holds numbers: 10, 20, 30.',
            'solution': 'let scores: number[] = [10, 20, 30];',
            'hint': 'Use number[] for an array of numbers.',
            'language': 'typescript',
            'difficulty': 'beginner'
        },
        {
            'title': 'Function with Type',
            'description': 'Write a function "greet" that takes a string "name" and returns a greeting string.',
            'solution': 'function greet(name: string): string { return "Hello, " + name; }',
            'hint': 'Annotate parameter and return type.',
            'language': 'typescript',
            'difficulty': 'beginner'
        },
        {
            'title': 'Union Type',
            'description': 'Declare a variable "id" that can be a number or a string.',
            'solution': 'let id: number | string;',
            'hint': 'Use | to combine types.',
            'language': 'typescript',
            'difficulty': 'beginner'
        },
        {
            'title': 'Tuple Type',
            'description': 'Declare a tuple "person" with a string and a number.',
            'solution': 'let person: [string, number] = ["Bob", 42];',
            'hint': 'Use [string, number] for a tuple.',
            'language': 'typescript',
            'difficulty': 'beginner'
        },
        {
            'title': 'Enum Declaration',
            'description': 'Declare an enum "Color" with values Red, Green, Blue.',
            'solution': 'enum Color { Red, Green, Blue }',
            'hint': 'Use enum keyword.',
            'language': 'typescript',
            'difficulty': 'beginner'
        },
        {
            'title': 'Any Type',
            'description': 'Declare a variable "data" of type any and assign it 5.',
            'solution': 'let data: any = 5;',
            'hint': 'Use : any for dynamic typing.',
            'language': 'typescript',
            'difficulty': 'beginner'
        },
        {
            'title': 'Type Assertion',
            'description': 'Assign the string "123" to a variable and assert it as a number.',
            'solution': 'let str = "123";\nlet num = str as unknown as number;',
            'hint': 'Use as keyword for type assertion.',
            'language': 'typescript',
            'difficulty': 'beginner'
        }
    ],
    'intermediate': [
        {
            'title': 'Interface Definition',
            'description': 'Define an interface "User" with properties name (string) and age (number).',
            'solution': 'interface User { name: string; age: number; }',
            'hint': 'Use interface keyword.',
            'language': 'typescript',
            'difficulty': 'intermediate'
        },
        {
            'title': 'Function Interface',
            'description': 'Define an interface "Adder" for a function that takes two numbers and returns a number.',
            'solution': 'interface Adder { (a: number, b: number): number; }',
            'hint': 'Function interfaces use parentheses.',
            'language': 'typescript',
            'difficulty': 'intermediate'
        },
        {
            'title': 'Optional Property',
            'description': 'Add an optional property "email" (string) to the "User" interface.',
            'solution': 'interface User { name: string; age: number; email?: string; }',
            'hint': 'Use ? for optional properties.',
            'language': 'typescript',
            'difficulty': 'intermediate'
        },
        {
            'title': 'Readonly Property',
            'description': 'Add a readonly property "id" (number) to the "User" interface.',
            'solution': 'interface User { readonly id: number; name: string; age: number; }',
            'hint': 'Use readonly keyword.',
            'language': 'typescript',
            'difficulty': 'intermediate'
        },
        {
            'title': 'Type Alias',
            'description': 'Create a type alias "Point" for an object with x and y as numbers.',
            'solution': 'type Point = { x: number; y: number; };',
            'hint': 'Use type keyword for aliases.',
            'language': 'typescript',
            'difficulty': 'intermediate'
        },
        {
            'title': 'Intersection Type',
            'description': 'Create a type "Person" that combines "Nameable" and "Ageable" types.',
            'solution': 'type Nameable = { name: string; };\ntype Ageable = { age: number; };\ntype Person = Nameable & Ageable;',
            'hint': 'Use & to combine types.',
            'language': 'typescript',
            'difficulty': 'intermediate'
        },
        {
            'title': 'Literal Types',
            'description': 'Declare a variable "direction" that can only be "left" or "right".',
            'solution': 'let direction: "left" | "right";',
            'hint': 'Use string literal types with |.',
            'language': 'typescript',
            'difficulty': 'intermediate'
        },
        {
            'title': 'Function Overloads',
            'description': 'Write function overloads for "add" that can add numbers or concatenate strings.',
            'solution': 'function add(a: number, b: number): number;\nfunction add(a: string, b: string): string;\nfunction add(a: any, b: any): any { return a + b; }',
            'hint': 'Declare multiple signatures before the implementation.',
            'language': 'typescript',
            'difficulty': 'intermediate'
        },
        {
            'title': 'Generic Function',
            'description': 'Write a generic function "identity" that returns its argument.',
            'solution': 'function identity<T>(arg: T): T { return arg; }',
            'hint': 'Use <T> to declare a generic.',
            'language': 'typescript',
            'difficulty': 'intermediate'
        },
        {
            'title': 'Keyof Operator',
            'description': 'Write a function that takes an object and a key of that object, and returns the value.',
            'solution': 'function getValue<T, K extends keyof T>(obj: T, key: K): T[K] { return obj[key]; }',
            'hint': 'Use keyof and generics.',
            'language': 'typescript',
            'difficulty': 'intermediate'
        }
    ],
    'advanced': [
        {
            'title': 'Generic Interface',
            'description': 'Define a generic interface "Box" with a value of type T.',
            'solution': 'interface Box<T> { value: T; }',
            'hint': 'Use <T> in the interface definition.',
            'language': 'typescript',
            'difficulty': 'advanced'
        },
        {
            'title': 'Mapped Types',
            'description': 'Create a mapped type "Readonly<T>" that makes all properties of T readonly.',
            'solution': 'type Readonly<T> = { readonly [P in keyof T]: T[P]; };',
            'hint': 'Use [P in keyof T] and readonly.',
            'language': 'typescript',
            'difficulty': 'advanced'
        },
        {
            'title': 'Conditional Types',
            'description': 'Write a conditional type "IsString<T>" that is true if T is string, false otherwise.',
            'solution': 'type IsString<T> = T extends string ? true : false;',
            'hint': 'Use extends in type definitions.',
            'language': 'typescript',
            'difficulty': 'advanced'
        },
        {
            'title': 'Infer Keyword',
            'description': 'Use infer to extract the return type of a function type.',
            'solution': 'type ReturnType<T> = T extends (...args: any[]) => infer R ? R : any;',
            'hint': 'Use infer R in a conditional type.',
            'language': 'typescript',
            'difficulty': 'advanced'
        },
        {
            'title': 'Discriminated Unions',
            'description': 'Create a union type "Shape" with "Circle" and "Square" types, each with a kind property.',
            'solution': 'type Circle = { kind: "circle"; radius: number; };\ntype Square = { kind: "square"; side: number; };\ntype Shape = Circle | Square;',
            'hint': 'Use a common "kind" property.',
            'language': 'typescript',
            'difficulty': 'advanced'
        },
        {
            'title': 'Type Guards',
            'description': 'Write a type guard function "isString" that checks if a value is a string.',
            'solution': 'function isString(x: any): x is string { return typeof x === "string"; }',
            'hint': 'Return x is string and use typeof.',
            'language': 'typescript',
            'difficulty': 'advanced'
        },
        {
            'title': 'Utility Types',
            'description': 'Use the Partial utility type to make all properties of an interface optional.',
            'solution': 'interface User { name: string; age: number; }\ntype PartialUser = Partial<User>;',
            'hint': 'Use Partial<T>.',
            'language': 'typescript',
            'difficulty': 'advanced'
        },
        {
            'title': 'Index Signatures',
            'description': 'Define an interface "Dictionary" with string keys and number values.',
            'solution': 'interface Dictionary { [key: string]: number; }',
            'hint': 'Use [key: string]: number.',
            'language': 'typescript',
            'difficulty': 'advanced'
        },
        {
            'title': 'Never Type',
            'description': 'Write a function "fail" that always throws and has return type never.',
            'solution': 'function fail(message: string): never { throw new Error(message); }',
            'hint': 'Use never as the return type.',
            'language': 'typescript',
            'difficulty': 'advanced'
        },
        {
            'title': 'Recursive Types',
            'description': 'Define a recursive type "NestedArray" for arrays of numbers or arrays of NestedArray.',
            'solution': 'type NestedArray = number | NestedArray[];',
            'hint': 'A type can reference itself.',
            'language': 'typescript',
            'difficulty': 'advanced'
        }
    ]
}

NEXTJS_CHALLENGES = {
    'beginner': [
        {
            'title': 'Create a Basic Next.js App',
            'description': 'Create a new Next.js application using create-next-app and set up the basic project structure.',
            'solution': 'npx create-next-app@latest my-app\ncd my-app\nnpm run dev',
            'hint': 'Use the create-next-app command to bootstrap your application.',
            'language': 'nextjs',
            'difficulty': 'beginner'
        },
        {
            'title': 'Create a Home Page',
            'description': 'Create a home page component in the pages directory that displays a welcome message.',
            'solution': '// pages/index.js\nexport default function Home() {\n  return <h1>Welcome to My Next.js App!</h1>\n}',
            'hint': 'Create a new file in the pages directory and export a React component.',
            'language': 'nextjs',
            'difficulty': 'beginner'
        },
        {
            'title': 'Add Navigation',
            'description': 'Create a navigation bar component and add it to your layout.',
            'solution': '// components/Navbar.js\nimport Link from "next/link";\n\nexport default function Navbar() {\n  return (\n    <nav>\n      <Link href="/">Home</Link>\n      <Link href="/about">About</Link>\n    </nav>\n  )\n}',
            'hint': 'Use Next.js Link component for client-side navigation.',
            'language': 'nextjs',
            'difficulty': 'beginner'
        },
        {
            'title': 'Create an About Page',
            'description': 'Create an about page with some basic information about your application.',
            'solution': '// pages/about.js\nexport default function About() {\n  return (\n    <div>\n      <h1>About Us</h1>\n      <p>This is our Next.js application.</p>\n    </div>\n  )\n}',
            'hint': 'Create a new file in the pages directory for the about page.',
            'language': 'nextjs',
            'difficulty': 'beginner'
        },
        {
            'title': 'Add CSS Styling',
            'description': 'Add CSS styling to your Next.js application using CSS modules.',
            'solution': '// styles/Home.module.css\n.container {\n  padding: 2rem;\n}\n\n// pages/index.js\nimport styles from "../styles/Home.module.css";\n\nexport default function Home() {\n  return <div className={styles.container}>Content</div>\n}',
            'hint': 'Create a CSS module file and import it in your component.',
            'language': 'nextjs',
            'difficulty': 'beginner'
        },
        {
            'title': 'Add Images',
            'description': 'Use Next.js Image component to add optimized images to your application.',
            'solution': '// pages/index.js\nimport Image from "next/image";\n\nexport default function Home() {\n  return (\n    <Image\n      src="/profile.jpg"\n      alt="Profile"\n      width={500}\n      height={300}\n    />\n  )\n}',
            'hint': 'Use the Next.js Image component for optimized images.',
            'language': 'nextjs',
            'difficulty': 'beginner'
        },
        {
            'title': 'Create a Layout',
            'description': 'Create a layout component that wraps your pages.',
            'solution': '// components/Layout.js\nexport default function Layout({ children }) {\n  return (\n    <div>\n      <Navbar />\n      <main>{children}</main>\n      <footer>Footer</footer>\n    </div>\n  )\n}',
            'hint': 'Create a layout component that accepts children as props.',
            'language': 'nextjs',
            'difficulty': 'beginner'
        },
        {
            'title': 'Add Meta Tags',
            'description': 'Add meta tags to your pages using Next.js Head component.',
            'solution': '// pages/index.js\nimport Head from "next/head";\n\nexport default function Home() {\n  return (\n    <>\n      <Head>\n        <title>My Next.js App</title>\n        <meta name="description" content="My Next.js application" />\n      </Head>\n      <h1>Home</h1>\n    </>\n  )\n}',
            'hint': 'Use the Next.js Head component to add meta tags.',
            'language': 'nextjs',
            'difficulty': 'beginner'
        },
        {
            'title': 'Create a Contact Form',
            'description': 'Create a simple contact form with name and email fields.',
            'solution': '// pages/contact.js\nexport default function Contact() {\n  return (\n    <form>\n      <input type="text" name="name" placeholder="Name" />\n      <input type="email" name="email" placeholder="Email" />\n      <button type="submit">Submit</button>\n    </form>\n  )\n}',
            'hint': 'Create a form with basic input fields.',
            'language': 'nextjs',
            'difficulty': 'beginner'
        },
        {
            'title': 'Add Environment Variables',
            'description': 'Set up environment variables in your Next.js application.',
            'solution': '// .env.local\nAPI_KEY=your_api_key\n\n// pages/index.js\nconsole.log(process.env.API_KEY);',
            'hint': 'Create a .env.local file and access variables using process.env.',
            'language': 'nextjs',
            'difficulty': 'beginner'
        }
    ],
    'intermediate': [
        {
            'title': 'Create Dynamic Routes',
            'description': 'Set up dynamic routing for blog posts using [id].js.',
            'solution': '// pages/posts/[id].js\nexport default function Post({ post }) {\n  return (\n    <div>\n      <h1>{post.title}</h1>\n      <p>{post.content}</p>\n    </div>\n  )\n}\n\nexport async function getStaticProps({ params }) {\n  const post = await getPost(params.id);\n  return { props: { post } };\n}\n\nexport async function getStaticPaths() {\n  const posts = await getAllPosts();\n  return {\n    paths: posts.map(post => ({ params: { id: post.id } })),\n    fallback: false\n  };\n}',
            'hint': 'Use getStaticProps and getStaticPaths for static generation.',
            'language': 'nextjs',
            'difficulty': 'intermediate'
        },
        {
            'title': 'Implement API Routes',
            'description': 'Create an API route to handle form submissions.',
            'solution': '// pages/api/contact.js\nexport default function handler(req, res) {\n  if (req.method === "POST") {\n    const { name, email } = req.body;\n    // Process the data\n    res.status(200).json({ success: true });\n  } else {\n    res.status(405).json({ message: "Method not allowed" });\n  }\n}',
            'hint': 'Create a file in the pages/api directory to handle API requests.',
            'language': 'nextjs',
            'difficulty': 'intermediate'
        },
        {
            'title': 'Add Authentication',
            'description': 'Implement authentication using NextAuth.js.',
            'solution': '// pages/api/auth/[...nextauth].js\nimport NextAuth from "next-auth";\nimport Providers from "next-auth/providers";\n\nexport default NextAuth({\n  providers: [\n    Providers.Google({\n      clientId: process.env.GOOGLE_ID,\n      clientSecret: process.env.GOOGLE_SECRET,\n    }),\n  ],\n});',
            'hint': 'Set up NextAuth.js with a provider like Google.',
            'language': 'nextjs',
            'difficulty': 'intermediate'
        },
        {
            'title': 'Implement State Management',
            'description': 'Add state management using Context API.',
            'solution': '// context/ThemeContext.js\nimport { createContext, useState } from "react";\n\nexport const ThemeContext = createContext();\n\nexport function ThemeProvider({ children }) {\n  const [theme, setTheme] = useState("light");\n  return (\n    <ThemeContext.Provider value={{ theme, setTheme }}>\n      {children}\n    </ThemeContext.Provider>\n  );\n}',
            'hint': 'Create a context provider for your state.',
            'language': 'nextjs',
            'difficulty': 'intermediate'
        },
        {
            'title': 'Add Data Fetching',
            'description': 'Implement data fetching using SWR.',
            'solution': '// pages/posts.js\nimport useSWR from "swr";\n\nfunction Posts() {\n  const { data, error } = useSWR("/api/posts", fetcher);\n  if (error) return <div>Failed to load</div>;\n  if (!data) return <div>Loading...</div>;\n  return <div>{data.map(post => <div key={post.id}>{post.title}</div>)}</div>;\n}',
            'hint': 'Use SWR for client-side data fetching.',
            'language': 'nextjs',
            'difficulty': 'intermediate'
        },
        {
            'title': 'Implement Server-side Rendering',
            'description': 'Create a page that uses server-side rendering.',
            'solution': '// pages/ssr.js\nexport default function SSRPage({ data }) {\n  return <div>{data}</div>;\n}\n\nexport async function getServerSideProps() {\n  const data = await fetchData();\n  return { props: { data } };\n}',
            'hint': 'Use getServerSideProps for server-side rendering.',
            'language': 'nextjs',
            'difficulty': 'intermediate'
        },
        {
            'title': 'Add Error Handling',
            'description': 'Implement custom error pages in Next.js.',
            'solution': '// pages/404.js\nexport default function Custom404() {\n  return <h1>404 - Page Not Found</h1>;\n}\n\n// pages/_error.js\nexport default function Error({ statusCode }) {\n  return <h1>{statusCode} - An error occurred</h1>;\n}',
            'hint': 'Create custom 404 and error pages.',
            'language': 'nextjs',
            'difficulty': 'intermediate'
        },
        {
            'title': 'Implement Middleware',
            'description': 'Create a middleware to handle authentication.',
            'solution': '// middleware.js\nexport function middleware(request) {\n  if (!request.cookies.get("auth")) {\n    return NextResponse.redirect("/login");\n  }\n  return NextResponse.next();\n}\n\nexport const config = {\n  matcher: ["/dashboard/:path*"],\n};',
            'hint': 'Create a middleware file to handle authentication.',
            'language': 'nextjs',
            'difficulty': 'intermediate'
        },
        {
            'title': 'Add Internationalization',
            'description': 'Implement internationalization using next-i18next.',
            'solution': '// next-i18next.config.js\nmodule.exports = {\n  i18n: {\n    locales: ["en", "fr"],\n    defaultLocale: "en",\n  },\n};\n\n// pages/index.js\nimport { useTranslation } from "next-i18next";\n\nexport default function Home() {\n  const { t } = useTranslation();\n  return <h1>{t("welcome")}</h1>;\n}',
            'hint': 'Set up next-i18next for internationalization.',
            'language': 'nextjs',
            'difficulty': 'intermediate'
        },
        {
            'title': 'Implement API Rate Limiting',
            'description': 'Add rate limiting to your API routes.',
            'solution': '// pages/api/limited.js\nimport rateLimit from "express-rate-limit";\n\nconst limiter = rateLimit({\n  windowMs: 15 * 60 * 1000,\n  max: 100,\n});\n\nexport default function handler(req, res) {\n  limiter(req, res, () => {\n    // Your API logic here\n  });\n}',
            'hint': 'Use express-rate-limit for API rate limiting.',
            'language': 'nextjs',
            'difficulty': 'intermediate'
        }
    ],
    'advanced': [
        {
            'title': 'Implement Custom Server',
            'description': 'Create a custom server with Express and Next.js.',
            'solution': '// server.js\nconst express = require("express");\nconst next = require("next");\n\nconst dev = process.env.NODE_ENV !== "production";\nconst app = next({ dev });\nconst handle = app.getRequestHandler();\n\napp.prepare().then(() => {\n  const server = express();\n  server.all("*", (req, res) => handle(req, res));\n  server.listen(3000);\n});',
            'hint': 'Create a custom server using Express and Next.js.',
            'language': 'nextjs',
            'difficulty': 'advanced'
        },
        {
            'title': 'Implement WebSocket',
            'description': 'Add WebSocket support to your Next.js application.',
            'solution': '// pages/api/socket.js\nimport { Server } from "socket.io";\n\nconst ioHandler = (req, res) => {\n  if (!res.socket.server.io) {\n    const io = new Server(res.socket.server);\n    res.socket.server.io = io;\n    io.on("connection", socket => {\n      socket.on("message", msg => {\n        io.emit("message", msg);\n      });\n    });\n  }\n  res.end();\n};\n\nexport default ioHandler;',
            'hint': 'Use socket.io to implement WebSocket functionality.',
            'language': 'nextjs',
            'difficulty': 'advanced'
        },
        {
            'title': 'Implement GraphQL',
            'description': 'Add GraphQL support using Apollo Client.',
            'solution': '// lib/apollo-client.js\nimport { ApolloClient, InMemoryCache } from "@apollo/client";\n\nexport const client = new ApolloClient({\n  uri: "/api/graphql",\n  cache: new InMemoryCache(),\n});\n\n// pages/index.js\nimport { useQuery } from "@apollo/client";\nimport { GET_POSTS } from "../queries";\n\nfunction Posts() {\n  const { data } = useQuery(GET_POSTS);\n  return <div>{data?.posts.map(post => <div key={post.id}>{post.title}</div>)}</div>;\n}',
            'hint': 'Set up Apollo Client for GraphQL support.',
            'language': 'nextjs',
            'difficulty': 'advanced'
        },
        {
            'title': 'Implement Serverless Functions',
            'description': 'Create serverless functions using Vercel.',
            'solution': '// api/hello.js\nexport default function handler(req, res) {\n  res.status(200).json({ message: "Hello from serverless function!" });\n}',
            'hint': 'Create serverless functions in the api directory.',
            'language': 'nextjs',
            'difficulty': 'advanced'
        },
        {
            'title': 'Implement PWA',
            'description': 'Convert your Next.js app to a Progressive Web App.',
            'solution': '// next.config.js\nconst withPWA = require("next-pwa");\n\nmodule.exports = withPWA({\n  pwa: {\n    dest: "public",\n    register: true,\n    skipWaiting: true,\n  },\n});',
            'hint': 'Use next-pwa to implement PWA features.',
            'language': 'nextjs',
            'difficulty': 'advanced'
        },
        {
            'title': 'Implement SEO',
            'description': 'Add advanced SEO features to your Next.js application.',
            'solution': '// components/SEO.js\nimport Head from "next/head";\n\nexport default function SEO({ title, description }) {\n  return (\n    <Head>\n      <title>{title}</title>\n      <meta name="description" content={description} />\n      <meta property="og:title" content={title} />\n      <meta property="og:description" content={description} />\n    </Head>\n  );\n}',
            'hint': 'Create a reusable SEO component.',
            'language': 'nextjs',
            'difficulty': 'advanced'
        },
        {
            'title': 'Implement Testing',
            'description': 'Add testing to your Next.js application using Jest and React Testing Library.',
            'solution': '// tests/Home.test.js\nimport { render, screen } from "@testing-library/react";\nimport Home from "../pages/index";\n\ntest("renders home page", () => {\n  render(<Home />);\n  expect(screen.getByText("Welcome")).toBeInTheDocument();\n});',
            'hint': 'Set up Jest and React Testing Library for testing.',
            'language': 'nextjs',
            'difficulty': 'advanced'
        },
        {
            'title': 'Implement CI/CD',
            'description': 'Set up continuous integration and deployment for your Next.js app.',
            'solution': '// .github/workflows/ci.yml\nname: CI\n\non: [push, pull_request]\n\njobs:\n  build:\n    runs-on: ubuntu-latest\n    steps:\n      - uses: actions/checkout@v2\n      - uses: actions/setup-node@v2\n      - run: npm install\n      - run: npm run build\n      - run: npm run test',
            'hint': 'Create GitHub Actions workflow for CI/CD.',
            'language': 'nextjs',
            'difficulty': 'advanced'
        },
        {
            'title': 'Implement Performance Monitoring',
            'description': 'Add performance monitoring to your Next.js application.',
            'solution': '// pages/_app.js\nimport { useEffect } from "react";\nimport { useRouter } from "next/router";\n\nexport default function App({ Component, pageProps }) {\n  const router = useRouter();\n  useEffect(() => {\n    const handleRouteChange = (url) => {\n      // Send pageview to analytics\n    };\n    router.events.on("routeChangeComplete", handleRouteChange);\n    return () => {\n      router.events.off("routeChangeComplete", handleRouteChange);\n    };\n  }, [router.events]);\n  return <Component {...pageProps} />;\n}',
            'hint': 'Use router events to monitor performance.',
            'language': 'nextjs',
            'difficulty': 'advanced'
        },
        {
            'title': 'Implement Security Headers',
            'description': 'Add security headers to your Next.js application.',
            'solution': '// next.config.js\nmodule.exports = {\n  async headers() {\n    return [\n      {\n        source: "/(.*)",\n        headers: [\n          {\n            key: "X-Content-Type-Options",\n            value: "nosniff",\n          },\n          {\n            key: "X-Frame-Options",\n            value: "DENY",\n          },\n        ],\n      },\n    ];\n  },\n};',
            'hint': 'Configure security headers in next.config.js.',
            'language': 'nextjs',
            'difficulty': 'advanced'
        }
    ]
} 