import turtle 

turtle.color('black','red')
turtle.begin_fill()
for i in range(0,4) :
    turtle.right(90)
    turtle.forward(100)
turtle.penup()
turtle.end_fill()
turtle.forward(100)

turtle.pendown()
turtle.color("black","yellow")
turtle.begin_fill()
for i in range(0,4) :
     turtle.right(90)
     turtle.forward(100)
turtle.penup()
turtle.end_fill()
turtle.forward(100)


turtle.pendown()
turtle.color("black","green")
turtle.begin_fill()
for i in range(0,4) :
     turtle.right(90)
     turtle.forward(100)
turtle.penup()
turtle.end_fill()
turtle.exitonclick()
