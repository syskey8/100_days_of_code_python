# Notes from "Python Full Course for free 🐍" by Bro Code
# Video URL: https://www.youtube.com/watch?v=ix9cRaBkVe0

# --- Introduction & Setup ---

# [00:00:50] Need to download Python interpreter (python.org) and an IDE.
# [00:01:10] During Python install (Windows), check "Add Python exe to Path".
# [00:01:30] IDE choices: PyCharm (beginner-friendly) or VS Code (requires Python extension).
# [00:02:00] PyCharm Community Edition is free.
# [00:03:03] Creating a new project and Python file (e.g., main.py).

# --- Basic Output & Comments ---

# [00:03:50] The print() function displays output to the console.
print("I like pizza") # Prints the string "I like pizza"
print("It's really good") # Prints another line

# [00:05:02] Comments start with '#' and are ignored by the interpreter.
# Comments are used for notes.
# This is a comment.

# --- Variables & Data Types ---

# [00:05:49] A variable is a container for a value.

# String (str): A series of characters (text). Use single or double quotes.
first_name = "Bro" # Assigning the string "Bro" to the variable first_name
food = 'pizza' # Single quotes also work for strings
email = "bro123@fake.com"
print(first_name) # Output: Bro

# [00:07:02] F-strings (Formatted String Literals) easily embed variables in strings.
print(f"Hello {first_name}") # Output: Hello Bro
print(f"You like {food}") # Output: You like pizza
print(f"Your email is {email}") # Output: Your email is bro123@fake.com

# Integer (int): Whole numbers (no decimals).
age = 25 # Assigning the integer 25
quantity = 3 # Assigning the integer 3
num_of_students = 30
print(f"You are {age} years old") # Output: You are 25 years old
print(f"You are buying {quantity} items") # Output: You are buying 3 items
print(f"Your class has {num_of_students} students") # Output: Your class has 30 students

# Float (float): Numbers with a decimal point.
price = 10.99 # Assigning the float 10.99
gpa = 3.2 # Assigning the float 3.2
distance = 5.5
print(f"The price is ${price}") # Output: The price is $10.99
print(f"Your GPA is {gpa}") # Output: Your GPA is 3.2
print(f"You ran {distance} km") # Output: You ran 5.5 km

# Boolean (bool): Represents True or False. Note the capital T and F.
is_student = True # Assigning the boolean True
for_sale = False # Assigning the boolean False
is_online = True
print(f"Are you a student? {is_student}") # Output: Are you a student? True

# [00:13:12] Booleans are often used in conditional logic (if statements).
if is_student:
    print("You are a student") # This will print because is_student is True
else:
    print("You are not a student")

if for_sale:
    print("Item is for sale")
else:
    print("Item is not available") # This will print

if is_online:
    print("You are online") # This will print
else:
    print("You are offline")

# --- Type Casting ---

# [00:16:05] Type casting converts a variable from one data type to another.

name_tc = "Bro"
age_tc = 21
gpa_tc = 3.2
student_tc = True

# [00:16:47] The type() function shows the data type of a variable.
print(type(name_tc)) # Output: <class 'str'>
print(type(age_tc)) # Output: <class 'int'>
print(type(gpa_tc)) # Output: <class 'float'>
print(type(student_tc)) # Output: <class 'bool'>

# Convert to integer using int()
gpa_int = int(gpa_tc)
print(gpa_int) # Output: 3 (decimal part is truncated)

# Convert to float using float()
age_float = float(age_tc)
print(age_float) # Output: 21.0

# Convert to string using str()
age_str = str(age_tc)
print(age_str) # Output: '21' (looks the same, but it's a string)
print(type(age_str)) # Output: <class 'str'>

# [00:19:09] Converting numbers to strings changes arithmetic behavior.
# print(age_str + 1) # This would cause a TypeError
print(age_str + "1") # String concatenation: Output: 211

# Convert to boolean using bool()
# [00:20:07] Non-empty strings convert to True, empty strings convert to False.
name_bool = bool(name_tc)
print(name_bool) # Output: True
empty_str_bool = bool("")
print(empty_str_bool) # Output: False

# [00:20:31] Zero converts to False, non-zero numbers convert to True.
age_bool = bool(age_tc) # age_tc is 21
print(age_bool) # Output: True
zero_bool = bool(0)
print(zero_bool) # Output: False

# --- User Input ---

