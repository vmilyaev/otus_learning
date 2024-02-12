from src.figure import Figure


class Triangle(Figure):

    def __init__(self, side_a, side_b, side_c):
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError(f'Cannot create Triangle')
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.name = 'Triangle'

    def get_area(self):
        return (self.side_a + self.side_b + self.side_c) / 2

    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c

    def add_area(self, other_figure):
        return self.get_area() + other_figure.get_area()