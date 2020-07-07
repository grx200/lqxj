import logging,os
import random
import time
from businessView.loginView import LoginView
from common.common_fun import Common,NoSuchElementException
from common.desired_caps import open_browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from common.common_fun import Common


class Change_person(Common):
    # 填写申请信息
    sq = (By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[1]/button[2]')
    sqr = (By.XPATH,'/html/body/div[10]/div[2]/div/div/div[2]/div/div/div/form[1]/div[1]/div[1]/div/div/div[1]/input')
    lxdh = (By.XPATH,'/html/body/div[10]/div[2]/div/div/div[2]/div/div/div/form[1]/div[1]/div[2]/div/div/div/input')
    sfzhm = (By.XPATH,'/html/body/div[10]/div[2]/div/div/div[2]/div/div/div/form[1]/div[2]/div[1]/div/div/div/input')
    yx = (By.XPATH,'/html/body/div[10]/div[2]/div/div/div[2]/div/div/div/form[1]/div[2]/div[2]/div/div/div/input')
    sqsy = (By.XPATH,'/html/body/div[10]/div[2]/div/div/div[2]/div/div/div/form[1]/div[3]/div/div/div/div/textarea')
    xyb1 = (By.XPATH,'/html/body/div[10]/div[2]/div/div/div[3]/div/button[3]')

    # 填写法人变更
    xzdw1 = (By.XPATH,'/html/body/div[10]/div[2]/div/div/div[2]/div/div/div/form[2]/div[1]/div[2]/button')
    chaxundw1 = (By.XPATH,'/html/body/div[10]/div[2]/div/div/div[2]/div/div/div/form[2]/div[7]/div/div[2]/div/div/div[2]/div/div[1]/div[2]/div/div/input')
    chaxundw2 = (By.XPATH,'/html/body/div[10]/div[2]/div/div/div[2]/div/div/div/form[2]/div[7]/div/div[2]/div/div/div[2]/div/div[1]/div[2]/div/div/i')
    xzdw2 = (By.XPATH,'/html/body/div[10]/div[2]/div/div/div[2]/div/div/div/form[2]/div[7]/div/div[2]/div/div/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr/td[5]/div/div/button[1]')
    zrztdbmc = (By.XPATH,'/html/body/div[10]/div[2]/div/div/div[2]/div/div/div/form[2]/div[2]/div[1]/div/div/div[1]/input')
    dblxfs = (By.XPATH,'/html/body/div[10]/div[2]/div/div/div[2]/div/div/div/form[2]/div[2]/div[2]/div/div/div/input')
    dbzjlx1 = (By.XPATH,'/html/body/div[10]/div[2]/div/div/div[2]/div/div/div/form[2]/div[3]/div[1]/div/div/div/div/div/i')
    ul = (By.XPATH,'/html/body/div[7]/ul[2]')
    li = (By.TAG_NAME,'li')


    # print(dbzjlx2)
    dbzjhm = (By.XPATH,'/html/body/div[10]/div[2]/div/div/div[2]/div/div/div/form[2]/div[3]/div[2]/div/div/div/input')
    dbzz = (By.XPATH,'/html/body/div[10]/div[2]/div/div/div[2]/div/div/div/form[2]/div[4]/div/div/div/div/input')
    bgsj = (By.XPATH,'/html/body/div[10]/div[2]/div/div/div[2]/div/div/div/form[2]/div[5]/div/div/div/div/div/div/input')
    bz = (By.XPATH,'/html/body/div[10]/div[2]/div/div/div[2]/div/div/div/form[2]/div[6]/div/div/div/div/textarea')
    xyb2 = (By.XPATH,'/html/body/div[10]/div[2]/div/div/div[3]/div/button[3]')

    # 上传附件
    fjlx1 = (By.XPATH,'/html/body/div[10]/div[2]/div/div/div[2]/div/div/div/div[2]/div[2]/div[1]/div[1]/div/div/div/i')
    fjlx2 = (By.XPATH,'/html/body/div[11]/ul[2]/li[1]')

    # fjul = (By.XPATH,'/html/body/div[11]/ul[2]')
    # fjli = (By.TAG_NAME,'li')

    fjsc = (By.XPATH,'/html/body/div[10]/div[2]/div/div/div[2]/div/div/div/div[2]/div[2]/div[1]/div[2]/div/div/input')
    qdsq = (By.XPATH,'/html/body/div[10]/div[2]/div/div/div[3]/div/button[4]')

    tbody = (By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[2]/table/tbody')
    tr = (By.TAG_NAME,'tr')


    # 审核法人变更申请
    shsq = (By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[2]/table/tbody/tr[1]/td[6]/div/div/button[2]')
    rwsh = (By.XPATH,'/html/body/div[5]/div[2]/div/div/div[1]/div/div[1]/div/div/div/div/div[5]')
    shyj = (By.XPATH,'/html/body/div[5]/div[2]/div/div/div[1]/div/div[2]/div[4]/div/form/div/div/div/textarea')
    shtg = (By.XPATH,'/html/body/div[5]/div[2]/div/div/div[2]/div/button[2]')

    sh_tbody = (By.XPATH,'/html/body/div[1]/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[2]/div/div[2]/table/tbody')
    sh_tr = (By.TAG_NAME,'tr')


    def apply(self,sqrz,lxdhz,sfzhmz,yxz,sqsyz,dwmc,zrztdbmcz,dblxfsz,dbzjhmz,dbzzz,bgsjz,bzz):
        num = self.driver.find_element(*self.tbody).find_elements(*self.tr)
        before_sqlen = len(num)
        print('之前有%d'%before_sqlen)


        # 申请信息
        self.driver.find_element(*self.sq).click()
        self.driver.find_element(*self.sqr).send_keys(sqrz)
        self.driver.find_element(*self.lxdh).send_keys(lxdhz)
        self.driver.find_element(*self.sfzhm).send_keys(sfzhmz)
        self.driver.find_element(*self.yx).send_keys(yxz)
        self.driver.find_element(*self.sqsy).send_keys(sqsyz)

        # 法人变更
        self.driver.find_element(*self.xyb1).click()
        self.driver.find_element(*self.xzdw1).click()
        self.driver.find_element(*self.chaxundw1).send_keys(dwmc)
        self.driver.find_element(*self.chaxundw2).click()
        self.driver.find_element(*self.xzdw2).click()
        self.driver.find_element(*self.zrztdbmc).send_keys(zrztdbmcz)
        self.driver.find_element(*self.dblxfs).send_keys(dblxfsz)
        self.driver.find_element(*self.dbzjlx1).click()

        size = self.driver.find_element(*self.ul).find_elements(*self.li)
        lenth = len(size)
        c = random.randint(1,lenth)
        self.dbzjlx2 = (By.XPATH,'/html/body/div[7]/ul[2]/li[%d]'%c)

        self.driver.find_element(*self.dbzjlx2).click()
        self.driver.find_element(*self.dbzjhm).send_keys(dbzjhmz)
        self.driver.find_element(*self.dbzz).send_keys(dbzzz)
        self.driver.find_element(*self.bgsj).send_keys(bgsjz)
        self.driver.find_element(*self.bz).send_keys(bzz)
        time.sleep(5)
        self.driver.find_element(*self.xyb2).click()

        # 附件上传
        self.driver.find_element(*self.fjlx1).click()

        # size1 = self.find_element(*self.fjul).find_elements(*self.fjli)
        # lenth = len(size1)
        # m = random.randint(1,lenth)
        # self.fjlx2 = (By.XPATH,'/html/body/div[11]/ul[2]/li[%d]'%m)

        time.sleep(2)
        self.driver.find_element(*self.fjlx2).click()
        time.sleep(2)
        print('正在上传')
        self.driver.find_element(*self.fjsc).send_keys(r'D:\grx_work\software\pycharm\lqgh\util\timg.jpg')
        print('上传完成')

        time.sleep(5)
        self.driver.find_element(*self.qdsq).click()

        time.sleep(3)
        num = self.driver.find_element(*self.tbody).find_elements(*self.tr)
        now_sqlen = len(num)
        print('现在有%d'%now_sqlen)

        if before_sqlen == now_sqlen:
            return True
        else:
            return False


    def audit(self,shyjz):
        be_shtr = self.driver.find_element(*self.sh_tbody).find_elements(*self.sh_tr)
        before_shlen = len(be_shtr)

        self.driver.find_element(*self.shsq).click()
        self.driver.find_element(*self.rwsh).click()
        self.driver.find_element(*self.shyj).send_keys(shyjz)
        time.sleep(3)
        self.driver.find_element(*self.shtg).click()

        no_shtr = self.driver.find_element(*self.sh_tbody).find_elements(*self.sh_tr)
        now_shlen = len(no_shtr)

        if before_shlen == now_shlen:
            return False
        else:
            return True





if __name__ == '__main__':
    driver=open_browser()
    l=LoginView(driver)
    l.login_action('admin','123456')
    # l.login_again()
    l.check_loginStatus()
    l.login_dwfrbg()
    a = Change_person(driver)
    a.apply('13','15823587415','340122200112057692','789@163.com','asd','1534','132','15823587415','132','4444','2020-03-03','123')
    # driver.quit()