# [00:21:15] The input() function gets input from the user (always returns a string).
# user_name = input("What is your name? ") # Prompts user and stores input in user_name
# print(f"Hello {user_name}")

# [00:22:55] Input must often be type cast if you need a number.
# user_age_str = input("How old are you? ")
# user_age_int = int(user_age_str) # Convert the input string to an integer
# print(f"You are {user_age_int} years old")
# user_age_int += 1 # Can now perform math operations
# print(f"Next year, you will be {user_age_int}")

# [00:25:29] Can type cast directly during input.
# user_age = int(input("How old are you? ")) # Gets input and converts to int immediately
# print(f"You are {user_age} years old")

# [00:26:11] Example: Area of a rectangle
# length = float(input("Enter the length: ")) # Using float for potential decimals
# width = float(input("Enter the width: "))
# area = length * width
# print(f"The area is {area} cm²") # Using ² (alt+0178 on Windows numpad)

# [00:29:18] Example: Shopping cart
# item = input("What item would you like to buy? ")
# price_item = float(input(f"What is the price of a {item}? $"))
# quantity_item = int(input(f"How many {item}s would you like? "))
# total_cost = price_item * quantity_item
# print(f"You have bought {quantity_item} x {item}/s")
# print(f"Your total is ${total_cost:.2f}") # Using format specifier for 2 decimal places

# --- Basic Math Operations ---

# [00:38:19] Arithmetic Operators
friends = 0
friends = friends + 1 # Addition
print(friends) # Output: 1

# [00:38:59] Augmented Assignment Operators (shorthand)
friends += 1 # Same as friends = friends + 1
print(friends) # Output: 2
friends -= 2 # Subtraction (friends = friends - 2)
print(friends) # Output: 0
friends = 5
friends *= 3 # Multiplication (friends = friends * 3)
print(friends) # Output: 15
friends /= 2 # Division (always results in a float)
print(friends) # Output: 7.5
friends = 5
friends **= 2 # Exponentiation (friends = friends ** 2)
print(friends) # Output: 25

# [00:41:04] Modulus Operator (%) - gives the remainder of division.
remainder = 10 % 3 # 10 divided by 3 is 3 with a remainder of 1
print(remainder) # Output: 1
remainder_even = 10 % 2 # 10 divided by 2 has no remainder
print(remainder_even) # Output: 0 (Useful for checking even/odd)

# --- Built-in Math Functions ---

x_math = 3.14
y_math = -4
z_math = 5

# [00:42:39] round() - rounds to the nearest integer or specified decimal places.
print(round(x_math)) # Output: 3
print(round(3.9)) # Output: 4
print(round(3.14159, 2)) # Output: 3.14 (rounds to 2 decimal places)

# [00:43:07] abs() - returns the absolute (positive) value.
print(abs(y_math)) # Output: 4

# [00:43:37] pow(base, exponent) - raises base to the power of exponent.
print(pow(4, 3)) # 4 * 4 * 4 = 64

# [00:44:06] max() - returns the largest among the arguments.
print(max(x_math, y_math, z_math)) # Output: 5

# [00:44:32] min() - returns the smallest among the arguments.
print(min(x_math, y_math, z_math)) # Output: -4

# --- Math Module ---

# [00:44:40] Need to import the math module for more advanced functions/constants.
import math

# [00:44:55] math.pi - constant for Pi.
print(math.pi) # Output: 3.141592653589793

# [00:45:15] math.e - constant for Euler's number.
print(math.e) # Output: 2.718281828459045

# [00:45:29] math.sqrt() - returns the square root.
print(math.sqrt(9)) # Output: 3.0

# [00:46:02] math.ceil() - rounds a number UP to the nearest integer.
print(math.ceil(9.1)) # Output: 10

# [00:46:28] math.floor() - rounds a number DOWN to the nearest integer.
print(math.floor(9.9)) # Output: 9

# --- If Statements ---

# [00:51:47] if statements execute code only if a condition is True.

# age_if = int(input("Enter your age: "))
age_if = 21 # Example age

# [00:52:33] Basic if statement with comparison operators (>, >=, <, <=, ==, !=)
if age_if >= 18:
    print("You are an adult.") # Executes if age_if is 18 or greater

# [00:53:28] if-else statement
if age_if >= 18:
    print("You are an adult.")
else:
    print("You are a minor.") # Executes if the 'if' condition is False

# [00:54:10] if-elif-else statement (elif means "else if")
if age_if < 0:
    print("You haven't been born yet!")
