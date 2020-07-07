from selenium import webdriver
import os,time



class Uploading():
    def login(self):
        chromedriver = "C:/Google/Chrome/Application/chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)
        url = "https://github.com/grx200/lqxj/upload/master/reports"
        self.driver.get(url)
        self.driver.maximize_window()

    def sc(self):
        self.driver.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/div[2]/a[1]').click()
        self.driver.find_element_by_xpath('//*[@id="login_field"]').send_keys('grx200')
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys('grx124812')
        self.driver.find_element_by_xpath('//*[@id="login"]/form/div[4]/input[9]').click()
        self.driver.find_element_by_xpath('//*[@id="upload-manifest-files-input"]').send_keys(r'D:\grx_work\software\pycharm\lqgh\lqxj\reports\dwbgsq.html')
        time.sleep(10)
        self.driver.find_element_by_xpath('//*[@id="js-repo-pjax-container"]/div[3]/div/form/button').click()

if __name__ == '__main__':
    up = Uploading()
    up.login()
    up.sc()