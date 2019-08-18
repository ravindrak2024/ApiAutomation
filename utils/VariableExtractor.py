from .Constants import *
import re

class VariableExtractor:

   def getJsonPathRawData(self,text): # this method isonly used in the Api Framework
        return re.findall(REGEX_GET_JSON_PATH,text)




