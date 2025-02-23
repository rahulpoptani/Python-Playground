import pytest

# when you want to test the function on different values

class TestParams:

    @pytest.mark.parametrize('input_data', [70, 80, 45, 55])
    def test_param(self, input_data):
        assert input_data > 50
    
    @pytest.mark.parametrize('x, y', [(2, 4), (3, 27), (4, 256)])
    def test_square(self, x, y):
        assert (x ** x) == y