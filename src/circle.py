from src.figure import Figure


class Circle(Figure):

    def __init__(self, radius):
        if radius <= 0:
            raise ValueError('Can not create Circle')
        self.radius = radius
        self.name = 'Circle'

    def get_area(self):
        return 3.14 * self.radius * self.radius

    def get_perimeter(self):
        return 2 * 3.14 * self.radius

    def add_area(self, other_figure):
        return self.get_area() + other_figure.get_area()