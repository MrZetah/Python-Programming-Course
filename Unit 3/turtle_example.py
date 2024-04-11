import turtle

# Create a turtle object
pen = turtle.Turtle()

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Set the turtle color and shape
pen.color("blue")
pen.shape("turtle")

# Set the speed of the turtle
pen.speed(2)

# Draw a square
for i in range(4):
    pen.forward(100)
    pen.left(90)

# Move the turtle to a new position
pen.penup()
pen.goto(150, 0)
pen.pendown()

# Set the fill color
pen.fillcolor("yellow")

# Begin filling a shape
pen.begin_fill()

# Draw a triangle
for _ in range(3):
    pen.forward(100)
    pen.left(120)

# End filling the shape
pen.end_fill()

# Move the turtle to a new position
pen.penup()
pen.goto(-150, -150)
pen.pendown()

# Set the pen color
pen.color("red")

# Draw a circle
pen.circle(100)

# Close the turtle graphics window when clicked
turtle.done()

