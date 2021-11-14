import turtle
from rectangle import Rectangle
from triangle import Triangle
from circle import Circle

emil = turtle.Turtle()
emil.speed(20)

rectangle_1 = Rectangle(200,200,75,120)
rectangle_1.setColor("black")
rectangle_1.draw(emil)

rectangle_2 = Rectangle(-100,100,180,50)
rectangle_2.setColor("yellow")
rectangle_2.draw(emil)

triangle = Triangle(50,0,80)
triangle.setColor("purple")
triangle.draw(emil)

circle = Circle(0,0,80)
circle.setColor("red")
circle.draw(emil)

turtle.exitonclick()