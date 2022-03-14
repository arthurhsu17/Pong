import turtle as t
import random as r
import tkinter

# two players game
playerA= 0
playerB= 0



# set screen

window= t.Screen()
window.title("Pong")
window.bgcolor("white")
window.setup(width=800,height=600)
window.tracer(0)

# initialize ball

ball=t.Turtle()
ball.speed(1)
ball.shape("circle")
ball.color("blue")
ball.penup()
ball.goto(r.randint(0, 360),r.randint(0, 360))
ballxdirection=2.5
ballydirection=2.5

# left paddle

left=t.Turtle()
left.speed(0)
left.shape("square")
left.color("black")
left.shapesize(stretch_wid=6,stretch_len=0.8)
left.penup()
left.goto(-350,0)

#right paddle

right=t.Turtle()
right.speed(0)
right.shape("square")
right.color("black")
right.shapesize(stretch_wid=6,stretch_len=0.8)
right.penup()
right.goto(350,0)



# score

pen=t.Turtle()
pen.speed(0)
pen.color("red")
pen.hideturtle()
pen.goto(0,260)
pen.write("score",align="center",font=('Comic Sans MS',24,'normal'))

# controls of paddle

def leftpaddleup():
    y= left.ycor()
    y=y+45
    left.sety(y)

def leftpaddledown():
    y= left.ycor()
    y=y-45
    left.sety(y)

def rightpaddleup():
    y= right.ycor()
    y=y+45
    right.sety(y)

def rightpaddledown():
    y= right.ycor()
    y=y-45
    right.sety(y)

# key presses

window.listen()
window.onkeypress(leftpaddleup,'w')
window.onkeypress(leftpaddledown,'s')
window.onkeypress(rightpaddleup,'Up')
window.onkeypress(rightpaddledown,'Down')

# game loop
while True:
    window.update()
    ball.setx(ball.xcor()+ballxdirection)
    ball.sety(ball.ycor()+ballydirection)

# set up the border
    if ball.ycor()>290:
        ball.sety(290)
        ballydirection=ballydirection*-1

    if ball.ycor()<-290:
        ball.sety(-290)
        ballydirection=ballydirection*-1

    if ball.xcor()>390:
        ball.goto(0,0)
        ballxdirection= ballxdirection *-1
        playerA=playerA+1
        pen.clear()
        pen.write("Player 1:{}    Player 2:{}".format(playerA,playerB),align="center",font=('Comic Sans MS',24,'normal'))

    if ball.xcor()<-390:
        ball.goto(0,0)
        ballxdirection= ballxdirection *-1
        playerB=playerB+1
        pen.clear()
        pen.write("Player 1:{}    Player 2:{}".format(playerA,playerB),align="center",font=('Comic Sans MS',24,'normal'))


## collisons with paddles

    if(ball.xcor() > 340) and (ball.xcor() < 360) and (
        ball.ycor()<right.ycor() +40 and ball.ycor()>right.ycor() -40) :

        ball.setx(340)
        ballxdirection= ballxdirection * -1

    if(ball.xcor() < -340) and (ball.xcor() > -360) and (
        ball.ycor() <left.ycor() +40 and ball.ycor()>left.ycor() -40) :
        
        ball.setx(-340)
        ballxdirection= ballxdirection * -1
        