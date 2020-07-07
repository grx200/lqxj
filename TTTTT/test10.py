import pytest
class TestCase():
    @pytest.mark.parametrize("getdataA",
                        [{'userID':'00001','username':'jack'},
                        {'userID':'00002','username':'mike'}])
    def test_case1(self, getdataA):
        print("第1个用例输出：{}".format(getdataA))

    @pytest.mark.parametrize("getdataB",
                        [{'userID':'00003','username':'tina'},
                        {'userID':'00004','username':'book'}])
    def test_case2(self, getdataB):
        print("第2个用例输出：{}".format(getdataB))

if __name__ == '__main__':
    pytest.main()