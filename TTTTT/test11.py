import xlrd
def read_excel(path,sheet):
    data = xlrd.open_workbook(path)
    table = data.sheet_by_name(sheet)
    fist = table.row(0)
    nrows = table.nrows
    key_lis = []
    values_lis = []
    dic = {}
    for i in range(len(fist)):
        key = str(fist[i]).split("'")[1]
        key_lis += [key]

    for i in range(1,nrows):
        values = table.row(i)
        for j in range(len(fist)):
            value = str(values[j]).split("'")[1]
            ke = key_lis[j]
            dic[ke] = value
    print(dic)





path = "..\\data\\test.xlsx"
sheet = "Sheet1"
re = read_excel(path,sheet)