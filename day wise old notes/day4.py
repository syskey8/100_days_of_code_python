# Randomization
import random

#import module
import my_module

random_integer = random.randint(1, 10) # picks a random value between the given two numbers, it is inclusive of 1 and 10
print(random_integer) # prints the variable which is a random int

# module - module in Python is just a file that contains Python code. It helps you organize your code by grouping related functions, classes, and variables into one place.
# create a different file named, my_module and import it to use it
print(my_module.my_favourite_number) #prints the value from the module

random_number_0_to_1 = random.random() # generates a number between 0.0 <= X < 1.0
print(random_number_0_to_1)

# Heads or Tails game
coin = random.randint(0, 1)
if coin == 0:
    print("heads")
else:
    print("tails")

# Lists
fruits = ["Cherry", "Mango", "Apple"]
print(fruits[2]) #prints Apple
fruits[2] = "Banana" # changes the item in the list at index 2 to banana
fruits.append("Watermelon") # add an item to the end of the list
 
# there are many functions as such which are not to be remembered but should be known, refer docs

# Banker Roulette
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
payer = random.randint(0, 4)
print(friends[payer])

print(random.choice(friends)) # does the same job but in a easy fashion

example = [fruits, friends]
print(example) # it will print both list one after the other
