import random
import turtle
turtle.pensize(3)
for i in range(0,8) :
    turtle.color (random.choice(["red","green","blue","cyan","pink","orange"]))
    turtle.forward(40)
    turtle.right(45)
turtle.exitonclick()