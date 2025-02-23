import pytest

class TestExceptions:
    def test_raiseZeroDivision(self):
        with pytest.raises(ZeroDivisionError):
            assert (10/0)
    
    def test_raiseAssertion(self):
        with pytest.raises(AssertionError):
            assert 3 > 4
