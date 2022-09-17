from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
paddle = Turtle()
screen.setup(height=600,width=800)
screen.bgcolor("black")
screen.tracer(0)
screen.title("PONG GAME")

r_paddle= Paddle((350,0))
l_paddle= Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down, "s")

game_is_one = True
while game_is_one :
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor() >280 or ball.ycor() <-280:
        #needs to bounce
        ball.bounce_y()

    #deect collision with r_paddle
    if ball.distance(r_paddle) <50 and ball.xcor() >320 or ball.distance(l_paddle)  <50 and ball.xcor() <-320 :
        ball.bounce_x()

    # detect r_paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # detect l_paddle miss
    if ball.xcor() <-380:
        ball.reset_position()
        scoreboard.r_point()















screen.exitonclick()