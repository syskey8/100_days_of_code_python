from turtle import Turtle, Screen
import random

timmy_the_turtle = Turtle()
screen = Screen()

# challenge 1: draw a square

timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")

timmy_the_turtle.left(90)
timmy_the_turtle.forward(100)
timmy_the_turtle.right(90)
timmy_the_turtle.forward(100)
timmy_the_turtle.right(90)
timmy_the_turtle.forward(100)
timmy_the_turtle.right(90)
timmy_the_turtle.forward(100)

# challenge 2: draw a dashed line
for i in range(10):
    timmy_the_turtle.penup()
    timmy_the_turtle.forward(10)
    timmy_the_turtle.pendown()
    timmy_the_turtle.forward(10)

# challenge 3: draw different shapes

# triangle
for i in range (3):
    timmy_the_turtle.right(120)
    timmy_the_turtle.forward(100)

# square
for i in range(4):
    timmy_the_turtle.right(90)
    timmy_the_turtle.forward(100)

# pentagon
for i in range(5):
    timmy_the_turtle.right(72)
    timmy_the_turtle.forward(100)

# hexagon
for i in range(6):
    timmy_the_turtle.right(60)
    timmy_the_turtle.forward(100)

# pentagon
for i in range(8):
    timmy_the_turtle.right(45)
    timmy_the_turtle.forward(100)

# challege 4: random walk
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
timmy_the_turtle.pensize(15)
timmy_the_turtle.speed("fastest")

for _ in range(50):
    timmy_the_turtle.color(random.choice(colours))
    timmy_the_turtle.forward(30)
    timmy_the_turtle.setheading(random.choice(directions))

# challenge 5: spirograph
screen.colormode(255)
timmy_the_turtle.pensize(1)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy_the_turtle.color(random_color())
        timmy_the_turtle.circle(100)
        timmy_the_turtle.setheading(timmy_the_turtle.heading() + size_of_gap)

draw_spirograph(5)
screen.exitonclick()
