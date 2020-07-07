import unittest
from common.desired_caps import open_browser
import logging
from time import sleep

# class StartEnd(unittest.TestCase):
#     def setUp(self):
#         logging.info('=====setUp====')
#         self.driver=open_browser()
#
#     def tearDown(self):
#         self.driver.quit()

class StartEnd(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = open_browser()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def add_img(self):
        self.imgs.append(self.driver.get_screenshot_as_base64())
        return True

    def setUp(self):
        # 在是python3.x 中，如果在这里初始化driver ，因为3.x版本 unittest 运行机制不同，会导致用力失败时截图失败
        self.imgs = []
        self.addCleanup(self.cleanup)

    def cleanup(self):
        pass