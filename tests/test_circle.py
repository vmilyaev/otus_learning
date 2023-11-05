import pytest
from src.circle import Circle
from src.triangle import Triangle


@pytest.mark.parametrize('radius, area, perimeter',
                         [
                             (4, 50.24, 25.12),
                             (8, 200.96, 50.24)
                         ])
def test_circle(radius, area, perimeter):
    r = Circle(radius)
    assert r.name == 'Circle'
    assert r.get_area() == area
    assert r.get_perimeter() == perimeter


@pytest.mark.parametrize('radius', [-4])
def test_circle_negative(radius):
    with pytest.raises(ValueError):
        Circle(radius)


def test_add_area():
    r1 = Triangle(10, 5, 5)
    r2 = Circle(10)
    assert r1.add_area(r2) == 324
