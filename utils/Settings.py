from utils.GlobalVariables import GlobalVariables
from utils.LogInitilizer import LogInitilizer
from utils.Evaluator import Evaluator
from utils.CSVReader import CSVReader
from utils.GoogleSheetReader import GoogleSheetRead

#global_vars=GlobalVariables().getGlobalVaraibles()
#setup_data=CSVReader(None).readCsv(setup_path)





def init(gsheet_reference,setup_path='.\setup.csv'):
    global global_vars
    global eval
    global setup_data
    global_vars = GlobalVariables().getGlobalVaraibles()

    if setup_path=='gsheet':
        setup_data=GoogleSheetRead(gsheet_reference,'setup').readTestCases()
    else:
        setup_data = CSVReader(setup_path).readAllCsv()

    eval=Evaluator()
    print(setup_path)


