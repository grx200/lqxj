from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

driver.get("https://www.baidu.com")

driver.maximize_window()
#定位相机按钮
driver.find_element_by_css_selector(".soutu-btn").click()
sleep(2)
#通过本地文件的绝对路径上传图片（r表示转移）
driver.find_element_by_css_selector(".upload-pic").send_keys(r"D:\grx_work\software\pycharm\lqgh\util\timg.jpg")

sleep(5)
driver.quit()