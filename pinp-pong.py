import turtle
from numpy import random

wn = turtle.Screen()
wn.title("Ping Pong")
wn.bgcolor('black')
width = 800
height = 600
wn.setup(width=width, height=height)
wn.tracer(0)

class AI:
    def where_to_move(self):
        ball_cor = [ball_1.ball.xcor(), ball_1.ball.ycor()]
        ball_speed = [ball_1.ball.dx, ball_1.ball.dy]
        if(ball_speed[0] > 0):
            y = (ball_speed[1]/ball_speed[0])*(width/2 - ball_cor[0] - 70) + ball_cor[1]
            if((y//2)%2 and (y > height/2 - 10)):
                y = (height/2 - 10) - (y % (height/2 - 10))
            elif((y > height/2 - 10)):
                y = (y % (height/2 - 10))
            elif((y//2)%2 and (y < -height/2 + 10)):
                y = (-height/2 + 10) + (y % (-height/2 + 10))
            elif ((y < -height/2 + 10)):
                y = (y % (-height / 2 + 10))
            return y
        return 0
    def move(self):
        y = self.where_to_move()
        if(y - paddle_2.paddle.ycor() > 45):
            paddle_2.move_up()
        elif (y - paddle_2.paddle.ycor() < -45):
            paddle_2.move_down()


class balls:
    def _init_(self):
        self.ball = turtle.Turtle()
        self.ball.speed(0)
        self.ball.shape("square")
        self.ball.color('white')
        self.ball.penup()
        self.ball.goto(0, 0)
    def random_init(self):
        self.ball.goto(random.randint(-min(width, height)/2 + 10, min(width, height)/2 - 10), random.randint(-min(width, height)/2 + 10, min(width, height)/2 - 10))
        if (random.rand() > 0.5):
            self.ball.dx = 0.03
        else:
            self.ball.dx = -0.03
        if (random.rand() > 0.5):
            self.ball.dy = 0.03
        else:
            self.ball.dy = -0.03
    def speed_increase(self):
        if self.ball.dx > 0:
            self.ball.dx += 0.001
        elif self.ball.dx < 0:
            self.ball.dx -= 0.001
        if self.ball.dy > 0:
            self.ball.dy += 0.001
        elif self.ball.dy < 0:
            self.ball.dy -= 0.001
    def movement(self):
        if (self.ball.ycor() > (height/2) - 10):
            self.ball.sety((height/2) - 10)
            self.ball.dy *= -1
        elif (self.ball.ycor() < -(height/2) + 10):
            self.ball.sety(-(height/2) + 10)
            self.ball.dy *= -1
        else:
            self.ball.sety(self.ball.ycor() + self.ball.dy)
        if ((self.ball.xcor() > (width/2) - 10) or (self.ball.xcor() < - (width/2) + 10)):
            self.random_init()
        else:
            self.ball.setx(self.ball.xcor() + self.ball.dx)

class paddle:
    def _init_(self, position):
        self.paddle = turtle.Turtle()
        self.paddle.speed(0)
        self.paddle.shape("square")
        self.paddle.color('white')
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.penup()
        self.paddle.sety(position[1])
        self.paddle.setx(position[0])
    def move_up(self):
        if(self.paddle.ycor() < height/2 - 50):
            self.paddle.sety(self.paddle.ycor() + 20)
        else:
            self.paddle.sety(height/2 - 50)
    def move_down(self):
        if (self.paddle.ycor() > -height / 2 + 50):
            self.paddle.sety(self.paddle.ycor() - 20)
        else:
            self.paddle.sety(-height / 2 + 50)


def collision():
    if((ball_1.ball.xcor() <= paddle_1.paddle.xcor() + 20) and (ball_1.ball.ycor() >= paddle_1.paddle.ycor() - 50 and ball_1.ball.ycor() <= paddle_1.paddle.ycor() + 50)):
        ball_1.ball.dx *= -1
        ball_1.speed_increase()
    elif ((ball_1.ball.xcor() >= paddle_2.paddle.xcor() - 20) and (ball_1.ball.ycor() >= paddle_2.paddle.ycor() - 50 and ball_1.ball.ycor() <= paddle_2.paddle.ycor() + 50)):
        ball_1.ball.dx *= -1
        ball_1.speed_increase()

ball_1 = balls()
ball_1.random_init()
paddle_1 = paddle((-width/2 + 50, 0))
paddle_2 = paddle((width/2 - 50, 0))
opponent = AI()

# Keyboard bindings
wn.listen()
wn.onkeypress(paddle_1.move_up, "w")
wn.onkeypress(paddle_1.move_down, "s")

# Main Game
while (True):
    wn.update()
    ball_1.movement()
    opponent.move()
    collision()
