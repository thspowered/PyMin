from random import randrange, uniform
import turtle


t = turtle.Turtle()
t.pensize(5)

def stvorec():
    dlzka = randrange(30, 100)
    t.pencolor("green")
    for i in  range(4):
        t.fd(dlzka)
        t.rt(90)


def troj():
    dlzka = randrange(30, 100)
    t.pencolor("yellow")
    for i in range(3):
        t.fd(dlzka)
        t.lt(120)

def miesto():
    x = randrange(-200, 200)
    y = randrange(-200, 200)
    t.setpos(x, y)


for i in range(randrange(10,50)):
    t.penup()
    miesto()
    t.pendown()
    tvar = randrange(0,2)
    if (tvar >= 1):
        stvorec()
    else:
        troj()

turtle.exitonclick()