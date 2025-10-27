# scope of variable 

enemies = 1 # global scope

def increase_enemies():
    enemies = 2 # local scope 
    print(f"enemies inside function: {enemies}") # enemies = 2

increase_enemies()
print(f"enemies outside function: {enemies}") # enemies = 1

# Accessible anywhere
my_global_var = 1

def my_function():
    # Only accessible within my_function()
    my_local_var = 2
    
for _ in range(10):
    # Accessible anywhere
    my_block_var = 3


# Modifying Global Scope

enemies = 1


def increase_enemies():
    global enemies # we have to mention it explicity to get access to the global variable

    enemies += 1
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

# You can define global constants in your code file for easy access. Their job is meant to be "set and forget" so you can use their values but never need to mofy them.

# Naming Convention
# Global constants are normally declared in ALL_CAPS with a underscore in between.

PI = 3.14159
GOOGLE_URL = "https://www.google.com"