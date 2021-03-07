import turtle
import winsound

def pa_up():
    y = pa.ycor()
    y += 20
    pa.sety(y)
def pa_down():
    y = pa.ycor()
    y -= 20
    pa.sety(y)
def pb_up():
    y = pb.ycor()
    y += 20
    pb.sety(y)
def pb_down():
    y = pb.ycor()
    y -= 20
    pb.sety(y)

scrn = turtle.Screen()
scrn.title("Pong")
scrn.bgcolor("black")
scrn.setup(width=800, height=600)
scrn.tracer(0)

scrn.listen()
scrn.onkeypress(pa_up, "w")
scrn.onkeypress(pa_down, "s")
scrn.onkeypress(pb_up, "Up")
scrn.onkeypress(pb_down, "Down")

pa = turtle.Turtle()
pa.shape("square")
pa.speed(0)
pa.color("cyan")
pa.penup()
pa.goto(-350, 0)
pa.shapesize(stretch_wid=5, stretch_len=1)

pb = turtle.Turtle()
pb.shape("square")
pb.speed(0)
pb.color("cyan")
pb.penup()
pb.goto(350, 0)
pb.shapesize(stretch_wid=5, stretch_len=1)

ball = turtle.Turtle()
ball.shape("square")
ball.speed(0)
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.4
ball.dy = 0.4

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 240)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 19, "normal"))

sca = 0
scb = 0

while True:
    scrn.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1 
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        sca += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(sca, scb), align="center", font=("Courier", 19, "normal"))
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        scb +=1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(sca, scb), align="center", font=("Courier", 19, "normal"))

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < pb.ycor() + 50 and ball.ycor() > pb.ycor() - 50):
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        ball.setx(340)
        ball.dx *= -1 
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < pa.ycor() + 50 and ball.ycor() > pa.ycor() - 50):
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        ball.setx(-340)
        ball.dx *= -1