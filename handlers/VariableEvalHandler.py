import re
import json
import ast
from utils.LogInitilizer import LogInitilizer
logger=LogInitilizer.getLogger()
class VariableEvalHandler:
    '''
    Responsible to evaluate the local varaibles in any given text
    '''

    def __init__(self):
        self.__variable_regex='\$[A-Z|a-z|_|0-9]+'

    def evaluateVariable(self,text,config):
        '''
        Evaluates variable based on text,config dictionary
        :param text: text to be evaluated
        :param config: config file . This is to be dictionary.
        :return: Local var evaluated text
        '''
        data=json.dumps(text)  # json.dumps(text) returns text in string format
        all_vars=re.findall(self.__variable_regex,data)
        for var in all_vars:
            val=config.get(var,None)
            data=data.replace(var,val)
            logger.debug("Evaluated variable {} to {}".format(var,val))
        logger.debug("Evalauated json - {}".format(data))
        return json.loads(data)  # ast.literal_eval(data) converts data from text to dict