elif age_if >= 100:
    print("You are too old!")
elif age_if >= 18:
    print("You are an adult.")
else: # Executes if none of the above conditions are True
    print("You are a minor.")

# [00:56:11] Checking string equality (==)
# response = input("Would you like food? (Y/N): ")
response = "Y" # Example response
if response == "Y":
    print("Have some food!")
elif response == "N":
    print("No food for you.")
else:
    print("Invalid response.")

# [00:57:34] Checking for an empty string
# name_if = input("Enter your name: ")
name_if = "" # Example empty input
if name_if == "":
    print("You did not type in your name!")
else:
    print(f"Hello {name_if}")

# [00:58:27] Using booleans directly in if statements
for_sale_if = True
if for_sale_if: # Same as 'if for_sale_if == True:'
    print("This item is for sale.")
else:
    print("This item is NOT for sale.")

online_if = False
if online_if:
    print("User is online.")
else: # Executes because online_if is False
    print("User is offline.")

# --- Logical Operators ---

# [01:13:58] Logical operators combine multiple conditions.

temp = 25
is_raining_log = False
is_sunny_log = True

# [01:14:06] or: True if AT LEAST ONE condition is True.
if temp > 35 or temp < 0 or is_raining_log:
    print("Event cancelled due to weather.")
else:
    print("Event is still scheduled.") # This will print

# [01:16:33] and: True only if BOTH conditions are True.
if temp >= 28 and is_sunny_log:
    print("It is hot AND sunny outside.")
elif temp < 28 and temp > 0 and is_sunny_log:
    print("It is warm AND sunny outside.") # This will print (25 is between 0 and 28)
elif temp <= 0 and is_sunny_log:
    print("It is cold AND sunny outside.")

# [01:18:59] Chained comparison shortcut (Python specific)
if 0 < temp < 28 and is_sunny_log: # Equivalent to temp > 0 and temp < 28 and is_sunny_log
     print("(Chained) It is warm AND sunny outside.") # This will also print

# [01:19:37] not: Inverts a boolean value (True becomes False, False becomes True).
if not is_sunny_log: # Checks if is_sunny_log is False
    print("It is cloudy.")
else:
    print("It is sunny.") # This will print because is_sunny_log is True

if not is_raining_log: # Checks if is_raining_log is False
    print("It is NOT raining.") # This will print because is_raining_log is False
else:
    print("It is raining.")

# --- Conditional Expressions (Ternary Operator) ---

# [01:21:28] A concise way to write simple if-else statements in one line.
# Format: value_if_true if condition else value_if_false

num_cond = 6
status_cond = "adult" if age_if >= 18 else "child"
print(status_cond) # Output: adult

result_cond = "Even" if num_cond % 2 == 0 else "Odd"
print(result_cond) # Output: Even

print("Positive" if num_cond > 0 else "Negative or Zero") # Output: Positive

# --- String Methods ---

# [01:27:03] Methods are functions associated with an object (like a string).

full_name = input("Enter your full name: ") # Example: "Bro Code"

# [01:27:30] len() function (not a method, but commonly used with strings) - gets length.
name_length = len(full_name)
print(f"Your name has {name_length} characters.") # Output: Your name has 8 characters. (includes space)

# [01:28:15] .find() method - finds the first index of a character/substring. Returns -1 if not found.
space_index = full_name.find(" ")
print(f"The first space is at index: {space_index}") # Output: The first space is at index: 3
o_index = full_name.find("o")
print(f"The first 'o' is at index: {o_index}") # Output: The first 'o' is at index: 2
q_index = full_name.find("q")
print(f"The first 'q' is at index: {q_index}") # Output: The first 'q' is at index: -1

# [01:29:20] .rfind() method - finds the last index of a character/substring.
last_o_index = full_name.rfind("o")
print(f"The last 'o' is at index: {last_o_index}") # Output: The last 'o' is at index: 5

# [01:30:00] .capitalize() method - capitalizes the first character of the string.
print(full_name.lower().capitalize()) # Example: "bro code" -> "Bro code"

# [01:30:34] .upper() method - converts the entire string to uppercase.
print(full_name.upper()) # Output: BRO CODE

# [01:30:54] .lower() method - converts the entire string to lowercase.
print(full_name.lower()) # Output: bro code

# [01:31:06] .isdigit() method - returns True if all characters are digits, False otherwise.
print("12345".isdigit()) # Output: True
print("Bro123".isdigit()) # Output: False
print(full_name.isdigit()) # Output: False

