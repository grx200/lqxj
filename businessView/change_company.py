import logging,os
import random
import time
from businessView.loginView import LoginView
from common.common_fun import Common,NoSuchElementException
from common.desired_caps import open_browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from common.common_fun import Common


class Change_company(Common):
    # 申请管护单位变更
    # 申请信息页面中的元素
    sq = (By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[1]/button[2]')
    sqr = (By.XPATH,'/html/body/div[13]/div[2]/div/div/div[2]/div/div/div/div[2]/form/div[1]/div[1]/div/div/div/input')
    lxdh = (By.XPATH,'/html/body/div[13]/div[2]/div/div/div[2]/div/div/div/div[2]/form/div[1]/div[2]/div/div/div/input')
    sfzhm = (By.XPATH,'/html/body/div[13]/div[2]/div/div/div[2]/div/div/div/div[2]/form/div[2]/div[1]/div/div/div[1]/input')
    yx = (By.XPATH,'/html/body/div[13]/div[2]/div/div/div[2]/div/div/div/div[2]/form/div[2]/div[2]/div/div/div/input')
    sqsy = (By.XPATH,'/html/body/div[13]/div[2]/div/div/div[2]/div/div/div/div[2]/form/div[3]/div/div/div/div/textarea')
    xyb1 = (By.XPATH,'/html/body/div[13]/div[2]/div/div/div[3]/div/button[3]')


    # 变更前面需要选 需要变更的单位
    xz1 = (By.XPATH,'/html/body/div[13]/div[2]/div/div/div[2]/div/div/div/div[3]/form/div/div/div/div/button')
    chaxunzrr = (By.XPATH,'/html/body/div[13]/div[2]/div/div/div[2]/div/div/div/div[3]/div/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div[2]/div/div/input')
    chaxunbtn = (By.XPATH,'/html/body/div[13]/div[2]/div/div/div[2]/div/div/div/div[3]/div/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div[2]/div/div/i')
    xz2 = (By.XPATH,'/html/body/div[13]/div[2]/div/div/div[2]/div/div/div/div[3]/div/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr/td[5]/div/div/button[1]')
    bg = (By.XPATH,'/html/body/div[13]/div[2]/div/div/div[2]/div/div/div/div[3]/div/div[1]/div[2]/div/div/div[2]/table/tbody/tr/td[4]/div/div/button')
    ghdwmc = (By.XPATH,'/html/body/div[12]/div[2]/div/div/div[2]/form/div[1]/div[1]/div/div/div[1]/input')
    ghztlx1 = (By.XPATH,'/html/body/div[12]/div[2]/div/div/div[2]/form/div[1]/div[3]/div/div/div/div/div/i')
    ghztlx2 = (By.XPATH,'/html/body/div[8]/ul[2]/li[1]')
    zrztdbmc = (By.XPATH,'/html/body/div[12]/div[2]/div/div/div[2]/form/div[2]/div[1]/div/div/div[1]/input')
    dblxfs = (By.XPATH,'/html/body/div[12]/div[2]/div/div/div[2]/form/div[2]/div[2]/div/div/div[1]/input')
    dbzjlx1 = (By.XPATH,'/html/body/div[12]/div[2]/div/div/div[2]/form/div[3]/div[1]/div/div/div/div/div/i')
    dbzjlx2 = (By.XPATH,'/html/body/div[9]/ul[2]/li[2]')
    dbzjhm = (By.XPATH,'/html/body/div[12]/div[2]/div/div/div[2]/form/div[3]/div[2]/div/div/div/input')
    dbzz = (By.XPATH,'/html/body/div[12]/div[2]/div/div/div[2]/form/div[4]/div/div/div/div/input')
    bgsj = (By.XPATH,'/html/body/div[12]/div[2]/div/div/div[2]/form/div[5]/div/div/div/div/div/div/input')
    bgqd = (By.XPATH,'/html/body/div[12]/div[2]/div/div/div[3]/div/button[2]')
    xyb2 = (By.XPATH,'/html/body/div[13]/div[2]/div/div/div[3]/div/button[3]')

    # 附件上传
    # 选择附件类型
    fjlx1 = (By.XPATH,'/html/body/div[13]/div[2]/div/div/div[2]/div/div/div/div[4]/div[2]/div[1]/div[1]/div')
    fjlx2 = (By.XPATH,'/html/body/div[14]/ul[2]/li[1]')
    sqqd = (By.XPATH,'/html/body/div[13]/div[2]/div/div/div[3]/div/button[4]')
    scfj = (By.XPATH,'/html/body/div[13]/div[2]/div/div/div[2]/div/div/div/div[4]/div[2]/div[1]/div[2]/div/div/input')

    # 管护变更页面中的元素
    # xz = (By.XPATH,'/html/body/div[13]/div[2]/div/div/div[2]/div/div/div/div[3]/form/div/div/div/div/button')

    # 获取当前有多少行申请，为了查看申请完成后，行数是否有变化
    tbody = (By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[2]/table/tbody')
    tr = (By.TAG_NAME,'tr')


    def apply(self,sqrz,lxdhz,sfzhmz,yxz,sqsyz,mc,ghdwmcz,zrztdbmcz,dblxfsz,dbzjhmz,dbzzz,bgsjz):
        # 查看当前有多少行tr
        size = self.driver.find_element(*self.tbody).find_elements(*self.tr)
        before_length = len(size)
        # print(before_length)
        # print(type(before_length))

        # 填写申请信息
        time.sleep(3)
        self.driver.find_element(*self.sq).click()
        time.sleep(1)
        self.driver.find_element(*self.sqr).send_keys(sqrz)
        self.driver.find_element(*self.lxdh).send_keys(lxdhz)
        self.driver.find_element(*self.sfzhm).send_keys(sfzhmz)
        self.driver.find_element(*self.yx).send_keys(yxz)
        self.driver.find_element(*self.sqsy).send_keys(sqsyz)
        time.sleep(2)
        self.driver.find_element(*self.xyb1).click()
        time.sleep(5)

        # 填写管护变更
        self.driver.find_element(*self.xz1).click()
        self.driver.find_element(*self.chaxunzrr).send_keys(mc)
        time.sleep(3)
        self.driver.find_element(*self.chaxunbtn).click()
        self.driver.find_element(*self.xz2).click()
        self.driver.find_element(*self.bg).click()
        self.driver.find_element(*self.ghdwmc).send_keys(ghdwmcz)
        self.driver.find_element(*self.ghztlx1).click()
        self.driver.find_element(*self.ghztlx2).click()
        self.driver.find_element(*self.zrztdbmc).send_keys(zrztdbmcz)
        self.driver.find_element(*self.dblxfs).send_keys(dblxfsz)
        self.driver.find_element(*self.dbzjlx1).click()
        self.driver.find_element(*self.dbzjlx2).click()
        self.driver.find_element(*self.dbzjhm).send_keys(dbzjhmz)
        self.driver.find_element(*self.dbzz).send_keys(dbzzz)
        self.driver.find_element(*self.bgsj).send_keys(bgsjz)
        time.sleep(5)
        self.driver.find_element(*self.bgqd).click()
        time.sleep(2)
        self.driver.find_element(*self.xyb2).click()
        self.driver.find_element(*self.fjlx1).click()
        time.sleep(2)
        self.driver.find_element(*self.fjlx2).click()
        # self.driver.find_element(*self.scfj).click()
        time.sleep(1)
        self.driver.find_element(*self.scfj).send_keys(r'D:\grx_work\software\pycharm\lqgh\util\timg.jpg')
        time.sleep(2)
        self.driver.find_element(*self.sqqd).click()

        # 查看现在有多少条申请
        size = self.driver.find_element(*self.tbody).find_elements(*self.tr)
        now_length = len(size)
        print(now_length)
        print(type(now_length))

        if before_length != now_length:
            return True
        else:
            return False

    def audit(self):
        pass


if __name__ == '__main__':
    driver=open_browser()
    l=LoginView(driver)
    l.login_action('admin','123456')
    # l.login_again()
    l.check_loginStatus()
    l.login_ghdwbg()
    a = Change_company(driver)
    a.apply('哈哈','13999999999','340122200112057000','789@163.com','101')
    driver.quit()