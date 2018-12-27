import xlrd
import xlwt
from datetime import datetime, date
from xlrd import xldate_as_tuple

# 打开Excel表格，参数是文件路径
data = xlrd.open_workbook('C://Users//Test Engineer//Desktop//test 1.xlsx', formatting_info=True)

# 通过索引顺序获取表的三种方法
# table = data.sheets()[0]
table = data.sheet_by_index(0)
# table = data.sheet_by_name('Sheet1')

# 获取行或列的值
print(table.row_values(1))
print(table.col_values(3))

# 获取单元格内容
print(table.cell(1, 0).value.encode('utf-8'))
print(table.cell_value(1, 0).encode('utf-8'))
print(table.row(2)[0].value.encode('utf-8'))

# 获取单元格的数据类型
print(table.cell(3, 5).ctype)

# python读取excel中单元格的内容返回的有5种类型，即上面例子中的ctype:
# ctype :  0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error

# 处理时间格式
row = table.nrows
col = table.ncols
if table.cell(row, col).ctype == 3:
    date_value = xlrd.xldate_as_tuple(table.cell_value(row, 4), book.datemode)
    date_tmp = date(*date_value[:3]).strftime('%Y/%M/%D')

# 处理合并单元格的内容
# 只能获取合并单元格的第一个cell的行列索引，才能读到值，读错了就是空值。
print(table.merged_cells)

'''class ExcelRead:
    def __init__(self, excel_path, sheet_name):
        self.data = xlrd.open_workbook('C://Users//Test Engineer//Desktop//test 1.xlsx')
        self.table = self.data.sheet_by_name('Sheet1')
        # 获取第一行作为key值
        self.keys = self.table.row_values(0)
        # 获取总行数
        self.rowNum = self.table.nrows
        # 获取总列数
        self.colNum = self.table.ncols

    def dict_data(self):
        if self.rowNum <= 1:
            print('总行数小于等于1')
        else:
            r = []
            j = 1
            for i in range(self.rowNum - 1):
                s = {}
                # 从第二行取对应values值
                values = self.table.row_values(j)
                for x in range(self.colNum):
                    s[self.keys[x]] = values[x]
                r.append(s)
                j += 1
            return r'


if __name__ == "__main__":
    filePath = "C://Users//Test Engineer//Desktop//test 1.xlsx"
    sheetName = "Sheet1"
    data = ExcelRead(filePath, sheetName)
    print(data.dict_data())'''
