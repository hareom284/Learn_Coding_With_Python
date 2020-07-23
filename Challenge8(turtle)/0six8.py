import turtle
import random
lines = random.randint(4,20)
for i in range(0,lines):
    length= random.randint(25,100)
    rotate= random.randint(1,350)
    turtle.forward(length)
    turtle.right(rotate)
turtle.exitonclick()