# [01:31:54] .isalpha() method - returns True if all characters are alphabetic (and no spaces!), False otherwise.
print("BroCode".isalpha()) # Output: True
print("Bro Code".isalpha()) # Output: False (because of the space)
print("Bro123".isalpha()) # Output: False

# [01:32:51] .count() method - counts occurrences of a character/substring.
phone_number = "123-456-7890"
dash_count = phone_number.count("-")
print(f"Number of dashes: {dash_count}") # Output: Number of dashes: 2

# [01:33:43] .replace(old, new) method - replaces all occurrences of 'old' with 'new'.
phone_no_dashes = phone_number.replace("-", "") # Replace dashes with empty string
print(phone_no_dashes) # Output: 1234567890
phone_with_spaces = phone_number.replace("-", " ") # Replace dashes with spaces
print(phone_with_spaces) # Output: 123 456 7890

# [01:34:41] help(str) - shows documentation for string methods.
# help(str) # Uncomment to see the help information

# --- String Indexing & Slicing ---

# [01:39:09] Access individual characters or parts of a string.
credit_number = "1234-5678-9012-3456"

# [01:39:54] Accessing single characters (index starts at 0).
first_digit = credit_number[0]
print(first_digit) # Output: 1
second_digit = credit_number[1]
print(second_digit) # Output: 2
fifth_char = credit_number[4] # This is the first dash
print(fifth_char) # Output: -

# [01:40:46] Slicing [start:end] - gets a substring (end index is exclusive).
first_four = credit_number[0:4] # Gets characters from index 0 up to (but not including) 4
print(first_four) # Output: 1234
# [01:41:37] Omitting start defaults to 0.
also_first_four = credit_number[:4]
print(also_first_four) # Output: 1234

# [01:41:54] Slicing example
second_group = credit_number[5:9] # Indices 5, 6, 7, 8
print(second_group) # Output: 5678

# [01:42:35] Omitting end defaults to the end of the string.
from_fifth_on = credit_number[5:]
print(from_fifth_on) # Output: 678-9012-3456

# [01:42:55] Negative indexing - counts from the end (-1 is the last character).
last_digit = credit_number[-1]
print(last_digit) # Output: 6
second_last_digit = credit_number[-2]
print(second_last_digit) # Output: 5

# [01:44:35] Slicing with negative indices
last_four = credit_number[-4:] # Last 4 characters
print(last_four) # Output: 3456

# [01:43:34] Slicing with a step [start:end:step].
every_second_char = credit_number[::2] # Get every 2nd character from start to end
print(every_second_char) # Output: 13-68-02-46

# [01:45:42] Reversing a string using step -1.
reversed_credit_number = credit_number[::-1]
print(reversed_credit_number) # Output: 6543-2109-8765-4321

# --- Format Specifiers (within F-strings) ---

# [01:46:36] Control how values are formatted inside f-string placeholders {value:flags}.

price1 = 3141.59
price2 = -987.65
price3 = 12.3

# [01:48:09] Decimal point precision (.nf) - specify 'n' decimal places for floats.
print(f"Price 1: ${price1:.2f}") # Output: Price 1: $3141.59
print(f"Price 2: ${price2:.2f}") # Output: Price 2: $-987.65
print(f"Price 3: ${price3:.3f}") # Output: Price 3: $12.300 (adds trailing zeros)

# [01:49:18] Allocating space (:n) - reserves 'n' spaces (right-aligned by default).
print(f"Price 1: ${price1:10.2f}") # Reserves 10 spaces total for the number
print(f"Price 2: ${price2:10.2f}")
print(f"Price 3: ${price3:10.2f}")

# [01:49:59] Alignment (< left, > right, ^ center) within allocated space.
print(f"Price 1: ${price1:<10.2f}") # Left-align within 10 spaces
print(f"Price 2: ${price2:^10.2f}") # Center-align within 10 spaces
print(f"Price 3: ${price3:>10.2f}") # Right-align (default)

# [01:49:37] Zero padding (:0n) - pads with leading zeros within allocated space.
print(f"Price 1: ${price1:010.2f}") # Pad with zeros to fill 10 spaces
print(f"Price 3: ${price3:010.2f}")

# [01:50:29] Show plus sign for positive numbers (:+).
print(f"Price 1: ${price1:+.2f}") # Output: Price 1: $+3141.59
print(f"Price 2: ${price2:+.2f}") # Output: Price 2: $-987.65

