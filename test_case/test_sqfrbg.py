import unittest,paramunittest
from common.excel_read import ExcelUtil
from businessView.change_person import Change_person
from common.desired_caps import open_browser
from businessView.loginView import LoginView
from common.common_fun import Common
from common.myunit import  StartEnd
from util.add_company import Add_company
import logging
from selenium.common.exceptions import NoSuchElementException,ElementClickInterceptedException,ElementNotInteractableException
import time


file = '../data/dwfrbg.xlsx'
excel = ExcelUtil(file,"Sheet1")
res = excel.next()
res = tuple(res)
# print(res)

@paramunittest.parametrized(*res)

class Test_sqfrbg(StartEnd,Common):
    def setParameters(self,sqrz,lxdhz,sfzhmz,yxz,sqsyz,zrztdbmcz,dblxfsz,dbzjhmz,dbzzz,bgsjz,bzz,shyjz):
        self.sqr = sqrz
        self.lxdh = lxdhz
        self.sfzhm = sfzhmz
        self.yx = yxz
        self.sqsy = sqsyz

        # 法人变更需要参数
        self.zrztdbmc = zrztdbmcz
        self.dblxfs = dblxfsz
        self.dbzjhm = dbzjhmz
        self.dbzz = dbzzz
        self.bgsj = bgsjz
        self.bzz = bzz

        # 审核意见
        self.shyj = shyjz


    def test_casesq(self):
        l=LoginView(self.driver)
        l.login_action('admin','123456')
        l.check_loginStatus()
        l.login_ghdw()
        a = Add_company(self.driver)
        dwmc = a.xinzeng()
        l.login_dwfrbg()
        try:
            a = Change_person(self.driver)
            if a.apply(self.sqr,self.lxdh,self.sfzhm,self.yx,self.sqsy,dwmc,self.zrztdbmc,self.dblxfs,self.dbzjhm,self.dbzz,self.bgsj,self.bzz) == True:
                time.sleep(1)
                logging.info('Application_Failed!')
                self.getScreenShot('application')
                self.assertTrue(False)
                raise

        except ElementClickInterceptedException:
            logging.info('Application_Failed!')
            self.getScreenShot('application')
            self.assertTrue(False)
            raise

        except ElementNotInteractableException:
            logging.info('Application_Failed!')
            self.getScreenShot('application')
            self.assertTrue(False)
            raise
        else:
            logging.info('Application_Succeed!')
            logging.info('Begin_Audits')
            try:
                if a.audit(self.shyj) == True:
                    time.sleep(1)
                    logging.info('Audit_Failed!')
                    self.getScreenShot('audit')
                    self.assertTrue(False)
                    raise

            except ElementClickInterceptedException:
                logging.info('Audit_Failed!')
                self.getScreenShot('audit')
                self.assertTrue(False)
                raise

            except ElementNotInteractableException:
                logging.info('Audit_Failed!')
                self.getScreenShot('audit')
                self.assertTrue(False)
                raise

            else:
                logging.info('Audit_Succeed!')




if __name__ == '__main__':
    unittest.main()