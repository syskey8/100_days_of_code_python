# Notes from "Python Full Course for free 🐍" by Bro Code
# Video URL: https://www.youtube.com/watch?v=ix9cRaBkVe0
# Continued from ~2h 23m

# --- Collections (Lists, Sets, Tuples) ---

# [02:23:05] Collections store multiple values in a single variable.

# List []: Ordered, changeable (mutable), allows duplicate elements.
# [02:23:54] Defined using square brackets [].
fruits_list = ["apple", "orange", "banana", "coconut"]
print(fruits_list) # Output: ['apple', 'orange', 'banana', 'coconut']

# [02:24:50] Access elements using index (starts at 0).
print(fruits_list[0]) # Output: apple
print(fruits_list[1]) # Output: orange

# [02:25:29] Slicing works like strings.
print(fruits_list[0:3]) # Output: ['apple', 'orange', 'banana']
print(fruits_list[::2]) # Output: ['apple', 'banana'] (every second element)
print(fruits_list[::-1]) # Output: ['coconut', 'banana', 'orange', 'apple'] (reversed)

# [02:26:05] Iterating through a list with a for loop.
for fruit in fruits_list:
    print(fruit) # Prints each fruit on a new line

# [02:27:00] dir(list) and help(list) show available methods.
# print(dir(fruits_list))
# help(fruits_list)

# [02:28:12] len() function gets the number of elements.
print(len(fruits_list)) # Output: 4

# [02:28:39] 'in' operator checks for membership.
print("apple" in fruits_list) # Output: True
print("pineapple" in fruits_list) # Output: False

# [02:29:15] Lists are mutable (changeable).
fruits_list[0] = "pineapple" # Change the first element
print(fruits_list) # Output: ['pineapple', 'orange', 'banana', 'coconut']

# [02:29:51] List Methods:
fruits_list.append("apple") # Adds "apple" to the end
print(fruits_list) # Output: ['pineapple', 'orange', 'banana', 'coconut', 'apple']

fruits_list.remove("orange") # Removes the first occurrence of "orange"
print(fruits_list) # Output: ['pineapple', 'banana', 'coconut', 'apple']

fruits_list.insert(0, "kiwi") # Inserts "kiwi" at index 0
print(fruits_list) # Output: ['kiwi', 'pineapple', 'banana', 'coconut', 'apple']

fruits_list.sort() # Sorts the list alphabetically (in-place)
print(fruits_list) # Output: ['apple', 'banana', 'coconut', 'kiwi', 'pineapple']

fruits_list.reverse() # Reverses the order of elements (in-place)
print(fruits_list) # Output: ['pineapple', 'kiwi', 'coconut', 'banana', 'apple']

print(fruits_list.index("banana")) # Returns the index of the first "banana" (Output: 3)
# print(fruits_list.index("grape")) # ValueError if element not found

fruits_list.append("apple")
print(fruits_list.count("apple")) # Counts occurrences of "apple" (Output: 2)

fruits_list.clear() # Removes all elements from the list
print(fruits_list) # Output: []

# Set {}: Unordered, immutable (elements can't be changed), no duplicates. Add/remove is OK.
# [02:32:44] Defined using curly braces {}.
fruits_set = {"apple", "orange", "banana", "coconut"}
print(fruits_set) # Output order may vary (e.g., {'apple', 'banana', 'coconut', 'orange'})

# [02:33:06] No duplicates allowed.
fruits_set_dups = {"apple", "orange", "banana", "coconut", "apple"}
print(fruits_set_dups) # Output: {'apple', 'banana', 'coconut', 'orange'} (duplicate apple ignored)

# [02:34:11] Cannot access elements by index because sets are unordered.
# print(fruits_set[0]) # TypeError: 'set' object is not subscriptable

# [02:34:22] Set Methods:
fruits_set.add("pineapple") # Add an element
print(fruits_set)

fruits_set.remove("banana") # Remove an element (KeyError if not found)
print(fruits_set)

# fruits_set.remove("grape") # KeyError: 'grape'

fruits_set.pop() # Removes and returns an ARBITRARY element
print(fruits_set) # Which element was removed depends on internal order

fruits_set.clear() # Remove all elements
print(fruits_set) # Output: set()

