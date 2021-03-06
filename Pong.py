import turtle
import time


wn=turtle.Screen()
wn.title("Pong by GentritC")
wn.bgcolor("lightgrey")
wn.setup(width=800, height=600)
wn.tracer(0)


#score
score_a=0
score_b=0

#Paddle A
paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("black")
paddle_a.penup()
paddle_a.goto(-350,0)
paddle_a.shapesize(stretch_wid=5, stretch_len=1)

#Paddle B
paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("black")
paddle_b.penup()
paddle_b.goto(350,0)
paddle_b.shapesize(stretch_wid=5, stretch_len=1)

#Ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("orange")
ball.penup()
ball.goto(0,0)
ball.dx=0.4
ball.dy=0.4

            


#pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A:0  Player B:0", align="center",font=("Arial",16,"normal"))



#Function
def paddle_a_up():
    y=paddle_a.ycor()
    if (y>=300-40):
        y=300-40
    else:
        y+=20
        
    paddle_a.sety(y)

def paddle_a_down():
    y=paddle_a.ycor()
    if (y<=-300+40+20):
        y=-300+40+20
    else:
        y-=20
    paddle_a.sety(y)

def paddle_b_up():
    y=paddle_b.ycor()
    if (y>=300-40):
        y=300-40
    else:
        y+=20
    paddle_b.sety(y)

def paddle_b_down():
    y=paddle_b.ycor()
    if (y<=-300+40+20):
        y=-300+40+20
    else:
        y-=20
    paddle_b.sety(y)

# #Keyboard
wn.listen()
wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")

#Main game loop
while True:
    wn.update()
    #ball moving
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    #border check
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy*=-1

    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy*=-1

    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx*=-1
        score_a+=1
        pen.clear()
        pen.write("Player A:{}  Player B:{}".format(score_a,score_b), align="center",font=("Arial",16,"normal"))
        
        
        
    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx*=-1
        score_b+=1
        pen.clear()
        pen.write("Player A:{}  Player B:{}".format(score_a,score_b), align="center",font=("Arial",16,"normal"))

    #ball and paddle collision
    if (ball.xcor()>335 and ball.xcor()<355) and (ball.ycor()<paddle_b.ycor()+60 and ball.ycor()>paddle_b.ycor()-60):
        ball.setx(335)
        ball.dx*=-1
    if (ball.xcor()<-335 and ball.xcor()>-355) and (ball.ycor()<paddle_a.ycor()+60 and ball.ycor()>paddle_a.ycor()-60):
        ball.setx(-335)
        ball.dx*=-1



        