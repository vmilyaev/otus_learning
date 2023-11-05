import pytest
from src.rectangle import Rectangle
from src.circle import Circle
from src.square import Square


@pytest.mark.parametrize('side_a, side_b, area, perimeter',
                         [
                             (4, 5, 20, 18),
                             (4, 5, 20, 18),
                         ])
def test_rectangle(side_a, side_b, area, perimeter):
    r = Rectangle(side_a, side_b)
    assert r.name == 'Rectangle'
    assert r.get_area() == area
    assert r.get_perimeter() == perimeter


@pytest.mark.parametrize('side_a, side_b, area, perimeter',
                         [
                             (-4, 5, 20, 18),
                             (-4, 0, 20, 18),
                         ])
def test_rectangle_negative(side_a, side_b, area, perimeter):
    with pytest.raises(ValueError):
        Rectangle(side_a, side_b)


def test_add_area():
    r1 = Rectangle(10, 5)
    r2 = Circle(5)
    assert r1.add_area(r2) == 128.5
