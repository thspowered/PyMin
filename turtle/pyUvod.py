import turtle

t = turtle.Turtle()
t.pensize(3)


def stvorec(dlzka):

    for i in range(4):
        t.fd(dlzka)
        t.rt(90)


def schody(dlzka):

    for i in range(1):
        t.forward(dlzka)
        t.left(90)
        t.forward(dlzka)
        t.right(90)


def hexagon(dlzka):

    for i in range(6):
        t.fd(dlzka)
        t.lt(60)


def hexagon_v02(dlzka):

    for i in range(4):
        t.lt(60)
        t.fd(30)


for i in range(1):
    hexagon(30)
    t.lt(240)
    t.fd(30)
    for i in range(6):
        hexagon_v02(30)
        t.lt(180)
        t.fd(30)


turtle.exitonclick()