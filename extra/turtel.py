import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create the turtle
t = turtle.Turtle()
t.speed(500)
t.hideturtle()

colors = ["red", "yellow", "blue", "green", "purple", "orange"]

# Draw many spirals rotated around the center
for angle in range(0, 360, 10):
    t.penup()
    t.goto(0, 0)      # Return to center
    t.setheading(angle)  # Rotate starting direction
    t.pendown()

    for x in range(120):
        t.pencolor(colors[x % 6])
        t.width(x / 20 + 1)
        t.forward(x * 2)
        t.left(59)

turtle.done()