# [01:50:43] Add space for positive numbers, minus for negative (: ).
print(f"Price 1: ${price1: .2f}") # Output: Price 1: $ 3141.59 (leading space)
print(f"Price 2: ${price2: .2f}") # Output: Price 2: $-987.65

# [01:50:52] Thousand separator (:,).
print(f"Price 1: ${price1:,.2f}") # Output: Price 1: $3,141.59
print(f"Price 2: ${price2:,.2f}") # Output: Price 2: $-987.65

# [01:51:11] Combining flags.
print(f"Price 1: ${price1:+,.2f}") # Show sign, use comma, 2 decimals
print(f"Price 2: ${price2:+,.2f}")

# --- While Loops ---

# [01:51:57] Executes code repeatedly as long as a condition is True.

# [01:52:05] Example: Input validation - keep asking until valid input is given.
# while True: # Example of potentially infinite loop (needs a break)
#     name_while = input("Enter your name: ")
#     if name_while != "":
#         break # Exit the loop if name is not empty
# print(f"Hello {name_while}")

# [01:53:15] More refined example
# name_while = ""
# while name_while == "":
#     name_while = input("Enter your name: ")
# print(f"Hello {name_while}")

# [01:54:21] Example: Age validation
# age_while = int(input("Enter your age: "))
# while age_while < 0:
#     print("Age can't be negative!")
#     age_while = int(input("Enter your age: "))
# print(f"You are {age_while} years old.")

# [01:55:39] Example: Loop until user quits
# food_while = ""
# while food_while.lower() != "q":
#     food_while = input("Enter a food you like (q to quit): ")
#     if food_while.lower() != "q":
#         print(f"You like {food_while}")
# print("Bye!")

# [01:57:10] Example: Number range validation
# num_while = 0
# while num_while < 1 or num_while > 10:
#     num_while = int(input("Enter a number between 1-10: "))
#     if num_while < 1 or num_while > 10:
#         print(f"{num_while} is not valid.")
# print(f"Your number is {num_while}.")

# --- For Loops ---

# [02:06:28] Executes a block of code a fixed number of times (iterates over a sequence).

# [02:06:58] Iterating over a range() of numbers.
# range(start, stop, step) - 'stop' is exclusive.
for i in range(1, 11): # Numbers 1 through 10
    print(i, end=" ") # Output: 1 2 3 4 5 6 7 8 9 10
print() # New line

# [02:08:06] Counting backwards using reversed().
for i in reversed(range(1, 11)):
    print(i, end=" ") # Output: 10 9 8 7 6 5 4 3 2 1
print("\nHappy New Year!")

# [02:08:47] Using a step in range().
for i in range(1, 11, 2): # Count by 2s (1, 3, 5, 7, 9)
    print(i, end=" ") # Output: 1 3 5 7 9
print()

# [02:09:15] Iterating over a string.
credit_card_for = "1234-5678-9012-3456"
for char in credit_card_for:
    print(char) # Prints each character on a new line

# [02:09:57] Control flow keywords in loops: continue and break.

# [02:10:03] continue - skips the rest of the current iteration and moves to the next.
for i in range(1, 21):
    if i == 13:
        continue # Skip printing 13
    print(i, end=" ") # Output: 1..12 14..20
print()

# [02:10:50] break - exits the loop entirely.
for i in range(1, 21):
    if i == 13:
        break # Stop the loop when i is 13
    print(i, end=" ") # Output: 1 2 3 4 5 6 7 8 9 10 11 12
print()

# --- Nested Loops ---

# [02:17:29] A loop inside another loop.

# [02:19:16] Example: Printing a grid pattern.
rows = 3
cols = 9
for r in range(rows): # Outer loop (for rows)
    for c in range(cols): # Inner loop (for columns)
        print(c + 1, end="") # Print column number (1-9)
    print() # New line after each row finishes

# Output:
# 123456789
# 123456789
# 123456789

# [02:21:03] Example: Printing a rectangle of symbols.
# rect_rows = int(input("Enter rows: "))
# rect_cols = int(input("Enter columns: "))
# rect_symbol = input("Enter symbol: ")

# for r in range(rect_rows):
#     for c in range(rect_cols):
#         print(rect_symbol, end="")
#     print()

# --- End of Notes (Approx. first 2h 23m of video) ---