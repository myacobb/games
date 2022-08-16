import turtle
import os

wn = turtle.Screen()
wn.title("Pong by Mya")
wn.bgcolor("black")
wn.setup(width = 800, height = 600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

#Paddle Speed
paddle_speed = 1
ball_speed = 0.5
ball_speed_increment = .5

# Paddle A
# paddle_a = turtle.Turtle()
# paddle_a.speed(paddle_speed)
# paddle_a.shape("square")
# paddle_a.color("white")
# paddle_a.shapesize(stretch_wid = 5, stretch_len = 1)
# paddle_a.penup()
# paddle_a.goto(-350, 0)

# Paddle B
# paddle_b = turtle.Turtle()
# paddle_b.speed(paddle_speed)
# paddle_b.shape("square")
# paddle_b.color("white")
# paddle_b.shapesize(stretch_wid = 5, stretch_len = 1)
# paddle_b.penup()
# paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = ball_speed
ball.dy = ball_speed


# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  PlayerB: 0", align = "center", font = ("Courier", 24, "normal"))




class Player:
    def __init__(self, x, y, speed, shape, color):
        self.x = x
        self.y = y
        self.t = turtle.Turtle()
        self.t.speed(speed)
        self.t.shape(shape)
        self.t.color(color)
        self.t.shapesize(stretch_wid=5, stretch_len=1)
        self.t.penup()
        self.t.goto(x, y)
        self.score = 0

    def goto(self, x, y):
        self.t.goto(x, y)

    def paddle_up(self):
        self.y = self.t.ycor()
        self.y += 20
        self.t.sety(self.y)

    def paddle_down(self):
        self.y = self.t.ycor()
        self.y -= 20
        self.t.sety(self.y)

    def point(self):
        self.score += 1




# class Player(turtle.Turtle):
#     def __init__(self, x, y, speed, shape, color):
#         self.speed(speed)
#         self.shape(shape)
#         self.color(color)
#         self.shapesize(stretch_wid=5, stretch_len=1)
#         self.penup()
#         self.goto(x, y)
#         self.score = 0

#     def paddle_up(self):
#         self.sety(self.ycor() + 20)

#     def paddle_down(self):
#         self.sety(self.ycor() - 20)

#     def point(self):
#         self.score += 1


player_a = Player(-350, 0, paddle_speed, "square", "white")
player_b = Player(350, 0, paddle_speed, "square", "purple")

# Functions
# def paddle_a_up():
#     y = paddle_a.ycor()
#     y += 20
#     paddle_a.sety(y)


# def paddle_a_down():
#     y = paddle_a.ycor()
#     y -= 20
#     paddle_a.sety(y)


# def paddle_b_up():
#     y = paddle_b.ycor()
#     y += 20
#     paddle_b.sety(y)


# def paddle_b_down():
#     y = paddle_b.ycor()
#     y -= 20
#     paddle_b.sety(y)

# Keyboard binding
wn.listen()

wn.onkeypress(player_a.paddle_up, "w")
wn.onkeypress(player_a.paddle_down, "s")
wn.onkeypress(player_b.paddle_up, "Up")
wn.onkeypress(player_b.paddle_down, "Down")

def go_home():
    pen.clear()
    ball.goto(0, 0)


# Main game loop
while True:
    wn.update()# Move the ball

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    # Top and Bottom
    if ball.ycor() >= 290.0:
        ball.sety(290.0)
        ball.dy *= -1.0
        #os.system("afplay bounce.wav&")

    elif ball.ycor() <= -290.0:
        ball.sety(-290.0)
        ball.dy *= -1.0
        #os.system("afplay bounce.wav&")

    # Left and Right
    if ball.xcor() > 350:
        score_a += 1
        player_a.point()
        ball_speed += ball_speed_increment
        ball.speed(ball_speed)
        print("speed: {}".format(ball_speed))

        go_home()
        pen.write("Player A: {} Player B: {}".format(player_a.score, player_b.score), align="center", font=("Courier", 24, "normal"))
        ball.dx *= -1

    elif ball.xcor() < -350:
        score_b += 1
        player_b.point()
        ball_speed += ball_speed_increment
        ball.speed(ball_speed)
        print("speed: {}".format(ball_speed))
        go_home()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.dx *= -1

    # Paddle and ball collisions
    if ball.xcor() < -340 and ball.ycor() < player_a.y + 50 and ball.ycor() > player_a.y - 50:
        ball.dx *= -1
        #os.system("afplay bounce.wav&")

    elif ball.xcor() > 340 and ball.ycor() < player_b.y + 50 and ball.ycor() > player_b.y - 50:
        ball.dx *= -1
        #os.system("afplay bounce.wav&")