import xlrd
import xlwt
import re
import time
#多路控制器
# list=['result00124B001B580DB4',
#       'result00124B001C26E32B',
#       'result00124B001B580DC2',
#       'result00124B001BBC7024',
#       'result00124B001C26E1D0',
#       'result00124B001C26E276',
#       'result00124B001C26E409',
#       'result00124B001BBC7F37',
#       'result00124B001B5923E1',
#       'result00124B001B58179F',
#       'result00124B001C26E07D',
#       'result00124B001C26E26C',
#       'result00124B001C26E375',
#       'result00124B001BBC6E91',
#       'result00124B001BBC6EB2',
#       'result00124B001B581783',
#       'result00124B001BBC6EFD',
#       'result00124B001BBC8694',
#       'result00124B001C26E2AB',
#       'result00124B001BBC9C98',
#       'result00124B001C26E39B',
#       'result00124B001C26E3E2',
#       'result00124B001B580DA8',
#       'result00124B001C26E181',
#       'result00124B001C26E29B',
#       'result00124B001C26E168',
#       'result00124B001D13303A',
#       'result00124B001C26E43E',
#       'result00124B001B580DE7',
#       'result00124B001D133126',]

#灯带
list=[
    'result35D1A4C1386A2D2F',
    'result2001A4C1384E579A',
    'result2001A4C1384A43C1',
    'result35D1A4C1386A8238',
    'result2001A4C1384AD6CC',
    'result2001A4C1384ABBC1',
    'result2001A4C1384F1797',
    'result35D1A4C1386AD113',
    'result2001A4C1384E909C',
    'result35D1A4C1386AB61A',
    'result35D1A4C1386A9F1B',
    'result2001A4C1384E229C',
    'result2001A4C1384E2695',
    'result2001A4C13852EE26',
    'result2001A4C1384E4A96',
    'result2001A4C1384E4496',
    'result2001A4C1384AD1C1',
    'result35D1A4C1386AB91A',
    'result2001A4C1384E7796',
    'result35D1A4C1386AB81A',
]
for item in list:
    key='message'
    filename='灯带/%s.xlsx'%item
    data = xlrd.open_workbook(filename)

    #data = xlrd.open_workbook(r'27/resultheart27.xlsx')
    colNumber = 0
    # the number of columns in sheet
    totalColumns = data.sheets()[0].ncols
    # the number of lines in sheet
    totalRows = data.sheets()[0].nrows

    orgTable = data.sheets()[0]
    newBook = xlwt.Workbook(encoding='utf-8', style_compression=0)
    newTable = newBook.add_sheet('Sheet1', True)
    count = 0
    newLineNum = 0
    for i in range(0, totalRows):
        if re.search(key, (orgTable.cell(i, colNumber).value)):
            for j in range(0, totalColumns):
                newTable.write(newLineNum, j, orgTable.cell(i, j).value)
            newLineNum += 1
    newBook.save('灯带/%s.xlsx'%item)