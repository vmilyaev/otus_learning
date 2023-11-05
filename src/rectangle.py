from src.figure import Figure


class Rectangle(Figure):

    def __init__(self, side_a, side_b):
        if side_a <= 0 or side_b <= 0:
            raise ValueError(f'Cannot create rectangle')
        self.side_a = side_a
        self.side_b = side_b
        self.name = 'Rectangle'

    def get_area(self):
        return self.side_a * self.side_b

    def get_perimeter(self):
        return (self.side_a + self.side_b) * 2

    def add_area(self, other_figure):
        return self.get_area() + other_figure.get_area()
