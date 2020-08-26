import xlrd
import xlwt
import re
data = xlrd.open_workbook(r'灯带/ddc5-14log.xlsx')
key: str = 'TST'
#the column number to match
colNumber = 0

#the number of columns in sheet
totalColumns = data.sheets()[0].ncols
#the number of lines in sheet
totalRows = data.sheets()[0].nrows

orgTable = data.sheets()[0]
newBook = xlwt.Workbook(encoding='utf-8' , style_compression = 0)
newTable = newBook.add_sheet('Sheet1',True)
count = 0
newLineNum = 0
for i in range(0,totalRows):
    if re.search(key,(orgTable.cell(i,colNumber).value)):
        for j in range(0,totalColumns):
            newTable.write(newLineNum,j,orgTable.cell(i,j).value)
        newLineNum += 1
newBook.save('灯带/resultTST.xlsx')
