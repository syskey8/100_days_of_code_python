# debugging
def my_function():
    for i in range(1, 20):
        if i == 20:
            print("You got it") # bug explantion- range is 1 to 19, we can fix by making the upperend 21

my_function()

# Describe the Problem - Write your answers as comments:
# 1. What is the for loop doing?
# 2. When is the function meant to print "You got it"?
# 3. What are your assumptions about the value of i?

from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)
print(dice_images[dice_num]) # bug explantion - randint includes both upper and lower limit so at 6th index we get erorr


# try and catch block
# You can use a try/except block in Python to catch any exceptions that might occur. For example if you imagine there could be a chance of user error. You can prevent it crashing your code by anticipating it. You trap the dangerous code inside a try block and use an except block to catch any potential errors. Then you define what should happen when that error occurs instead of simply just crashing and stopping the code.

try:
    print(6 > "five")
except TypeError:
    print("You can't mix integers and strings in a comparison")

try:
    age = int(input("How old are you?"))
except ValueError:
    print("You have typed an invalid number. Please try again with a numerical resposnse such as 12.")
    age = int(int("How old are you?"))

if age > 18:
    print(f"You can drive at the age {age}.")

# print() is your friend. It can help expose hidden values while your code is running. In a for loop, the loop will follow some rules to perform a repeated block of code











