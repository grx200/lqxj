class BaseView(object):
    def __init__(self,driver):
        self.driver=driver
        self.driver.implicitly_wait(10)


    def find_element(self,*loc):
        return self.driver.find_element(*loc)

    def find_elements(self,*loc):
        return self.driver.find_elements(*loc)
