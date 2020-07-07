import unittest
# from common.HTMLTestRunner import HTMLTestRunner
# from T2.HTMLTestRunner import HTMLTestRunner
# from TTTTT.HTMLTestRunner import HTMLTestRunner
from T2.HTMLTestRunner import HTMLTestRunner
from util.change_file import Change_file

# 生成测试报告
test_dir = "..\\test_case\\"
suite = unittest.defaultTestLoader.discover(test_dir, pattern="test_sqdwbg.py")
with open("..\\reports\\dwbgsq.html", 'wb+')as fp:
    HTMLTestRunner(stream=fp, title="测试报告", description="测试报告").run(suite)


# 将最新的测试报告放在jenkins上
ch = Change_file()
ch.cs_reports()

# ,retry=1