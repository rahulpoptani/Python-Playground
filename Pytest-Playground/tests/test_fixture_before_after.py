import pytest

l1 = [1, 2, 3]
l2 = [5, 6, 7]

class TestFixtureBeforeAndAfter:
    
    @pytest.fixture()
    def setup(self):
        # Before yield means setup
        l3 = l1.copy()
        l3.append(4)
        yield l3
        # After yield means teardown
        l2.pop()
    
    def test_list(self, setup):
        setup.extend(l2)
        assert setup == [1, 2, 3, 4, 5, 6, 7]