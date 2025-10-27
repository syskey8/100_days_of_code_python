
# function

def greet():
    print("Hello")
    print("How do you do?")
    print("Isn't the weather nice?")

greet()

# function with parameters
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")

greet_with_name("Angela") # output name will be replace with Angela

# function with more than one input

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

greet_with("tanmay", "london")
greet_with(location="dallas", name="tanmay")

sample_text = "hello world"
character_to_count = 'o'
count = sample_text.count(character_to_count)
print(count)
