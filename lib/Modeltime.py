import xlrd,unittest
from lib.timeutil import *
from config.config import *

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
        book1 = xlrd.open_workbook(data_file)
        sheet1 = book1.sheet_by_index(0)
        rows1 = sheet1.nrows
        # # 1.读取execl中第一个sheet中第一列的用例名称，封装到集合或者数组中

        yl = []
        for n in range(0,rows1):
            yl.append(sheet1.cell(n,0).value)
        print("第一行：",yl)

        data = []
        #  #循环每一个excel表名称
        for k in range(len(yl)):
            book = xlrd.open_workbook(Config.data_dirs() +"\\"+yl[k])
            print("k.text:"+yl[k])
            sheet = book.sheet_by_index(0)
            rows = sheet.nrows
            cols = sheet.ncols
            for i in range(1, rows):
                for k in range(len(getTimeperiod())):
                    data_rows = []
                    for j in range(cols):
                        d = sheet.cell(i, j).value
                        if j == 0:
                            if d == "off":
                                break
                        if "%d" in d:
                            d = d % (getTimeperiod()[k], "'" + getTimegranularity()[k] + "'")
                            # getTimeperiod()  [30, 60, 360, 720, 1440, 4320, 10080, 20160, 43200, 86400, 129600]
                            # getTimegranularity()  ['1m','2m','5m','30m','1h','3h','6h','12h','1d','2d','3d']
                        data_rows.append(d)
                    if data_rows:
                        data.append(data_rows)
        return data






if __name__ == '__main__':
    unittest.main()
