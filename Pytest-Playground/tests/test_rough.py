
class TestRough:

    def test_type(self):
        assert type(1) == int
    
    def test_string(self):
        assert str.upper('python') == 'PYTHON'
        assert 'python'.capitalize() == 'Python'