# Tuple (): Ordered, unchangeable (immutable), allows duplicate elements.
# [02:35:46] Defined using parentheses (). Faster than lists.
fruits_tuple = ("apple", "orange", "banana", "coconut", "apple")
print(fruits_tuple) # Output: ('apple', 'orange', 'banana', 'coconut', 'apple')

# [02:36:27] Accessing elements and slicing works like lists.
print(fruits_tuple[1]) # Output: orange
print(fruits_tuple.count("apple")) # Output: 2
print(fruits_tuple.index("banana")) # Output: 2

# [02:35:54] Cannot change elements after creation.
# fruits_tuple[0] = "pineapple" # TypeError: 'tuple' object does not support item assignment

# [02:37:19] Can iterate through tuples.
for fruit in fruits_tuple:
    print(fruit)

# --- 2D Lists & Tuples ---

# [02:45:21] A list (or tuple) containing other lists (or tuples) - like a grid/matrix.

# [02:45:52] Example: List of lists
fruits = ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats = ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meats]
print(groceries)
# Output: [['apple', 'orange', 'banana', 'coconut'], ['celery', 'carrots', 'potatoes'], ['chicken', 'fish', 'turkey']]

# [02:47:55] Accessing elements requires two indices: [row][column].
print(groceries[0][0]) # First list (row 0), first element (col 0) -> Output: apple
print(groceries[1][1]) # Second list (row 1), second element (col 1) -> Output: carrots
print(groceries[2][2]) # Third list (row 2), third element (col 2) -> Output: turkey

# [02:49:11] Can define directly.
groceries_direct = [
    ["apple", "orange", "banana", "coconut"],
    ["celery", "carrots", "potatoes"],
    ["chicken", "fish", "turkey"]
]
print(groceries_direct[0][3]) # Output: coconut

# [02:49:49] Iterating through a 2D list using nested loops.
for category in groceries_direct: # Outer loop iterates through the lists (rows)
    for item in category: # Inner loop iterates through items in the current list (columns)
        print(item, end=" ")
    print() # New line after each category/row

# [02:51:14] 2D Tuples (tuple of tuples) - useful for fixed grids like numpads.
numpad = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
    ("*", 0, "#")
)
print(numpad[3][1]) # Output: 0

for row in numpad:
    for num in row:
        print(num, end=" ")
    print()

# --- Dictionaries ---

# [03:03:28] Collection of {key: value} pairs. Ordered (Python 3.7+), changeable, NO duplicate keys.

# [03:03:59] Defined using curly braces {} with key:value pairs.
capitals = {
    "USA": "Washington D.C.",
    "India": "New Delhi",
    "China": "Beijing",
    "Russia": "Moscow"
}
print(capitals)

# [03:05:24] Accessing values using keys:
# Method 1: Using square brackets [] - KeyError if key doesn't exist.
# print(capitals["USA"]) # Output: Washington D.C.
# print(capitals["Germany"]) # KeyError: 'Germany'

# Method 2: Using .get() method - returns None (or a default value) if key doesn't exist.
print(capitals.get("USA")) # Output: Washington D.C.
print(capitals.get("Germany")) # Output: None
print(capitals.get("Germany", "Key not found")) # Output: Key not found (default value)

# [03:06:05] Checking if a key exists using .get() and an if statement.
if capitals.get("Russia"):
    print("That capital exists.")
else:
    print("That capital doesn't exist.")

# [03:06:56] .update() - Adds new key-value pairs or updates existing ones.
capitals.update({"Germany": "Berlin"}) # Add Germany
print(capitals)
capitals.update({"USA": "Detroit"}) # Update USA's capital
print(capitals)

# [03:07:43] .pop(key) - Removes a key-value pair by key and returns the value.
removed_capital = capitals.pop("China")
print(removed_capital) # Output: Beijing
print(capitals)

# [03:07:52] .popitem() - Removes and returns the LAST inserted key-value pair (in Python 3.7+).
last_item = capitals.popitem()
print(last_item) # Output: ('Germany', 'Berlin') - assuming Germany was last added
print(capitals)

# [03:08:08] .clear() - Removes all items.
# capitals.clear()
# print(capitals) # Output: {}

