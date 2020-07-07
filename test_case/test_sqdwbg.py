import unittest,paramunittest
from common.excel_read import ExcelUtil
from businessView.change_company import Change_company
from common.desired_caps import open_browser
from businessView.loginView import LoginView
from common.common_fun import Common
from common.myunit import  StartEnd
from util.add_company import Add_company
import logging
from selenium.common.exceptions import NoSuchElementException,ElementClickInterceptedException
import time


file = '../data/test.xlsx'
excel = ExcelUtil(file,"Sheet1")
res = excel.next()
res = tuple(res)
# print(res)

@paramunittest.parametrized(*res)

class Testsq(StartEnd,Common):
    def setParameters(self,sqrz,lxdhz,sfzhmz,yxz,sqsyz,ghdwmcz,zrztdbmcz,dblxfsz,dbzjhmz,dbzzz,bgsjz):
        # 填写申请信息需要的参数
        self.sqr = sqrz
        self.lxdh = lxdhz
        self.sfzhm = sfzhmz
        self.yx = yxz
        self.sqsy = sqsyz

        # 变更单位需要的参数
        self.ghdwmc = ghdwmcz
        self.zrztdbmc = zrztdbmcz
        self.dblxfs = dblxfsz
        self.dbzjhm = dbzjhmz
        self.dbzz = dbzzz
        self.bgsj = bgsjz



    def test_casesq(self):
        l=LoginView(self.driver)
        l.login_action('admin','123456')
        l.check_loginStatus()
        l.login_ghdw()
        a = Add_company(self.driver)
        ztmc = a.xinzeng()
        l.login_ghdwbg()
        try:
            a = Change_company(self.driver)
            if a.apply(self.sqr,self.lxdh,self.sfzhm,self.yx,self.sqsy,ztmc,self.ghdwmc,self.zrztdbmc,self.dblxfs,self.dbzjhm,self.dbzz,self.bgsj) == False:
                time.sleep(0.1)
                logging.info('Application_Failed!')
                self.getScreenShot('application')
                self.assertTrue(False)
                raise


        except NoSuchElementException:
            logging.info('Application_Failed!')
            self.getScreenShot('application')
            self.assertTrue(False)
            raise

        except ElementClickInterceptedException:
            logging.info('Application_Failed!')
            self.getScreenShot('application')
            self.assertTrue(False)
            raise

        else:
            logging.info('Application_Succeed!')



if __name__ == '__main__':
    unittest.main()