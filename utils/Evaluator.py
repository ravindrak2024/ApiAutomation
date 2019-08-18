from utils.VariableExtractor import VariableExtractor
from utils import Settings
from utils.LogInitilizer import LogInitilizer
logger=LogInitilizer.getLogger()


class Evaluator:
    def evaluateStatement(self,localvar,text):
        var_extract=VariableExtractor()
        all_global_vars=var_extract.getGlobalVars(text)
        text_replaced=text
        logger.debug("Evaluating text {}".format(text))
        for var in all_global_vars:
            text_replaced=text_replaced.replace(var,Settings.global_vars.get(var,var))
        logger.debug("Evaluated text {}".format(text_replaced))
        return text_replaced


