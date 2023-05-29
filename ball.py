from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.07

    def move(self):
        """Default ball movement"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """The ball starts moving in the opposite y direction when it hits the ceiling"""
        self.y_move *= -1

    def bounce_x(self):
        """The ball starts moving towards the opposite paddle and the speed increases when it hits a paddle"""
        self.x_move *= -1
        self.move_speed *= 0.9
        print(self.move_speed)

    def reset_position(self):
        """The ball is reset to the starting position, starts moving towards the opposite paddle and
        the speed is reset"""
        self.goto(0, 0)
        self.bounce_x()
        self.move_speed = 0.07
