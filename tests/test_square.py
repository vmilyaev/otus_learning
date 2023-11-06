import pytest
from src.square import Square
from src.triangle import Triangle


@pytest.mark.parametrize('side_a, area, perimeter',
                         [
                             (4, 16, 16),
                             (5, 25, 20)
                         ])
def test_square(side_a, area, perimeter):
    r = Square(side_a)
    assert r.name == 'Square'
    assert r.get_area() == area
    assert r.get_perimeter() == perimeter


@pytest.mark.parametrize('side_a', [-4, 0])
def test_square_negative(side_a):
    with pytest.raises(ValueError):
        Square(side_a)


def test_add_area():
    r1 = Triangle(10, 5, 5)
    r2 = Square(5)
    assert r1.add_area(r2) == 35
