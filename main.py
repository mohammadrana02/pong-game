from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# screen setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# paddle, ball and scoreboard objects are created
right_paddle = Paddle(350)
left_paddle = Paddle(-350)
ball = Ball()
scoreboard = Scoreboard()

# controls for the right paddle
screen.listen()
screen.onkeypress(right_paddle.up, "Up")
screen.onkeypress(right_paddle.down, "Down")

# controls for the left paddle
screen.onkeypress(left_paddle.up, "w")
screen.onkeypress(left_paddle.down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)  # determines how fast the ball moves
    screen.update()  # updates the screen after all the segments have been generated

    ball.move()  # default ball movement

    # detects collisions with the ball or ceiling
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()  # the ball starts moving in the opposite y direction

    # detects collisions with the paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()  # the ball starts moving in the opposite x direction

    # detects if the right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # detects if the left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()  # the screen stays on until the mouse is clicked
