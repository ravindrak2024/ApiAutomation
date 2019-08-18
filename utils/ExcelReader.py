import xlrd
from utils.LogInitilizer import LogInitilizer
logger=LogInitilizer.getLogger()

class ExcelReader:
    def __init__(self,filepath,sheetname):
        self.filepath=filepath
        self.sheetname=sheetname

    def readTestCases(self):
        loc = (self.filepath)
        logger.info("Reading TestCase in excel at location {}".format(self.filepath))
        workbook = xlrd.open_workbook(loc)
        sheet = workbook.sheet_by_name(self.sheetname)
        logger.info("Reading Sheet {}".format(self.sheetname))
        row_count = sheet.nrows
        col_count = sheet.ncols
        data=[[str(sheet.cell_value(i,j)) for j in range(0,col_count)] for i in range(0,row_count)]
        lst1=[",".join(dat) for dat in data]
        logger.debug("Read Data {}".format(lst1))
        data_tc = []
        while True:
            try:
                start_index = 0
                end_index = lst1.index(',,,,,,')
                data_tc.append(lst1[start_index:end_index])
                lst1 = lst1[end_index+1:]
            except ValueError as notfound:
                data_tc.append(lst1)
                break;
        logger.debug("Full Read Data {}".format(data_tc))
        return data_tc


    # def readExcel(self):
    #     loc = (self.filepath)
    #     workbook = xlrd.open_workbook(loc)
    #     sheet = workbook.sheet_by_name(self.sheetname)
    #     row_count = sheet.nrows
    #     col_count = sheet.ncols
    #     data = [[str(sheet.cell_value(i, j)) for j in range(0, col_count)] for i in range(0, row_count)]
    #     return [",".join(dat) for dat in data]

    def readExcel(self):
        loc = (self.filepath)
        workbook = xlrd.open_workbook(loc)
        sheet = workbook.sheet_by_name(self.sheetname)
        row_count = sheet.nrows
        col_count = sheet.ncols
        data = [[str(sheet.cell_value(i, j)) for j in range(0, col_count)] for i in range(0, row_count)]
        return data
