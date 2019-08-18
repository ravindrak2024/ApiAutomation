from utils.CSVReader import CSVReader
from utils.LogInitilizer import LogInitilizer


class GlobalVariables:
   def getGlobalVaraibles(self):
        csv = CSVReader(None)
        lst = csv.readCsv_without_index("./properties.csv")
        dic = dict()
        for item in lst:
            item_lst = item.split(",")
            try:
                key = '$$' + item_lst[0]
                value = item_lst[1]
                dic[key] = value
            except IndexError as indErr:
                dic[key] = ''
        return dic




