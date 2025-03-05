from colorama import init, Fore
init()

def show_title(message):
    print(Fore.YELLOW + "=" * 50)
    print(f"Python Tutorial: {message}")
    print("=" * 50 + Fore.RESET)
    print()

def explain_concept(concept):
    print(Fore.GREEN + "📚 What is it?")
    print(concept + Fore.RESET)
    print()

def show_example(operator, example, answer, explanation=""):
    print(Fore.CYAN + f"🔍 Example of {operator}:")
    print(f"Code: {example}")
    print(f"Output: {answer}")
    if explanation:
        print(f"Explanation: {explanation}")
    print(Fore.RESET)
    print()

def learn_arithmetic():
    show_title("Arithmetic Operators in Python")
    
    explain_concept("""Arithmetic operators in Python are used for mathematical calculations.
Python provides all basic math operations, plus some extra ones like // for floor division
and ** for exponentiation, which are very useful in programming.""")
    
    num1 = 10
    num2 = 3
    
    print("Let's try some calculations with:", num1, "and", num2)
    input("Press Enter to see examples...")
    print()
    
    examples = [
        ("addition (+)", f"{num1} + {num2}", num1 + num2, "Basic addition, just like in math"),
        ("subtraction (-)", f"{num1} - {num2}", num1 - num2, "Subtracts second number from first"),
        ("multiplication (*)", f"{num1} * {num2}", num1 * num2, "Uses * instead of × for multiplication"),
        ("division (/)", f"{num1} / {num2}", num1 / num2, "Always returns a float in Python 3"),
        ("floor division (//)", f"{num1} // {num2}", num1 // num2, "Divides and rounds down to nearest integer"),
        ("modulus (%)", f"{num1} % {num2}", num1 % num2, "Returns the remainder after division"),
        ("exponentiation (**)", f"{num1} ** 2", num1 ** 2, "Raises number to a power, here it's squared")
    ]
    
    for op, ex, ans, expl in examples:
        show_example(op, ex, ans, expl)
        input("Press Enter for next example...")
        print()

def learn_assignment():
    show_title("Assignment Operators in Python")
    
    explain_concept("""Assignment operators are used to assign values to variables.
Python provides shorthand operators (like +=) that make it easier to modify variables.
These are commonly used in loops and calculations.""")
    
    print(Fore.CYAN + "🔄 Let's see how variables change with different assignments:")
    print("We'll start with x = 5 and modify it in different ways.\n")
    
    x = 5
    steps = [
        ("Basic assignment", "x = 5", x),
        ("Add and assign", "x += 3", x + 3),
        ("Subtract and assign", "x -= 2", x + 3 - 2),
        ("Multiply and assign", "x *= 2", (x + 3 - 2) * 2),
        ("Divide and assign", "x /= 4", ((x + 3 - 2) * 2) / 4)
    ]
    
    for step_name, code, result in steps:
        print(f"{Fore.MAGENTA}{step_name}:")
        print(f"Code: {code}")
        print(f"Value of x becomes: {result}")
        print(f"{Fore.RESET}\n")
        input("Press Enter to see next step...")
        print()

def learn_comparison():
    show_title("Comparison Operators in Python")
    
    explain_concept("""Comparison operators are used to compare values and return True or False.
These are essential for making decisions in your code using if statements and while loops.
Python makes comparisons very intuitive, reading almost like English.""")
    
    x, y = 10, 5
    print(f"We'll compare these values: x = {x} and y = {y}")
    input("Press Enter to start comparing...")
    print()
    
    comparisons = [
        ("equal to (==)", f"{x} == {y}", x == y, "Tests if two values are equal"),
        ("not equal to (!=)", f"{x} != {y}", x != y, "Tests if two values are different"),
        ("greater than (>)", f"{x} > {y}", x > y, "Checks if left value is bigger"),
        ("less than (<)", f"{x} < {y}", x < y, "Checks if left value is smaller"),
        ("greater or equal (>=)", f"{x} >= {y}", x >= y, "Checks if left value is bigger or equal"),
        ("less or equal (<=)", f"{x} <= {y}", x <= y, "Checks if left value is smaller or equal")
    ]
    
    for op, ex, ans, expl in comparisons:
        show_example(op, ex, ans, expl)
        input("Press Enter for next comparison...")
        print()

def learn_logical():
    show_title("Logical Operators in Python")
    
    explain_concept("""Logical operators (and, or, not) are used to combine conditions.
Python uses English words instead of symbols (&&, ||) making code more readable.
These are crucial for complex decision-making in your programs.""")
    
    print(Fore.CYAN + "🌞 Real-world example: Planning a Beach Day")
    is_sunny = True
    is_warm = True
    is_weekend = False
    
    print("\nConditions:")
    print(f"Is it sunny? {is_sunny}")
    print(f"Is it warm? {is_warm}")
    print(f"Is it weekend? {is_weekend}\n")
    
    examples = [
        ("AND operator", "is_sunny and is_warm", is_sunny and is_warm, 
         "Both conditions must be True"),
        ("OR operator", "is_sunny or is_warm", is_sunny or is_warm,
         "At least one condition must be True"),
        ("NOT operator", "not is_weekend", not is_weekend,
         "Inverts True to False or False to True"),
        ("Complex condition", "is_sunny and is_warm and not is_weekend",
         is_sunny and is_warm and not is_weekend,
         "Combining multiple conditions")
    ]
    
    for op, ex, ans, expl in examples:
        show_example(op, ex, ans, expl)
        input("Press Enter for next example...")
        print()

def learn_identity():
    show_title("Identity Operators in Python")
    
    explain_concept("""Identity operators (is, is not) check if two objects are the same in memory.
This is different from equality (==)! Two objects can have the same value but be different objects.
These operators are often used with None and for specific object comparisons.""")
    
    print(Fore.CYAN + "🔍 Let's understand with lists:")
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]  
    list3 = list1     
    examples = [
        ("is operator with lists", "list1 is list2", list1 is list2,
         "Different objects with same values"),
        ("is operator with same object", "list1 is list3", list1 is list3,
         "Same object in memory"),
        ("is with None", "None is None", None is None,
         "Common use with None checks"),
        ("is not operator", "list1 is not list2", list1 is not list2,
         "Checking if objects are different")
    ]
    
    for op, ex, ans, expl in examples:
        show_example(op, ex, ans, expl)
        input("Press Enter for next example...")
        print()

