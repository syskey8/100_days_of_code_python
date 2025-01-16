# Introduction to OOP (Object - Oriented Programming)

# Atriutes - are the characteristics of an object
# Methods - are the actions that an object can perform
# Objects - are the instances of a class

# car = CarBluePrint() # Object of the class CarBluePrint

import turtle # this is an inbuilt module in python

timmy = turtle.Turtle() # Object timmy of the class Turtle
print(timmy)
timmy.shape("turtle") # method to change the shape of the turtle
timmy.color("chartreuse3") # method to change the color of the turtle
timmy.forward(100) # method to move the turtle forward

my_screen = turtle.Screen() # Object my_screen of the class Screen
print(my_screen.canvheight) # will output the height of the screen, canvheight is an attribute of the class Screen

my_screen.exitonclick() # will close the screen when clicked, this is a method of the class Screen

# pypi.org - python package index is a website where you can find prebuilt python packages

import prettytable

table = prettytable.PrettyTable() # created object tabel of teh class PrettyTable

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"]) # method to add a column to the table

table.add_column("Type", ["Electric", "Water", "Fire"]) # method to add a column to the table

table.align = "l" # method to align the text to the left

print(table)

