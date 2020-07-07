# def debug():
#     import inspect
#     caller_name = inspect.stack()[1][3]
#     print(caller_name)
#     print( "[DEBUG]: enter {}()".format(caller_name))
#
# def say_hello():
#     debug()
#     print("hello!")
#
# def say_goodbye():
#     debug()
#     print("goodbye!")
#
# if __name__ == '__main__':
#     say_hello()
#     say_goodbye()

# dic = {'xm':'小明','nl':'18','mz':'汉族'}
# # for i in range(len(dic.keys())):
# key = list(dic.keys())
# print(key)

# data = [{'xm':'小明','nl':'18','mz':'汉族'},{'xm':'小红','nl':'11','mz':'诺克'}]
# print(data[0])

# dic = {'xm':'小明','nl':'18','mz':'汉族'}
# values = dic['xm']
# print(values)
# import xlwt
# # 创建一个workbook 设置编码
# workbook = xlwt.Workbook(encoding = 'utf-8')
# # 创建一个worksheet
# worksheet = workbook.add_sheet('My Worksheet')
#
# # 写入excel
# # 参数对应 行, 列, 值
# worksheet.write(0,0, label = )
#
# # 保存
# workbook.save('..\\data\\haha.xlsx')
str = '132dascshh1'
a = len(str)
str1 = str[a-3:a-1]
print(str1)
