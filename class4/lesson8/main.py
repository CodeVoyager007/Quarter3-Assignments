#lesson 8
# 1. Built-in Module Example
import math
print("1. Built-in Module Example:")
print(f"Square root of 25: {math.sqrt(25)}")
print()

# 2. User-Defined Module Example
def add(a, b):
    return a + b

print("2. User-Defined Function Example:")
print(f"5 + 3 = {add(5, 3)}")
print()

# 3. Function Arguments Example
def greet(name):
    print(f"Hello {name}")

print("3. Function Arguments Example:")
greet("Ali")
print()

# 4. Keyword Arguments Example
def print_info(name, age):
    print(f"Name: {name}")
    print(f"Age: {age}")

print("4. Keyword Arguments Example:")
print_info(age=50, name="Arif")
print()

# 5. Default Arguments Example
def print_info_default(name, age=35):
    print(f"Name: {name}")
    print(f"Age: {age}")

print("5. Default Arguments Example:")
print_info_default(name="Arif")
print()

# 6. Variable-length Arguments Example
def print_variable_args(arg1, *vartuple):
    print(f"First argument: {arg1}")
    for var in vartuple:
        print(f"Additional argument: {var}")

print("6. Variable-length Arguments Example:")
print_variable_args(10, 20, 30, 40)
print()

# 7. Lambda Function Example
print("7. Lambda Function Example:")
add_lambda = lambda x, y: x + y
print(f"Lambda addition: {add_lambda(5, 3)}")
print()

# 8. Scope of Variables Example
total = 0  # Global variable

def sum_numbers(a, b):
    total = a + b  # Local variable
    print(f"Inside function total: {total}")
    return total

print("8. Scope of Variables Example:")
sum_numbers(10, 20)
print(f"Outside function total: {total}")
print()

# 9. Generator Function Example
def simple_generator():
    yield 1
    yield 2
    yield 3

print("9. Generator Function Example:")
gen = simple_generator()
for value in gen:
    print(f"Generated value: {value}")
print()

# 10. Recursive Function Example
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print("10. Recursive Function Example:")
print(f"Factorial of 5: {factorial(5)}")
print()

# 11. Multi-type Return Example
def multi_type_return():
    return 42, [1, 2, 3], {"name": "Arif", "age": 35}

print("11. Multi-type Return Example:")
number, numbers_list, person_dict = multi_type_return()
print(f"Number: {number}")
print(f"List: {numbers_list}")
print(f"Dictionary: {person_dict}")
