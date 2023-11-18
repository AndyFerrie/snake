import turtle

WIDTH = 500
HEIGHT = 500
DELAY = 20

def move_turtle():
    my_turtle.forward(1)
    my_turtle.right(1)
    screen.update()
    screen.ontimer(move_turtle, DELAY)

screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Program Title")
screen.bgcolor("cyan")
screen.tracer(0)

my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.color("red")

move_turtle()

turtle.done()