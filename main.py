from turtle import Screen
from food import Food
from scoreboard import Scoreboard
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Eat")
screen.tracer(0)


# close the screen on esc function
def close():
    screen.bye()


# CREATING THE SNAKE
snake = Snake()
scoreboard = Scoreboard()
# CREATING THE FOOD
food = Food()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")
# screen.onkey(snake.up, "up")
# screen.onkey(snake.down, "down")
# screen.onkey(snake.left, "left")
# screen.onkey(snake.right, "right")
screen.onkey(close, "Escape")

# MOVING THE SNAKE
game_is_on = True
while game_is_on:
    screen.update()

    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        scoreboard.increase_score()

    # Detect collision with walls
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 15:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()