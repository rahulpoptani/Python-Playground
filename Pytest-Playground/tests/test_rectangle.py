import pytest
from source import Shape as shapes

class TestRectangle:

    # @pytest.fixture
    def my_rectangle():
        return shapes.Rectangle(10, 20)

    def test_area(my_rectangle):
        assert TestRectangle.my_rectangle().area() == 10 * 20

    def test_perimeter(my_rectangle):
        assert TestRectangle.my_rectangle().perimeter() == (10 * 2) + (20 * 2)
