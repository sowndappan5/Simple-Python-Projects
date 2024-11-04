# Import the turtle graphics package
import turtle

# Create a screen object for the drawing area
screen = turtle.Screen()

# Create a turtle object to draw
drawer = turtle.Turtle()

# Function to draw a semicircle with specified color, radius, and position offset
def draw_semi_circle(color, radius, offset):

    # Set the pen color for the semicircle
    drawer.color(color)

    # Draw a half-circle with the specified radius
    drawer.circle(radius, -180)

    # Lift the pen to move without drawing
    drawer.penup()

    # Move the turtle to a new position
    drawer.setpos(offset, 0)

    # Place the pen back down to continue drawing
    drawer.pendown()

    # Rotate the pen to face the correct direction
    drawer.right(180)

# List of colors for the rainbow
colors = ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']

# Set up screen size and background color
screen.setup(width=600, height=600)
screen.bgcolor('black')

# Set up initial turtle properties
drawer.right(90)
drawer.width(10)
drawer.speed(7)

# Loop to draw each colored semicircle
for i in range(7):
    draw_semi_circle(colors[i], 10 * (i + 8), -10 * (i + 1))

# Hide the turtle after drawing
drawer.hideturtle()
