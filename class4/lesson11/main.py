#lesson 11
# 1. Time Module Examples
print("1. Time Module Examples:")
import time

# Get current time in ticks (seconds since epoch)
ticks = time.time()
print(f"Seconds since epoch: {ticks}")

# Get local time
localtime = time.localtime(time.time())
print(f"Local time tuple: {localtime}")

# Get formatted time
formatted_time = time.asctime(time.localtime(time.time()))
print(f"Formatted local time: {formatted_time}")
print()

# 2. Calendar Module Examples
print("2. Calendar Module Examples:")
import calendar

# Get calendar for a specific month
cal = calendar.month(2025, 1)
print("Calendar for January 2025:")
print(cal)
print()

# 3. DateTime Module Examples
print("3. DateTime Module Examples:")
from datetime import date, datetime

# Create specific dates
date1 = date(2023, 4, 19)
date2 = date(2023, 4, 30)
print(f"Date 1: {date1}")
print(f"Date 2: {date2}")

# Get current date and time
current_time = datetime.now()
print(f"Current date and time: {current_time}")
print()

# 4. strftime() Method Examples
print("4. strftime() Method Examples:")
x = datetime(2025, 1, 1)
print(f"Microsecond: {x.strftime('%f')}")
print(f"Day name: {x.strftime('%A')}")
print(f"Year: {x.strftime('%Y')}")
print(f"Month name: {x.strftime('%B')}")
print()

# 5. Math Module Examples
print("5. Math Module Examples:")
import math

# Basic math functions
print(f"Absolute value of -5: {abs(-5)}")
print(f"2 raised to power 3: {pow(2, 3)}")
print(f"3.14159 rounded to 2 decimals: {round(3.14159, 2)}")
print(f"Maximum of 1,2,3,4,5: {max(1,2,3,4,5)}")
print(f"Minimum of 1,2,3,4,5: {min(1,2,3,4,5)}")
print()

# Trigonometric functions
print("Trigonometric Functions:")
print(f"sin(π/2): {math.sin(math.pi/2)}")
print(f"cos(0): {math.cos(0)}")
print(f"tan(π/4): {math.tan(math.pi/4)}")
print()

# Other math functions
print("Other Math Functions:")
print(f"Square root of 9: {math.sqrt(9)}")
print(f"Factorial of 5: {math.factorial(5)}")
print(f"Natural log of 10: {math.log(10)}")
print(f"Base-10 log of 100: {math.log10(100)}")
print(f"e raised to power 2: {math.exp(2)}")
print()

# Math constants
print("Math Constants:")
print(f"Pi (π): {math.pi}")
print(f"Euler's number (e): {math.e}")
print(f"Tau (τ): {math.tau}")
print()

# 6. NaN and Infinity Examples
print("6. NaN and Infinity Examples:")

# NaN examples
nan_value = float('nan')
print(f"NaN value: {nan_value}")
print(f"Is NaN: {math.isnan(nan_value)}")
print(f"NaN == NaN: {nan_value == float('nan')}")

# Infinity examples
infinity = math.inf
print(f"Positive infinity: {infinity}")
print(f"Infinity > 999999: {infinity > 999999}")
print(f"Infinity * 2: {infinity * 2}")
print(f"Infinity - Infinity: {infinity - infinity}")  # Results in NaN
print()

# 7. Date Arithmetic Example
print("7. Date Arithmetic Example:")
from datetime import timedelta

# Add days to a date
future_date = date1 + timedelta(days=10)
print(f"Date1 + 10 days: {future_date}")

# Calculate difference between dates
date_diff = date2 - date1
print(f"Days between date2 and date1: {date_diff.days}")
print()

# 8. Time Formatting Examples
print("8. Time Formatting Examples:")
now = datetime.now()
print(f"Current time in 12-hour format: {now.strftime('%I:%M %p')}")
print(f"Current date in different formats:")
print(f"  YYYY-MM-DD: {now.strftime('%Y-%m-%d')}")
print(f"  DD/MM/YYYY: {now.strftime('%d/%m/%Y')}")
print(f"  Month Day, Year: {now.strftime('%B %d, %Y')}")
print()

# 9. Calendar Operations
print("9. Calendar Operations:")
# Check if a year is leap year
print(f"Is 2024 a leap year? {calendar.isleap(2024)}")

# Get weekday of first day of month
print(f"First day of January 2025 is: {calendar.weekday(2025, 1, 1)}")
print()

# 10. Math Module Advanced Examples
print("10. Math Module Advanced Examples:")
# Convert degrees to radians
degrees = 45
radians = math.radians(degrees)
print(f"{degrees} degrees = {radians} radians")

# Calculate hypotenuse
a, b = 3, 4
hypotenuse = math.hypot(a, b)
print(f"Hypotenuse of triangle with sides {a} and {b}: {hypotenuse}")

# Calculate greatest common divisor
print(f"GCD of 48 and 18: {math.gcd(48, 18)}")
