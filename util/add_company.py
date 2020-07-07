import random
from common.common_fun import Common
from selenium.webdriver.common.by import By
import time
from selenium .webdriver.support.select import Select
from common.desired_caps import open_browser
from businessView.loginView import LoginView
import logging


class Add_company(Common):
    # 新增管护单位用于管护单位变更
    tj = (By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[2]/div/div[1]/div[2]/div/button[3]')
    lqpkdm = (By.XPATH,'/html/body/div[9]/div[2]/div/div/div[2]/form/div/div[2]/div[1]/div[1]/div[1]/div/div/div/input')
    gbzntjsqk1 = (By.XPATH,'/html/body/div[9]/div[2]/div/div/div[2]/form/div/div[2]/div[1]/div[2]/div[1]/div/div/div/div/div/span')
    gbzntjsqk = (By.XPATH,'/html/body/div[4]/ul[2]/li[1]')
    xzqydm = (By.XPATH,'/html/body/div[9]/div[2]/div/div/div[2]/form/div/div[2]/div[1]/div[1]/div[2]/div/div/div/input')
    gbzntzb = (By.XPATH,'/html/body/div[9]/div[2]/div/div/div[2]/form/div/div[2]/div[1]/div[2]/div[2]/div/div/div/input')
    sjxzc = (By.XPATH,'/html/body/div[9]/div[2]/div/div/div[2]/form/div/div[2]/div[1]/div[3]/div[1]/div/div/div[1]/input')
    bzpbh = (By.XPATH,'/html/body/div[9]/div[2]/div/div/div[2]/form/div/div[2]/div[1]/div[3]/div[2]/div/div/div[1]/input')
    bhsjq = (By.XPATH,'/html/body/div[9]/div[2]/div/div/div[2]/form/div/div[2]/div[1]/div[4]/div[1]/div/div/div[1]/div/div/input')
    bhsjz = (By.XPATH,'/html/body/div[9]/div[2]/div/div/div[2]/form/div/div[2]/div[1]/div[4]/div[2]/div/div/div[1]/div/div/input')
    zrztlx1 = (By.XPATH,'/html/body/div[9]/div[2]/div/div/div[2]/form/div/div[2]/div[1]/div[5]/div[1]/div/div/div/div/div/span')
    zrztlx = (By.XPATH,'/html/body/div[7]/ul[2]/li[1]')
    zrztmc = (By.XPATH,'/html/body/div[9]/div[2]/div/div/div[2]/form/div/div[2]/div[1]/div[5]/div[2]/div/div/div[1]/input')
    zrztdbmc = (By.XPATH,'/html/body/div[9]/div[2]/div/div/div[2]/form/div/div[2]/div[1]/div[6]/div[1]/div/div/div[1]/input')
    zrdbzjlx1 = (By.XPATH,'/html/body/div[9]/div[2]/div/div/div[2]/form/div/div[2]/div[1]/div[6]/div[2]/div/div/div/div/div/span')
    zrdbzjlx = (By.XPATH,'/html/body/div[8]/ul[2]/li[2]')
    zrdbzjhm = (By.XPATH,'/html/body/div[9]/div[2]/div/div/div[2]/form/div/div[2]/div[1]/div[7]/div[1]/div/div/div/input')
    zrdblxfs = (By.XPATH,'/html/body/div[9]/div[2]/div/div/div[2]/form/div/div[2]/div[1]/div[7]/div[2]/div/div/div[1]/input')
    qdxz = (By.XPATH,'/html/body/div[9]/div[2]/div/div/div[3]/div/button[1]')

    def xinzeng(self):
        self.driver.find_element(*self.tj).click()
        time.sleep(1)
        self.driver.find_element(*self.lqpkdm).send_keys('123456789987654')
        self.driver.find_element(*self.xzqydm).send_keys('450221')
        self.driver.find_element(*self.gbzntjsqk1).click()
        self.driver.find_element(*self.gbzntjsqk).click()
        self.driver.find_element(*self.gbzntzb).send_keys('0.5')
        self.driver.find_element(*self.sjxzc).send_keys('哈哈村')
        self.driver.find_element(*self.bzpbh).send_keys('001')
        self.driver.find_element(*self.bhsjq).send_keys('2020-03-03')
        self.driver.find_element(*self.bhsjz).send_keys('2020-03-04')
        self.driver.find_element(*self.zrztlx1).click()
        self.driver.find_element(*self.zrztlx).click()
        ztmc = random.randint(1000,2000)
        self.driver.find_element(*self.zrztmc).send_keys(ztmc)
        self.driver.find_element(*self.zrztdbmc).send_keys('11')
        self.driver.find_element(*self.zrdbzjlx1).click()
        self.driver.find_element(*self.zrdbzjlx).click()
        self.driver.find_element(*self.zrdbzjhm).send_keys('123')
        self.driver.find_element(*self.zrdblxfs).send_keys('13999999999')
        time.sleep(8)
        self.driver.find_element(*self.qdxz ).click()
        logging.info('新增管护单位的责任主体名称是：%s'%ztmc)
        return ztmc

if __name__ == '__main__':
    driver=open_browser()
    l=LoginView(driver)
    l.login_action('admin','123456')
    l.login_ghdw()
    a = Add_company(driver)
    b = a.xinzeng()



