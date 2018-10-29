import os,xlrd

class Config(object):
	def __init__(self):
		pass

	@staticmethod
	def data_dirs():
		BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
		DATA_DIRS = (
		os.path.join(BASE_DIR,  'data'),
		)
		d='/'.join(DATA_DIRS)
		return d


class DataHelper(object):
    def __init__(self):
        pass
    def readExcels(self):
        rows = []
        book = xlrd.open_workbook(Config.data_dirs() + "\summary.xlsx")
        #xlrd.open_workbook("E:/workspaces/EAInterface/testcase/%s.xlsx" % pyfile)
        sheet = book.sheet_by_index(0)
        for row in range(1,sheet.nrows):
			# 类似切片的操作，参数：row, startInx, endInx ，返回一个list：[70.0, 69.0]
			# a0=sheet.row_values(row,0,sheet.ncols)
			# a =list(a0)
			# rows.append(a)
			# print(a0)
            rows.append(list(sheet.row_values(row,0,sheet.ncols)))
        return rows



if __name__ == '__main__':
    w = DataHelper()
    L = w.readExcels()
    print(L)
