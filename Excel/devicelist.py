import xlrd
import xlwt
import re
#data in the original excel file name.
#data = xlrd.open_workbook(r'27/resultheart27.xlsx')
#data = xlrd.open_workbook(r'27/result272B.xlsx')

#多路控制器
# list=['00124B001B580DB4',
#       '00124B001C26E32B',
#       '00124B001B580DC2',
#       '00124B001BBC7024',
#       '00124B001C26E1D0',
#       '00124B001C26E276',
#       '00124B001C26E409',
#       '00124B001BBC7F37',
#       '00124B001B5923E1',
#       '00124B001B58179F',
#       '00124B001C26E07D',
#       '00124B001C26E26C',
#       '00124B001C26E375',
#       '00124B001BBC6E91',
#       '00124B001BBC6EB2',
#       '00124B001B581783',
#       '00124B001BBC6EFD',
#       '00124B001BBC8694',
#       '00124B001C26E2AB',
#       '00124B001BBC9C98',
#       '00124B001C26E39B',
#       '00124B001D133126',
#       '00124B001C26E3E2',
#       '00124B001B580DA8',
#       '00124B001C26E181',
#       '00124B001C26E29B',
#       '00124B001C26E168',
#       '00124B001D13303A',
#       '00124B001C26E43E',
#       '00124B001B580DE7']
#插卡取电
# list=[
# #     '00124B001D36F7FE',
# #     '00124B001D37689C',
# #     '00124B001D376879',
# #     '00124B001D369128',
# #     '00124B001D376887',
# #     '00124B001D36F7C9'
# # ]

#灯带
list=[
    '35D1A4C1386A2D2F',
    '2001A4C1384E579A',
    '2001A4C1384A43C1',
    '35D1A4C1386A8238',
    '2001A4C1384AD6CC',
    '2001A4C1384ABBC1',
    '2001A4C1384F1797',
    '35D1A4C1386AD113',
    '2001A4C1384E909C',
    '35D1A4C1386AB61A',
    '35D1A4C1386A9F1B',
    '2001A4C1384E229C',
    '2001A4C1384E2695',
    '2001A4C13852EE26',
    '2001A4C1384E4A96',
    '2001A4C1384E4496',
    '2001A4C1384AD1C1',
    '35D1A4C1386AB91A',
    '2001A4C1384E7796',
    '35D1A4C1386AB81A',
]
for key in list:
    data = xlrd.open_workbook(r'灯带/resultheart.xlsx')
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
    newBook.save('灯带/result%s.xlsx'%key)

