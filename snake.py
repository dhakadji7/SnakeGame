from turtle import Turtle
STARTING_POSITONS=[(0,0),(-20,0),(-40,0)]
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake:
    
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]


    def create_snake(self):
        for position in STARTING_POSITONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)
            # self.update_snake()

    #Add new segment to the snake
    def update_snake(self):
        x_cor=self.segments[len(self.segments)-1].xcor()
        y_cor=self.segments[len(self.segments)-1].ycor()
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(x=x_cor,y=y_cor)
        self.segments.append(new_segment)

    def reset_snake(self):
        for segment in self.segments:
            segment.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def move(self):
        for i in range(len(self.segments)-1,0,-1):
            self.segments[i].goto(self.segments[i - 1].pos())
        # self.segments[1].goto(self.segments[0].pos())
        self.head.forward(20)

    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

