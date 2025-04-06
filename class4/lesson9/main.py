#lesson 9
# 1. Basic try-except Example
print("1. Basic try-except Example:")
try:
    result = 10 / 0  # This will raise a ZeroDivisionError
except:
    print("An error occurred!")
print()

# 2. Specific Exception Handling
print("2. Specific Exception Handling:")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
print()

# 3. try-except-else Example
print("3. try-except-else Example:")
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print(f"Division successful. Result: {result}")
print()

# 4. try-except-finally Example
print("4. try-except-finally Example:")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
finally:
    print("This will always execute.")
print()

# 5. Comprehensive Example
print("5. Comprehensive Example:")
def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    except TypeError:
        print("Error: Invalid input type. Numbers required.")
    else:
        print(f"Division successful. Result: {result}")
    finally:
        print("Operation complete.")

# Test cases
divide_numbers(10, 2)  # Successful division
divide_numbers(10, 0)  # ZeroDivisionError
divide_numbers(10, "2")  # TypeError
print()

# 6. Raising Exceptions
print("6. Raising Exceptions:")
def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed!")
    return a / b

try:
    result = divide(5, 0)
    print(result)
except ValueError as e:
    print(f"Error: {e}")
print()

# 7. Custom Exceptions
print("7. Custom Exceptions:")
class NegativeNumberError(Exception):
    """Custom exception for negative numbers"""
    pass

def check_positive(n):
    if n < 0:
        raise NegativeNumberError("Negative numbers are not allowed!")
    return f"{n} is positive"

try:
    print(check_positive(-5))
except NegativeNumberError as e:
    print(f"Custom Exception Caught: {e}", " - Exception Class Type: ", type(e))
print()

# 8. NoReturn Example
print("8. NoReturn Example:")
from typing import NoReturn

def terminate_program() -> NoReturn:
    """Terminate the program by raising an exception."""
    raise SystemExit("Terminating the program.")

try:
    terminate_program()
except SystemExit as e:
    print(f"Program terminated: {e}")
print()

# 9. Practical Example with File Handling
print("9. Practical Example with File Handling:")
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("File content:", content)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except PermissionError:
        print(f"Error: Permission denied to read '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("File operation completed.")

# Test cases
read_file("nonexistent.txt")  # FileNotFoundError
print()

# 10. User Input Validation
print("10. User Input Validation:")
def get_user_input():
    try:
        age = int(input("Enter your age: "))
        if age < 0:
            raise ValueError("Age cannot be negative!")
        print(f"Your age is: {age}")
    except ValueError as e:
        print(f"Invalid input: {e}")
    except KeyboardInterrupt:
        print("\nProgram interrupted by user")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Uncomment to test user input
# get_user_input()
print()

# 11. Complex Example with Multiple Error Types
print("11. Complex Example with Multiple Error Types:")
def process_data(data):
    try:
        if not isinstance(data, list):
            raise TypeError("Input must be a list")
        if not data:
            raise ValueError("List cannot be empty")
        result = sum(data) / len(data)
        print(f"Average: {result}")
    except TypeError as e:
        print(f"Type Error: {e}")
    except ValueError as e:
        print(f"Value Error: {e}")
    except ZeroDivisionError:
        print("Error: Cannot calculate average of empty list")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        print("Data processing completed")

# Test cases
process_data([1, 2, 3, 4, 5])  # Valid input
process_data([])  # Empty list
process_data("not a list")  # Wrong type
print()
