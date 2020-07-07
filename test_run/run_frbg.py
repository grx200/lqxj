import unittest
from common.HTMLTestRunner import HTMLTestRunner


test_dir = "..\\test_case\\"
suite = unittest.defaultTestLoader.discover(test_dir, pattern="test_sqfrbg.py")
with open("..\\reports\\frbgsq.html", 'wb+')as fp:
    HTMLTestRunner(stream=fp, title="测试报告", description="测试报告").run(suite)