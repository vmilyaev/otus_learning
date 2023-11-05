import pytest
from src.rectangle import Rectangle
from src.triangle import Triangle


@pytest.mark.parametrize('side_a, side_b, side_c, area, perimeter',
                         [
                             (4, 5, 5, 7, 14),
                             (13, 7, 10, 15, 30),
                         ])
def test_triangle(side_a, side_b, side_c, area, perimeter):
    r = Triangle(side_a, side_b, side_c)
    assert r.name == 'Triangle'
    assert r.get_area() == area
    assert r.get_perimeter() == perimeter


@pytest.mark.parametrize('side_a, side_b, side_c, area, perimeter',
                         [
                             (-4, 5, 5, 20, 18),
                             (-4, 0, 6, 20, 18),
                         ])
def test_triangle_negative(side_a, side_b, side_c, area, perimeter):
    with pytest.raises(ValueError):
        Triangle(side_a, side_b, side_c)


def test_add_area():
    r1 = Rectangle(10, 5)
    r2 = Triangle(5, 5, 7)
    assert r1.add_area(r2) == 58.5
