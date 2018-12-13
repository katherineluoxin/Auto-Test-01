import xlrd
import xlwt
from datetime import datetime, date


'''# 打开Excel表格，参数是文件路径
data = xlrd.open_workbook('C://Users//Test Engineer//Desktop//test 1.xlsx')

# 通过索引顺序获取表的三种方法
# table = data.sheets()[0]
# table = data.sheet_by_index(0)
table = data.sheet_by_name('Sheet1')

# 获取第一行或第一列的值
print(table.row_values(1))
print(table.col_values(2))

# 获取单元格内容
 table.cell(1, 0).value.encode('utf-8')
 table.cell_value(1, 0).encode('utf-8')
 table.row(1)[0].value.encode('utf-8')'''


class ExcelRead:
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
            return r


if __name__ == "__main__":
    filePath = "C://Users//Test Engineer//Desktop//test 1.xlsx"
    sheetName = "Sheet1"
    data = ExcelRead(filePath, sheetName)
    print(data.dict_data())
