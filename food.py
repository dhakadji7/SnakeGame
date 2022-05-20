from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.refresh()

    def refresh(self):
        rand_xcor = random.randint(-280, 280)
        rand_ycor = random.randint(-280, 280)
        self.goto(x=rand_xcor, y=rand_ycor)
