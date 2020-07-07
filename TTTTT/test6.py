import unittest
import ddt

testdata = [{'username':'admin','password':'123456'},{'username':'ad','password':'111111'}]
@ddt.ddt
class MyTestCase(unittest.TestCase):
    def setUp(self):
        print('setup')

    @ddt.data(*testdata)
    def test_sth(self,data1):
        for i in range(len(testdata)):
            username = data1['username']
            password = data1['password']
            dic = {'username':username,'password':password}
            if dic == testdata[i]:
                print("第{}条用例，输入用户名：{} 输入密码：{}".format(i+1,username,password))

    def tearDown(self):
        print('teardown')

if __name__ == '__main__':
    unittest.main()