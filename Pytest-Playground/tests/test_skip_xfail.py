import pytest, sys

# for marking the complete test file to be skipped based on condition
# pytestmark = pytest.mark.skipif(sys.platform == 'linux', reason='will only run on windows')

class TestFixturess:
    
    # skipping individual tests
    @pytest.mark.skip(reason="skipping for testing")
    def test_skiptest(self):
        assert 1 == 2
    
    @pytest.mark.skipif(sys.version_info > (3,8), reason="does not work in with v3.8 and higher")
    def test_skipForLesserVersions(self):
        assert 1 == 2
    
    # tests which are expected to fail for some reason
    @pytest.mark.xfail(reason="known issue")
    def test_shouldfail(self):
        assert 1 == 2
    
    @pytest.mark.xfail(raises=IndexError, reason="Should throw an Index Error, Expected to Fail")
    def test_IndexError(self):
        l = [1,2,3]
        assert l[4]
    
    def test_shouldrun(self):
        assert True