def learn_membership():
    show_title("Membership Operators in Python")
    
    explain_concept("""Membership operators (in, not in) check if a value exists in a sequence.
They work with lists, tuples, strings, and other Python sequences.
These are very useful for searching and validation.""")
    
    print(Fore.CYAN + "🛒 Shopping List Example:")
    shopping_list = ["apple", "banana", "orange", "milk"]
    search_items = ["apple", "cookie", "milk"]
    
    print(f"Shopping list: {shopping_list}")
    print("Let's check what we need to buy!\n")
    
    for item in search_items:
        result = item in shopping_list
        print(f"Is '{item}' in shopping list? {result}")
        if result:
            print("✓ We have this on our list")
        else:
            print("✗ Not on the list")
        print()
        input("Press Enter to check next item...")
        print()

def learn_bitwise():
    show_title("Bitwise Operators in Python")
    
    explain_concept("""Bitwise operators work with numbers at the binary (bit) level.
They're used in systems programming, file permissions, and optimization.
While less common in everyday Python, they're important for certain tasks.""")
    
    a = 60 
    b = 13  
    
    print(Fore.CYAN + "🔢 Binary representation:")
    print(f"a = {a} (binary: {bin(a)})")
    print(f"b = {b} (binary: {bin(b)})\n")
    
    operations = [
        ("AND (&)", f"{a} & {b}", a & b, "Sets each bit to 1 if both bits are 1"),
        ("OR (|)", f"{a} | {b}", a | b, "Sets each bit to 1 if any bit is 1"),
        ("XOR (^)", f"{a} ^ {b}", a ^ b, "Sets each bit to 1 if exactly one bit is 1"),
        ("NOT (~)", f"~{a}", ~a, "Inverts all the bits"),
        ("Left Shift (<<)", f"{a} << 2", a << 2, "Shifts bits left by 2 positions"),
        ("Right Shift (>>)", f"{a} >> 2", a >> 2, "Shifts bits right by 2 positions")
    ]
    
    for op, ex, ans, expl in operations:
        show_example(op, ex, ans, expl)
        input("Press Enter for next operation...")
        print()