# [03:08:20] .keys() - Returns a view object containing all keys.
keys = capitals.keys()
print(keys) # Output: dict_keys(['USA', 'India', 'Russia'])
for key in capitals.keys():
    print(key) # Prints each key

# [03:09:23] .values() - Returns a view object containing all values.
values = capitals.values()
print(values) # Output: dict_values(['Detroit', 'New Delhi', 'Moscow'])
for value in capitals.values():
    print(value) # Prints each value

# [03:10:10] .items() - Returns a view object containing all (key, value) tuple pairs.
items = capitals.items()
print(items) # Output: dict_items([('USA', 'Detroit'), ('India', 'New Delhi'), ('Russia', 'Moscow')])
for key, value in capitals.items(): # Can unpack the tuple directly
    print(f"{key}: {value}") # Prints each pair

# --- Random Module ---

# [03:19:42] Used for generating random numbers and making random choices.
import random
# [03:20:02] help(random) shows available functions.
# help(random)

# [03:20:31] random.randint(a, b) - Returns a random integer N such that a <= N <= b (inclusive).
dice_roll = random.randint(1, 6) # Simulates a 6-sided die
print(dice_roll)
random_num = random.randint(1, 100)
print(random_num)

# [03:22:04] random.random() - Returns a random float between 0.0 (inclusive) and 1.0 (exclusive).
random_float = random.random()
print(random_float)

# [03:22:25] random.choice(sequence) - Returns a random element from a non-empty sequence (list, tuple, string).
options = ("rock", "paper", "scissors")
computer_choice = random.choice(options)
print(computer_choice)

# [03:23:17] random.shuffle(list) - Shuffles the elements of a list in-place (modifies the original list).
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
print(f"Original cards: {cards}")
random.shuffle(cards)
print(f"Shuffled cards: {cards}")

# --- Functions ---

# [03:52:12] A block of reusable code. Defined using 'def'.
# [03:53:13] Define a function.
def happy_birthday():
    print("Happy birthday to you!")
    print("Happy birthday to you!")
    print("Happy birthday dear you!")
    print("Happy birthday to you!")

# [03:53:38] Call (invoke) the function.
happy_birthday()

# [03:54:03] Functions with Parameters and Arguments.
# Parameter: Variable listed inside the parentheses in the function definition.
# Argument: Value sent to the function when it is called.
def happy_birthday_name(name, age): # name and age are parameters
    print(f"Happy birthday dear {name}!")
    print(f"You are {age} years old!")

happy_birthday_name("Bro", 20) # "Bro" and 20 are arguments
happy_birthday_name("Steve", 30)
# [03:56:09] Order matters for positional arguments.
# happy_birthday_name(40, "Joe") # Would print "Happy birthday dear 40!" (incorrect)

# [03:58:28] return statement - Sends a result back from the function.
def add(x, y):
    z = x + y
    return z # Send the value of z back

sum_result = add(1, 2) # The value returned by add(1, 2) is stored in sum_result
print(sum_result) # Output: 3

def subtract(x, y):
    return x - y # Can return directly

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print(subtract(1, 2)) # Output: -1
print(multiply(1, 2)) # Output: 2
print(divide(1, 2)) # Output: 0.5

# [04:00:45] Example: Creating a formatted name
def create_name(first, last):
    first = first.capitalize() # Use string methods inside function
    last = last.capitalize()
    return first + " " + last # Return the combined, capitalized string

full_name_func = create_name("spongebob", "squarepants")
print(full_name_func) # Output: Spongebob Squarepants

# --- Default Arguments ---

# [04:02:50] Provide default values for parameters, used if argument is omitted.
# [04:03:14] Example: Calculating net price with optional discount/tax.
def net_price(list_price, discount=0, tax=0.05): # discount and tax have defaults
    return list_price * (1 - discount) * (1 + tax)

# [04:04:54] Calling with only required argument (uses defaults).
ps5_price = net_price(500)
print(f"PS5 Price (defaults): ${ps5_price:.2f}") # Output: $525.00

# [04:05:09] Calling with one default overridden (discount provided).
ps5_discount = net_price(500, 0.10) # 10% discount, default tax
print(f"PS5 Price (10% off): ${ps5_discount:.2f}") # Output: $472.50

