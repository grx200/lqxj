import subprocess
import xlrd
from baseView.baseView import BaseView
from common.desired_caps import open_browser
from selenium.common.exceptions import NoSuchElementException
import logging
from selenium.webdriver.common.by import By
import time,os
import csv

class Common(BaseView):
    def getTime(self):
        self.now=time.strftime("%Y-%m-%d %H_%M_%S")
        return self.now

    def getScreenShot(self,model):
        logging.info("get screenshot %s failed"%model)

        timestrmap = time.strftime('%Y%m%d_%H.%M.%S')
        imgPath = os.path.join('..\screenshots', '%s.png' % str(timestrmap))
        self.driver.save_screenshot(imgPath)
        print('screenshot:', timestrmap, '.png' )

    def get_csv_data(self,csv_file,line):
        logging.info('=====get_csv_data======')
        with open(csv_file,'r',encoding='utf-8-sig') as file:
            reader=csv.reader(file)
            for index,row in enumerate(reader,1):
                if index==line:
                    return row
    def fast_input(self,str,element):
    #####'快速输入'######
        x = subprocess.check_output('adb devices', shell=True).decode()
        x= x.split('\n')[1][:-7]
        element.click()
        time.sleep(0.3)
        subprocess.Popen('adb -s %s shell input text %s'%(x,str), shell=True)
        time.sleep(0.5)
    def editClear(self,text):
    ###直接使用clear()太慢了的话，可以使用这个方法####
    #     123代表光标移动到末尾
        self.driver.keyevent(123)
        for i in range(0, len(text)):
            #67退格键
            self.driver.keyevent(67)
    def get_result(self,file,column):
        data = xlrd.open_workbook(file)
        sheet = data.sheet_by_index(0)
        nrows = sheet.nrows
        ncols = sheet.ncols
        li1 = []
        for i in range(1,nrows):#第0行为表头
            alldata = sheet.row_values(i)#循环输出excel表中每一行，即所有数据
            li1.append(alldata[column])
        return li1
    def getSize(self):                               #获取当前的width和height的x、y的值
        x = driver.get_window_size()['width']   #width为x坐标
        y = driver.get_window_size()['height']  #height为y坐标
        return (x, y)
    def swipeDown(self):    #向下滑动swipedown
        x = driver.get_window_size()['width']   #width为x坐标
        y = driver.get_window_size()['height']
        x1 = int(x * 0.5)
        y1 = int(y * 0.25)
        y2 = int(y * 0.75)
        driver.swipe(x1, y1, x1, y2,500)




if __name__ == '__main__':
    driver=open_browser()
