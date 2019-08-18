from jsonpath_rw import jsonpath, parse
from utils.LogInitilizer import LogInitilizer
logger=LogInitilizer.getLogger()

class JSONHandler:

    def createJsonPath(self,text):
        logger.debug("Creating jsong path of text {}".format(text))
        base='$...'
        start=end=False
        for char in text:
            if char=='[':
                start=True
            elif char==']':
                end=True

            if char!='[' and  char!=']' and char!='"':
                if self.__is_number(char):
                    base=base[0:len(base)-1]
                    base+='['+char+']'
                else:
                    base+=char
            if end:
                base+='.'
                start=False
                end=False
        base=base.replace('...','..')
        logger.debug("JSON Path created {}".format(base[0:len(base)-1]))
        return base[0:len(base)-1]

    def __is_number(self,n):
        is_number = True
        try:
            #      v type-casting the number here as `complex`, instead of `float`
            num = float(n)
            is_number = num == num
        except ValueError:
            is_number = False
        return is_number

    def extractJsonValue(self,jsonpath,json):
        jsonpath_exp = parse(jsonpath)
        all_matches=[match.value for match in jsonpath_exp.find(json)]
        return all_matches[0]
