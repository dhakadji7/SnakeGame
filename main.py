from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen=Screen()
screen.title("Rahul's Snake Game")
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.tracer(0)

snake=Snake()
food = Food()
score = Scoreboard()
# score=ScoreBoard()
screen.listen()
screen.onkey(key="Up",fun=snake.up)
screen.onkey(key="Down",fun=snake.down)
screen.onkey(key="Left",fun=snake.left)
screen.onkey(key="Right",fun=snake.right)



start_game=True
while start_game:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detecting snake collision with food
    if snake.head.distance(food)<15:
        food.refresh()
        score.increase_score()
        snake.update_snake()

    #Detect collision with wall
    if snake.head.xcor()>280 or snake.head.xcor()<-285 or snake.head.ycor()>280 or snake.head.ycor()<-285:
        score.reset_score()
        snake.reset_snake()
        # score.game_over()

    #Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            score.reset_score()
            snake.reset_snake()
            # score.game_over() 

    #If head collides with any part of snake
        #game ends there







screen.exitonclick()