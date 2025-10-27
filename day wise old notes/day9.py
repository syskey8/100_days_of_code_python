# dictionaries
colours = {
    "apple": "red", 
    "pear": "green", 
    "banana": "yellow"
}

print(colours["pear"]) # output: green

my_empty_dictionary = {} # this is how you create an empty dictionary

colours["peach"] = "pink" # this is how you add new item to dictionary

colours["apple"] = "green" # this is how you can edit the values in a dictionary

for key in colours:
    print(key)  # this is how you loop through a dictionary and print all the keys

for key in colours:
    print(colours[key])  # this is how you loop through a dictionary and print all the values

# nesting a list inside a dictionary

# my_dictionary = {
#     key1: [List],
#     key2: Value,
# }

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}

print(travel_log["France"][1]) # output: Lille

# Nesting lists inside other lists

nested_list = ["A", "B", ["C", "D"]]

print(nested_list[2][1]) # output: D


# Nesting dictionary inside dictionary

# my_dictionary = {
#     key1: Value,
#     key2: {Key: Value, Key: Value},
# }

travel_log = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"], 
    "total_visits": 12
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
    "total_visits": 5
   },
}

print(travel_log["Germany"]["cities_visited"][2]) # output: Stuttgart

