import turtle

WIDTH = 500
HEIGHT = 500
DELAY = 20

screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Stamping")
screen.bgcolor("cyan")

stamper = turtle.Turtle()
stamper.shape("square")
stamper.color("red")
stamper.shapesize(50 / 20)
stamper.stamp()
stamper.penup()
stamper.shapesize(10 / 20)
stamper.goto(100, 100)
stamper.stamp()

turtle.done()