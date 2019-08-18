from utils.LogInitilizer import LogInitilizer
from utils.ExcelReader import ExcelReader
from handlers.VariableEvalHandler import VariableEvalHandler

logger=LogInitilizer.getLogger()

methods=['PUT','POST','DELETE','GET']
assertions=['ASSERTEQ','ASSERTCONTAINS','ASSERTNEQ','ASSERTLISTLENGTH','ASSERTSTRLENGTH']

'''
$variablename - lookup in config file - replace with variable defined in config.json/environment.json
$$variablename - lookup for file directly eg - If header - look for  header.json file and replace it directly.
'''

def getDataFrom(index,full_data):
    assert_list=list()
    for counter,line in enumerate(full_data):
        if counter>=index+1 and line[0] not in methods:
            assert_list.append(line)
        elif counter>index and line[0] in methods:
            break
    return assert_list

class ParameterizationHandler:

    def __init__(self,path,template):
        self.excelreader=ExcelReader(path,'Sheet1')
        self.template=template
        self.variable_eval=VariableEvalHandler()

    def getParameters(self):
        '''
        Get local var,file variable directly.
        :return: Returns parameter in format [[['METHOD','PAYLOAD','HEADER',STATUS],[[ASSERT,VAL,VAL],[ASSERT,VAL,VAL],[ASSERT,VAL,VAL]]]
        '''

        data = self.excelreader.readExcel()
        param_data = []

        for index, line in enumerate(data):
            step = []

            if line[0] in methods:

                if '$' in line[1]:                              # evaluate the variables in the payload
                    line[1]=self.variable_eval.evaluateVariable(line[1],self.template.getConfig())

                if '$$' in line[2]:                             # check if the header is to be picked from header file.
                    headername=line[2][2:]
                    line[2]=self.template.getFromHeaders(headername)

                if '$' in line[2]:                              # check if header congains variables and then evaluate
                    line[2]=self.variable_eval.evaluateVariable(line[2],self.template.getConfig())

                step.append(line)
                val_list = getDataFrom(index, data)
                step.append(val_list)
                param_data.append(step)

        return param_data
