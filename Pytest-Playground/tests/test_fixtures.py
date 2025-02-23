import pytest

class TestFixtures:

    @pytest.fixture()
    def setup_list(self):
        print('\nInside Fixture.. Setting Up Test')
        ll = [1, 2, 3, 4, 5]
        return ll
    
    def test_getlist(self, setup_list):
        assert setup_list == [1, 2, 3, 4, 5]