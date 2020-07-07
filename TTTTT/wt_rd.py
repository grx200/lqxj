# lis = [17,255,78,89,11]
# len = len(lis)
# for i in range(len):
#     for j in range (0,len-i-1):
#         if lis[j] > lis[j+1]:
#             lis[j],lis[j+1] = lis[j+1],lis[j]
#
#     print(lis)


# 将列表中的字典写入excel中
import xlwt

def data_write(file_path, datas):
    workbooks = xlwt.Workbook(encoding='utf-8')
    sheet1 = workbooks.add_sheet(u'工作表1',cell_overwrite_ok=True) #创建sheet
    dic = datas[0]
    # 得到键名key 就是把它写入第一行
    key = list(dic.keys())
    for i in range(len(key)):
        sheet1.write(0,i,key[i])

    # 得到每个字典中的vluses，陆续写到后面每排
    for j in range(len(datas)):
        zd = datas[j]
        print(zd)
        key = list(zd.keys())
        print(key)
        for i in range(len(key)):
            values = datas[j][key[i]]
            sheet1.write(j+1,i,values)

    workbooks.save(file_path) #

if __name__ == '__main__':
    data = [{'xm':'小明','nl':'18','mz':'汉族','xb':'男'},{'xm':'小红','nl':'11','mz':'诺克','xb':'女'}]
    path = '../data/ces.xlsx'
    data_write(file_path=path,datas=data)


# import xlrd
#
# def data_read(path,sheet):
#     data = xlrd.open_workbook(path)
#     table = data.sheet_by_name(sheet)
#     key = table.row(0)
#     lis = []
#     dic = {}
#     li = []
#     nrows = table.nrows
#     for i in range(len(key)):
#         s = str(key[i])
#         liem = s.split("'")[1]
#         lis = lis + [liem]
#     print(lis)
#
#     for j in range(1,nrows):
#         values = table.row(j)
#         for m in range(len(values)):
#             s = str(values[m])
#             va = s.split("'")[1]
#             dic[lis[m]] = va
#         li = li + [dic]
#     print(li)
#
# if __name__ == '__main__':
#     pa = '..\\data\\ces.xlsx'
#     sh = '工作表1'
#     data_read(pa,sh)


