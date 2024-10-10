from turtle import Screen
from food import Food
import time
from snake import Snake
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.title("My Snake Game")
screen.bgcolor("black")
screen.tracer(0)

call_snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(call_snake.up, "Up")
screen.onkey(call_snake.down, "Down")
screen.onkey(call_snake.left, "Left")
screen.onkey(call_snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    call_snake.move()

    # detect collision with food
    if call_snake.head.distance(food) < 15:
        food.refresh()
        call_snake.extend()
        scoreboard.increase_score()

    # detect collision with wall
    if (call_snake.head.xcor() > 280 or call_snake.head.xcor() < -280 or call_snake.head.ycor() > 280 or
            call_snake.head.ycor() < -280):
        game_is_on = False
        scoreboard.game_over()

    # if head collide with tail
    for segment in call_snake.segment[1:]:
        if call_snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
