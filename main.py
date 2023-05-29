from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

# screen setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle(350)
left_paddle = Paddle(-350)
ball = Ball()

# controls setup
screen.listen()
screen.onkeypress(right_paddle.up, "Up")
screen.onkeypress(right_paddle.down, "Down")

screen.onkeypress(left_paddle.up, "w")
screen.onkeypress(left_paddle.down, "s")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()  # updates the screen after all the segments have been generated

    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:  # if the ball hits the floor or ceiling
        ball.bounce_y()  # the ball starts moving in the opposite y direction

    # detects collisions with the paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detects if the ball is out of bounds
    if ball.xcor() > 420 or ball.xcor() < -420:
        game_is_on = False
screen.exitonclick()
