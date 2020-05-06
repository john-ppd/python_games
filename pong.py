#turtle module and pigame are modules used for making games
import turtle

#creating the window
wn = turtle.Screen()
wn.title("pong game")
#background color
wn.bgcolor("black")
#window size, 0,0 is in the center of the window, -400 is left border, +400 is right border, -300 is bottom, 300 is top border
wn.setup(width=800, height=600)
#window tracer makes it so we manually update our window, stops an infinite refresh
wn.tracer(0)

#Paddle A
#turtle is module name, Turtle is class name
paddle_a = turtle.Turtle()
#speed(0) sets animation speed to max speed
paddle_a.speed(0)
paddle_a.shape("square")
#stretch 5 will be 5 squares, 1 is default size, default is 20px,20px so this will make it 100,20
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.color("white")
#without penup() there will be a line from 0,0 to the box
paddle_a.penup()
#goto is paddle_a's starting location or spawn location
paddle_a.goto(-350,0)
#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)
#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.shapesize(stretch_wid=1, stretch_len=1)
ball.penup()
ball.goto(0,0)
#ball speed x and y, every refresh it will move 2 px up and right
ball.dx = 0.3
ball.dy = 0.3


p1_score = 0
p2_score = 0

# Function
def paddle_a_up():
    #returns the y coordinate
    y = paddle_a.ycor()
    #calculate new y which is 20 pixels above
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_a_right():
    x = paddle_a.xcor()
    x += 20
    paddle_a.setx(x)

def paddle_a_left():
    x = paddle_a.xcor()
    x -= 20
    paddle_a.setx(x)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


def update_scores(p1, p2):
    # pen is a turtle object to print onto the screen
    pen = turtle.Turtle()
    pen.speed(0)
    # animation speed
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.clear()
    pen.write("Player A: {} Player B: {}".format(p1_score, p2_score), align="center", font=("Courier", 24, "normal"))





#keyboard listener
#listen for keyboarrd input
wn.listen()
#when w is pressed call function and W will not work, no brackets with function call
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_a_right, "d")
wn.onkeypress(paddle_a_left, "a")

#arrows use Up Down Left Right
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

def check_border_collision():
    #remember ball is 20px,20px
    if ball.ycor() > 290:
        ball.sety(290)#solves some problems by setting it back
        ball.dy *= -1
    elif ball.ycor() < (-290):
        ball.sety(-290)
        ball.dy *= -1


    #p1_score += 1

    if ball.xcor() > 390:
        #ball.setx(0)
        #ball.sety(0)
        #above code is same as
        ball.goto(0,0)
        ball.dx *= -1
        update_score(True, False)
    elif ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        update_score(False, True)

        #p2_score += 1

def update_score(p1, p2):
    global p1_score
    global p2_score
    if p1:
        p1_score += 1
        print("p1 = " + str(p1_score))
        update_scores(p1_score, p2_score)

    elif p2 == True:
        p2_score += 1
        print("p2 = " + str(p2_score))
        update_scores(p1_score, p2_score)



def paddle_ball_collision():
   # print("paddl_a y = " + str(paddle_a.ycor()))
   #paddle right side
    if ((ball.xcor() > 340 and ball.xcor() < 350) and ball.ycor() < (paddle_b.ycor()+50) and ball.ycor() > (paddle_b.ycor()-50)):
        print("passed through")
        ball.setx(340)
        ball.dx *= -1

    #paddle left side
    if ((ball.xcor() < -340 and ball.xcor() > -350) and ball.ycor() < (paddle_a.ycor()+50) and ball.ycor() > (paddle_a.ycor()-50)):
        print("passed through")
        ball.setx(-340)
        ball.dx *= -1
update_scores(0, 0)
while True:
    wn.update()

    #ball movement
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    paddle_ball_collision()
    #borderchecking
    check_border_collision()


