import unittest
import ddt
from common.excel_read import ExcelUtil

re = ExcelUtil('../data/haha.xlsx','Sheet1')
testdata = re.next()
# print(testdata)
# testdata = [{'username':'admin','password':'123456'},{'username':'ad','password':'111111'}]
@ddt.ddt
class MyTestCase(unittest.TestCase):
    def setUp(self):
        print('setup')

    @ddt.data(*testdata)
    def test_sth(self,data1):

        ex = ExcelUtil('../data/haha.xlsx','Sheet1').next()
        ces = ex[int(data1['编码']-1)]['密码']
        print(ces)
        # for i in range(len(testdata)):
        #     username = data1['用户名']
        #     password = data1['密码']
        #     self.dic = {'用户名':username,'密码':password}
        # print(self.dic)
        # yuqi = data1['预期结果']
        # siji = data1['实际结果']
        # self.assertEqual(yuqi,siji)
            # if dic == testdata[i]:
            #     print("第{}条用例，输入用户名：{} 输入密码：{}".format(i+1,username,password))

    def tearDown(self):
        print('teardown')

if __name__ == '__main__':
    unittest.main()