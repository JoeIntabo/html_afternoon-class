class Shape:

    def area(self):
        return 0


class Triangle(Shape):
    def __init__(self, base, height):
        self.myheight = height
        self.mybase = base

    def area(self):
        print(0.5 *   self.mybase * self.myheight)
calculate=Triangle(9,10)
calculate.area()

class Rectangle(Shape):
    def __init__(self, length, width):
        self.mylenth = length
        self.mywidth = width

    def area(self):
        print(  self.mylenth* self.mywidth)
hesabu= Rectangle(9,10)
hesabu.area()
