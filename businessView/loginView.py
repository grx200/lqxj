import logging
import time
from common.common_fun import Common,NoSuchElementException
from common.desired_caps import open_browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
class LoginView(Common):
    username_type=(By.ID,'username')
    password_type=(By.ID,'password')
    loginBtn=(By.NAME,'submit')
    loginCheck=(By.XPATH,'/html/body/div[1]/div[1]/div/div[3]/ul/li[1]')
    userBtn=()
    logoutBtn=()
    def login_action(self,username,password):

        logging.info('============login_action==============')
        logging.info('username is:%s' %username)
        self.driver.find_element(*self.username_type).send_keys(username)

        logging.info('password is:%s'%password)
        self.driver.find_element(*self.password_type).send_keys(password)

        logging.info('click loginBtn')
        self.driver.find_element(*self.loginBtn).click()
        logging.info('login finished!')

    # def login_again(self):
    #     url = 'http://192.168.10.24:3001/dist/index.html#/'
    #     self.driver.get(url)
    #     time.sleep(4)
    #     self.driver.find_element(By.XPATH,'/html/body/div[4]/div[2]/div/div/div/div/div[3]/button').click()
    #     self.driver.find_element(By.ID,'username').send_keys('admin')
    #     self.driver.find_element(By.ID,'password').send_keys('123456')
    #     self.driver.find_element(By.NAME,'submit').click()

    def check_loginStatus(self):
        logging.info('====check_loginStatus======')

        try:
            element = self.driver.find_element(*self.loginCheck)
        except NoSuchElementException:
            logging.error('login Fail!')
            self.getScreenShot('login')
            return False
        else:
            logging.info('login success!')
            return True

    def login_ghdwbg(self):
        url = 'http://192.168.10.24:3001/dist/index.html#/lqgh/ghdwbg'
        self.driver.get(url)

    def login_ghdw(self):
        url = 'http://192.168.10.24:3001/dist/index.html#/sjzx/ghdw/ghdw'
        self.driver.get(url)

    def login_dwfrbg(self):
        url = 'http://192.168.10.24:3001/dist/index.html#/lqgh/ghzrrbg'
        self.driver.get(url)


if __name__ == '__main__':
    driver=open_browser()
    l=LoginView(driver)
    l.login_action('admin','123456')
    # l.login_again()
    l.check_loginStatus()