def practice():
    show_title("Interactive Practice")
    
    print(Fore.GREEN + "🎯 Let's practice what you've learned!")
    print("You can try different operators with your own numbers.")
    print("I'll show you the results and explain what's happening.\n")
    
    try:
        num1 = float(input(Fore.CYAN + "Enter first number: "))
        num2 = float(input("Enter second number: " + Fore.RESET))
        print()
        
        print(Fore.YELLOW + "✨ Let's see what we can do with these numbers!")
        
        # Arithmetic
        print("\n📐 Arithmetic Operations:")
        operations = [
            ("Addition", num1 + num2),
            ("Subtraction", num1 - num2),
            ("Multiplication", num1 * num2),
            ("Division", num1 / num2),
            ("Floor Division", num1 // num2),
            ("Modulus", num1 % num2),
            ("Exponentiation", num1 ** 2)
        ]
        
        for op_name, result in operations:
            print(f"{op_name}: {result}")
            input("Press Enter to see next result...")
        
        # Comparisons
        print("\n⚖️ Comparison Results:")
        comparisons = [
            ("Greater than", num1 > num2),
            ("Less than", num1 < num2),
            ("Equal to", num1 == num2),
            ("Not equal to", num1 != num2)
        ]
        
        for comp_name, result in comparisons:
            print(f"{comp_name}: {result}")
            input("Press Enter to see next comparison...")
        
    except ValueError:
        print(Fore.RED + "❌ Please enter valid numbers!" + Fore.RESET)
    except ZeroDivisionError:
        print(Fore.RED + "❌ Can't divide by zero!" + Fore.RESET)
    except Exception as e:
        print(Fore.RED + f"❌ Something went wrong: {e}" + Fore.RESET)
    
    input("\nPress Enter to return to menu...")

def main():
    while True:
        show_title("Welcome to Python Operators Tutorial!")
        
        print(Fore.CYAN + "📚 Choose what you want to learn:")
        topics = [
            "Arithmetic Operators (+, -, *, /, //, %, **)",
            "Assignment Operators (=, +=, -=, etc.)",
            "Comparison Operators (==, !=, >, <, etc.)",
            "Logical Operators (and, or, not)",
            "Identity Operators (is, is not)",
            "Membership Operators (in, not in)",
            "Bitwise Operators (&, |, ^, ~, <<, >>)",
            "Practice with Your Own Numbers",
            "Exit Tutorial"
        ]
        
        for i, topic in enumerate(topics, 1):
            print(f"{i}. {topic}")
        
        print(Fore.RESET)
        choice = input("Enter your choice (1-9): ")
        print()
        
        if choice == "1":
            learn_arithmetic()
        elif choice == "2":
            learn_assignment()
        elif choice == "3":
            learn_comparison()
        elif choice == "4":
            learn_logical()
        elif choice == "5":
            learn_identity()
        elif choice == "6":
            learn_membership()
        elif choice == "7":
            learn_bitwise()
        elif choice == "8":
            practice()
        elif choice == "9":
            print(Fore.YELLOW + "Thanks for learning Python operators! Happy coding! 👋" + Fore.RESET)
            break
        else:
            print(Fore.RED + "❌ Please enter a number between 1 and 9" + Fore.RESET)
        
        input("\nPress Enter to return to main menu...")

if __name__ == "__main__":
    main()
