
# Creating lists with different data types
fruits: list  = ["apple", "banana", "cherry"]
numbers: list = [10, 20, 30, 40]
mixed: list   = ["hello", 42, 3.14, True]

print("fruits  = ", fruits)
print("numbers = ", numbers)
print("mixed   = ", mixed)

# Accessing List Elements
print(fruits[0])   
print(fruits[-3])  
# Modifying Lists
fruits[-3] = "watermelon" 
print(fruits)  

# List Slicing
print(fruits[0:2])  

# Appending and Extending Lists
fruits.append("mango")  
fruits.extend(["grape", "kiwi"]) 
print(fruits)

# Removing Elements
fruits.remove("banana")  
deleted = fruits.pop(1)  
print("deleted element = ", deleted)
print(fruits)

# Sorting a List
numbers: list[int] = [3, 1, 4, 1, 5, 9]
numbers.sort()
print(numbers) 

numbers.sort(reverse=True)
print(numbers)

words = ["apple", "kiwi", "banana"]
words.sort(key=len)
print(words) 

words.sort(key=lambda word: word[-1])
print(words) 

# Reverse Sorting
numbers.reverse()
print(numbers)  
# Iterating Over Lists
for fruit in fruits:
    print(fruit)

# List Comprehension
squared: list = [x**2 for x in [1, 2, 3, 4, 5]]
print(squared) 
