from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(x=0, y=270)
        self.score=0
        with open("data.txt") as data:
            self.highscore=(data.read())
        self.color("white")
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score:{self.score}  Highscore:{self.highscore}", align="center", font=("Courier", 18 , "normal"))

    def reset_score(self):
        if self.score>self.highscore:
            self.highscore = self.score
            with open("data.txt",mode="w") as data:
                data.write(f"{self.highscore}")
        self.score=0
        self.update_score()

    def increase_score(self):
        self.score = self.score + 1
        self.update_score()

