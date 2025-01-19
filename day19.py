# event listener

from  turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)

screen.listen()
screen.onkey(key='space', fun=move_forwards)
screen.exitonclick()

# positional arugments example: my_function(1, 2, 3)
# keyword arguments example: my_function(c=3, a=1, b=2)

# Object: A self-contained entity in programming that bundles data (attributes) and behavior (methods).  
# State: The current values of an object's attributes that define its condition at a specific moment.  
# Instance: A concrete realization of a class, representing a specific object created using the class blueprint.  


