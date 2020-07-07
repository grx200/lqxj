# import unittest,paramunittest
# from common.excel_read import ExcelUtil
# from businessView.change_company import Change_company
# from common.desired_caps import open_browser
# from businessView.loginView import LoginView
# from common.common_fun import Common
# from common.myunit import  StartEnd
#
# file = '../data/test.xlsx'
# excel = ExcelUtil(file,"Sheet1")
# res = excel.next()
# res = tuple(res)
#
# @paramunittest.parametrized(*res)
#
# class testsq(StartEnd,Common):
#     def setParameters(self,sqrz,lxdhz,sfzhmz,yxz,sqsyz):
#         self.sqr = sqrz
#         self.lxdh = lxdhz
#         self.sfzhm = sfzhmz
#         self.yx = yxz
#         self.sqsy = sqsyz
#
#     def testcasesq(self):
#         l=LoginView(self.driver)
#         l.login_action('admin','123456')
#         l.check_loginStatus()
#         l.login_ghdwbg()
#         a = Change_company(self.driver)
#         a.apply(self.sqr,self.lxdh,self.sfzhm,self.yx,self.sqsy)
#
#
# if __name__ == '__main__':
#     unittest.main()


# import os
# file = open(r'D:\grx_work\basic_file\performance\sjcanshu\12.txt')
# a = file.read()
# c = a.count('响应断言')
# print(c)

# count = 3
#
# while count > 0:
#     username = input('username is:')
#     password = input('password is:')
#     if username != 'admin' or password != '123456':
#         print('worong username or password')
#         count = count -1
#         if count == 0:
#             print('no change')
#     else:
#         print('successful')
#         break


# height = float(input("输入身高（米）："))
# weight = float(input("输入体重（千克）："))
# bmi = weight / (height * height)  # 计算BMI指数
# if bmi < 18.5:
#     print("BMI指数为：" + str(bmi))
#     print("体重过轻")
# elif bmi >= 18.5 and bmi < 24.9:
#     print("BMI指数为：" + str(bmi))
#     print("正常范围，注意保持")
# elif bmi >= 24.9 and bmi < 29.9:
#     print("BMI指数为：" + str(bmi))
#     print("体重过重")
# else:
#     print("BMI指数为：" + str(bmi))
#     print("肥胖")


# import requests,json
#
#
# url1 = 'http://192.168.10.111:3000/uaa/oauth/token'
# data = {'username':'admin','password':'123456','grant_type':'password','scope':'app','client_id':'webApp','client_secret':'webApp'}
#
# response = requests.post(url=url1,data=data)
# print (response.status_code)

# def collatz(num):
#     if num
#     while True:

# def collatz():
#     while True:
#         try:
#             num=int(input('输入一个整数：'))
#         except ValueError:
#             print("输入的不是整数！")
#             continue
#         if num%2==0:
#             print('偶数')
#             while True:
#                 num = num/2
#                 if num == 1:
#                     print(num)
#                     break
#                 else:
#                     return num
#         else:
#             print('奇数')
#             num = num*3 + 1
#             return num
#         break
# if __name__ == '__main__':
#     c = collatz()
num=int(input('输入一个整数：'))
while True:
    if num%2==0:
        print('偶数')
        while True:
            num = num/2
            if num%2 == 0:
                continue
            else:
                break
        print(num)
        if num == 1:
            break
    else:
        print('奇数')
        num = num*3 + 1
        print(num)

# 判断数字奇偶
# def jiou(num):
#     while True:
