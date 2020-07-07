import random
from common.common_fun import Common
from selenium.webdriver.support.wait import WebDriverWait

class judge():
    a = random.randint(1,100)
    b = random.randint(25,75)
    def bijiao(self):
        print(self.a,self.b)
        if self.a > self.b:
            return True
        else:
            return False

if __name__ == '__main__':
    j = judge()
    j.bijiao()
    if j.bijiao() == True:
        print('1')
    else:
        print('2')
