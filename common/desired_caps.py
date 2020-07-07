from selenium import webdriver
import logging
import logging.config
import os
from os import path

# CON_LOG='../config/log.conf'
# logging.config.fileConfig(CON_LOG)
# logging=logging.getLogger()

log_file_path = path.join(path.dirname(path.abspath(__file__)), '../config/log.conf')
logging.config.fileConfig(log_file_path)
logger = logging.getLogger()

def open_browser():
    chromedriver = "C:/Google/Chrome/Application/chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)
    url = "http://192.168.10.24:7081/cas/login?service=http%3A%2F%2F192.168.10.24%3A8081%2Fdzzw%2Flogin%2Fcas"
    driver.get(url)
    driver.maximize_window()
    return driver

if __name__ == '__main__':
    open_browser()