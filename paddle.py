from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_cor):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setpos(x=x_cor, y=0)

    def up(self):
        """The paddle moves up"""
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        """The paddle moves down"""
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)