# [04:05:43] Calling with all arguments provided.
ps5_no_tax = net_price(500, 0.10, 0) # 10% discount, 0% tax
print(f"PS5 Price (10% off, no tax): ${ps5_no_tax:.2f}") # Output: $450.00

# [04:07:42] Important: Non-default arguments must come BEFORE default arguments in definition.
# def bad_function(a=1, b): # SyntaxError: non-default argument follows default argument
#     pass
def good_function(b, a=1): # Correct order
    pass

# --- Keyword Arguments ---

# [04:08:56] Arguments identified by the parameter name they are assigned to.
# Order doesn't matter, improves readability.

def hello(greeting, title, first, last):
    print(f"{greeting} {title}{first} {last}")

# [04:10:21] Calling with positional arguments (order matters).
hello("Hello", "Mr.", "Spongebob", "Squarepants")

# [04:10:46] Calling with keyword arguments (order doesn't matter).
hello(greeting="Hi", last="Squarepants", first="Spongebob", title="Mr.")
hello(last="Star", title="Mr.", greeting="Hey", first="Patrick")

# [04:11:12] Mixing positional and keyword arguments (positional MUST come first).
hello("Howdy", last="Cheeks", first="Sandy", title="Ms.")
# hello(last="Cheeks", "Howdy", first="Sandy", title="Ms.") # SyntaxError: positional argument follows keyword argument

# [04:12:22] Built-in functions often use keyword arguments (e.g., print()).
print(1, 2, 3, 4, 5) # Default separator is space
print(1, 2, 3, 4, 5, sep="-") # Using 'sep' keyword argument -> Output: 1-2-3-4-5
print("Hello", end="") # Using 'end' keyword argument -> no newline after Hello
print("World") # Output: HelloWorld (on the same line)

# --- Arbitrary Arguments (*args and **kwargs) ---

# [04:15:40] Allow functions to accept a variable number of arguments.

# [04:16:08] *args (Arbitrary Positional Arguments): Packs arguments into a tuple.
# [04:17:10] Conventionally named 'args', but can be any name prefixed with *.
def add_many(*numbers): # Renamed 'args' to 'numbers' for clarity
    print(type(numbers)) # Output: <class 'tuple'>
    total = 0
    for num in numbers:
        total += num
    return total

print(add_many(1, 2, 3)) # Output: 6
print(add_many(10, 20, 30, 40, 50)) # Output: 150
print(add_many(5)) # Output: 5

# [04:18:51] Example: Displaying names with variable parts.
def display_name(*name_parts):
    for part in name_parts:
        print(part, end=" ")
    print()

display_name("Dr.", "Spongebob", "Harold", "Squarepants", "III")
display_name("Patrick", "Star")

# [04:20:16] **kwargs (Arbitrary Keyword Arguments): Packs keyword arguments into a dictionary.
# [04:20:37] Conventionally named 'kwargs'. Must be prefixed with **.
def print_address(**address_parts):
    print(type(address_parts)) # Output: <class 'dict'>
    for key, value in address_parts.items():
        print(f"{key}: {value}")

print_address(street="123 Fake St", city="Bikini Bottom", zip="12345")
print_address(street="124 Conch St", apt="Unit A", city="Bikini Bottom", state="Pacific Ocean", zip="54321")

# [04:23:34] Using *args and **kwargs together. *args must come before **kwargs.
def shipping_label(*name, **address):
    for part in name: # args becomes a tuple named 'name'
        print(part, end=" ")
    print()
    if 'apt' in address: # kwargs becomes a dict named 'address'
        print(f"{address.get('street')} {address.get('apt')}")
    elif 'pobox' in address:
         print(f"{address.get('street')}")
         print(f"{address.get('pobox')}")
    else:
        print(f"{address.get('street')}")

    print(f"{address.get('city')}, {address.get('state')} {address.get('zip')}")

shipping_label("Mr.", "Squidward", "Tentacles",
               street="126 Conch St",
               city="Bikini Bottom",
               state="Pacific Ocean",
               zip="54321")

shipping_label("Sandy", "Cheeks",
               street="1 Tree Dome St",
               apt="Main Dome",
               city="Bikini Bottom",
               state="Pacific Ocean",
               zip="98765")

# --- End of Notes (Approx. first 4h 32m of video) ---