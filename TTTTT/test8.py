import unittest
import paramunittest

data = ({"username": "admin", "password": "123"},{"username": "admin1", "password": "1234"})
@paramunittest.parametrized(*data)
class TestDemo(unittest.TestCase):
    def setParameters(self, username, password):
        self.user = username
        self.paw = password

    def testcase(self):
        print('用户名输入：{} 密码输入：{}'.format(self.user,self.paw))

    def setUp(self):
        print('setup')

    def tearDown(self):
        print('teardown')

if __name__ == "__main__":
    unittest.main()