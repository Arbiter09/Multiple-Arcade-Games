import turtle
def game():
    win = turtle.Screen()
    win.title("Pong By Jas Shah")
    win.setup(width=800, height=600)
    win.bgcolor("black")
    win.tracer(0)

    a_score = 0
    b_score = 0
    #Paddle A
    paddle_a = turtle.Turtle()
    paddle_a.speed(0)
    paddle_a.color("white")
    paddle_a.shape("square")
    paddle_a.shapesize(stretch_wid=5,stretch_len=1)
    paddle_a.penup()
    paddle_a.goto(-350,0)

    #Paddle B
    paddle_b = turtle.Turtle()
    paddle_b.speed(0)
    paddle_b.color("white")
    paddle_b.shape("square")
    paddle_b.shapesize(stretch_wid=5,stretch_len=1)
    paddle_b.penup()
    paddle_b.goto(350,0)

    #Ball
    ball = turtle.Turtle()
    ball.speed(0.5)
    ball.color("white")
    ball.shape("square")
    ball.penup()
    ball.goto(0,0)
    ball.dx = 0.1
    ball.dy = 0.1

    #Score Board
    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape("square")
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

    #Move Paddle A
    def Pad_a_up():
        y = paddle_a.ycor()
        y = y+20
        paddle_a.sety(y)
    def Pad_a_down():
        y = paddle_a.ycor()
        y = y-20
        paddle_a.sety(y)

    # Move Paddle B
    def Pad_b_up():
        y = paddle_b.ycor()
        y = y+20
        paddle_b.sety(y)
    def Pad_b_down():
        y = paddle_b.ycor()
        y = y-20
        paddle_b.sety(y)


    win.listen()
    win.onkeypress(Pad_a_up, "w")
    win.onkeypress(Pad_a_down, "s")
    win.onkeypress(Pad_b_up, "Up")
    win.onkeypress(Pad_b_down, "Down")

    while True:
        win.update()


    #Making Sure Paddle Does not go Out Of Bounds
        while(paddle_a.ycor()>250):
            paddle_a.sety(250)
        while(paddle_b.ycor()>250 ):
            paddle_b.sety(250)
        while(paddle_a.ycor()<-250 ):
            paddle_a.sety(-250)
        while(paddle_b.ycor()<-250 ):
            paddle_b.sety(-250)

    #Moving the Ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

    #Border Checking
        if(ball.ycor()>300):
            ball.sety(300)
            ball.dy *= -1
        if(ball.ycor()<-300):
            ball.sety(-300)
            ball.dy *= -1

    #Ball Reset
        if ball.xcor() > 370:
           a_score += 1  
           pen.clear()
           pen.write("Player A: {}  Player B: {}".format(a_score,b_score), align="center", font=("Courier", 24, "normal"))
           ball.goto(0, 0)
           ball.dx *= -1
        if ball.xcor() <- 370:
            b_score += 1  
            pen.clear()
            pen.write("Player A: {}  Player B: {}".format(a_score,b_score), align="center", font=("Courier", 24, "normal"))
            ball.goto(0, 0)
            ball.dx *= -1
    #Ball Collisions
        #Paddle B
        if((ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50 ) ):
            ball.setx(340)
            ball.dx *= -1
        #Paddle A
        if((ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50 ) ):
            ball.setx(-340)
            ball.dx *= -1






