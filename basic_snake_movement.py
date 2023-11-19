import turtle
import random

WIDTH = 500
HEIGHT = 500
DELAY = 100
FOOD_SIZE = 20

offsets = {
    "up": (0, 20),
    "down": (0, -20),
    "left": (-20, 0),
    "right": (20, 0)
}

def bind_direction_keys():
    screen.onkey(lambda: set_snake_direction("up"), "Up")
    screen.onkey(lambda: set_snake_direction("down"), "Down")
    screen.onkey(lambda: set_snake_direction("left"), "Left")
    screen.onkey(lambda: set_snake_direction("right"), "Right")
    
def set_snake_direction(direction):
    global snake_direction
    if direction == "up":
        if snake_direction != "down": # No self-collision simply by pressing wrong key
            snake_direction = "up"
    elif direction == "down":
        if snake_direction != "up": # No self-collision simply by pressing wrong key
            snake_direction = "down"
    elif direction == "right":
        if snake_direction != "left": # No self-collision simply by pressing wrong key
            snake_direction = "right"
    elif direction == "left":
        if snake_direction != "right": # No self-collision simply by pressing wrong key
            snake_direction = "left"
 
def game_loop():
    stamper.clearstamps()

    new_head = snake[-1].copy()
    new_head[0] += offsets[snake_direction][0]
    new_head[1] += offsets[snake_direction][1]

    # Check collisions
    if new_head in snake or new_head[0] < - WIDTH / 2 or new_head[0] > WIDTH / 2 \
        or new_head[1] < - HEIGHT / 2 or new_head[1] > HEIGHT / 2:
        reset()
    else: 

        # Add new head to snake body
        snake.append(new_head)

        # Check food collision
        if not food_collision():
            snake.pop(0) # Remove last segment of snake (keep the same length unless fed)

        # Draw snake for the first time
        for segment in snake:
            stamper.goto(segment[0], segment[1])
            stamper.stamp()

        # Refresh screen
        screen.title(f"Snake Game. Score: {score}")
        screen.update()

        turtle.ontimer(game_loop, DELAY)

def food_collision():
    global food_position, score
    if get_distance(snake[-1], food_position) < 20:
        score += 1
        food_position = get_random_food_position()
        food.goto(food_position)
        return True
    return False

def get_random_food_position():
    x = random.randint(int(- WIDTH / 2 + FOOD_SIZE), int(WIDTH / 2 - FOOD_SIZE))
    y = random.randint(int(- HEIGHT / 2 + FOOD_SIZE), int(HEIGHT / 2 - FOOD_SIZE))
    return (x, y)

def get_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    distance = ((y2-y1) ** 2 + (x2 - x1) ** 2) ** 0.5 # Pythagoras' Theorem
    return distance

def reset():
    global score, snake, snake_direction, food_position
    score = 0
    snake = snake = [[0, 0], [20, 0], [40, 0], [60,0]]
    snake_direction = "up"
    food_position = get_random_food_position()
    food.goto(food_position)
    game_loop()

screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Snake")
screen.bgcolor("pink")
screen.tracer(0)

screen.listen()
bind_direction_keys()

# Create a turtle 
stamper = turtle.Turtle()
stamper.shape("square")
stamper.color()
stamper.penup()

# Food
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.shapesize(FOOD_SIZE / 20)
food.penup()

# Start animation
reset()

# Finish
turtle.done()