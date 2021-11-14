from shape import Shape


class Triangle(Shape):
    def __init__(self, pos_x, pos_y, sideSize):
        super().__init__(pos_x, pos_y)
        self.sideSize = sideSize

    def draw(self, turtle):
        super().draw(turtle)
        if self.color != None:
            turtle.pencolor(self.color)

        for i in range(0,3):
            turtle.forward(self.sideSize)
            turtle.left(120)
