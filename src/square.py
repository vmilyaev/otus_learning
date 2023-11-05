from src.rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, side_a):
        if side_a <= 0:
            raise ValueError(f'Cannot create Square')
        super().__init__(side_a, side_a)
        self.side_a = side_a
        self.name = 'Square'

    def get_area(self):
        return self.side_a * self.side_a

    def get_perimeter(self):
        return (self.side_a + self.side_a) * 2

    def add_area(self, other_figure):
        return self.get_area() + other_figure.get_area()
