# Import the turtle library for drawing
import turtle

# Set up the screen
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Heart of Love")

# Create a turtle object for drawing
pen = turtle.Turtle()
pen.shape("turtle")
pen.speed(2)
pen.width(3)

# Function to draw a heart shape
def draw_heart():
    pen.color("blue")
    pen.begin_fill()
    pen.left(50)
    pen.forward(133)
    pen.circle(50, 200)
    pen.right(140)
    pen.circle(50, 200)
    pen.forward(133)
    pen.end_fill()

# Function to display the "Love" text
def display_message():
    pen.penup()
    pen.goto(-70, -70)
    pen.color("white")
    pen.write("Love u sayangku cintaku ", align="center", font=("Arial", 24, "bold"))
    pen.goto(-70, -100)
    pen.write("Fahira Cimulukutut", align="center", font=("Arial", 18, "italic"))

# Main drawing function
def main():
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()
    draw_heart()
    display_message()

# Run the main function
main()

# Keep the window open until the user closes it
turtle.done()
