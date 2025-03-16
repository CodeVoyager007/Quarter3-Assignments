# 1. Comparison Operators Example
a = 15
b = 25

print("a == b:", a == b)  
print("a != b:", a != b)  
print("a > b:", a > b)   
print("a < b:", a < b)   
print("a >= b:", a >= b) 
print("a <= b:", a <= b) 

# 2. Logical Operators Example
is_raining = True
have_umbrella = False

if is_raining and have_umbrella:
    print("You can go outside without getting wet.")
elif is_raining or have_umbrella:
    print("You might get a little wet.")
else:
    print("The weather is clear.")

# 3. if Statement Example
temperature = 30

if temperature > 25:
    print("It's a hot day, drink lots of water!")

# 4. else Statement Example
age = 17

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")

# 5. elif Statement Example
marks = 85

if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: F")

# 6. Nested if Statement Example
number = -8

if number >= 0:
    if number % 2 == 0:
        print("The number is even and positive.")
    else:
        print("The number is odd and positive.")
else:
    print("The number is negative.")

# 7. Practical Example: Discount System
age = int(input("Enter your age: "))
is_student = input("Are you a student? (yes/no): ").lower() == "yes"

if age < 12 or age > 60:
    print("You qualify for a special discount.")
elif age >= 12 and is_student:
    print("You get a student discount.")
else:
    print("No discount available.")
