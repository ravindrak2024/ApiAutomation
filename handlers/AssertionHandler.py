from utils.Assert import *
from utils.VariableExtractor import VariableExtractor
from utils.JSONHandler import JSONHandler
import json

def getValue(actual_text, responsepayload):

    var_eval = VariableExtractor()
    jsonhandler = JSONHandler()

    value=responsepayload

    if not isinstance(responsepayload,str):
        value=json.dumps(responsepayload)

    if 'RESPONSE[' in actual_text:
        json_raw_data = var_eval.getJsonPathRawData(actual_text)
        jsonpath = jsonhandler.createJsonPath(json_raw_data[0])
        value=jsonhandler.extractJsonValue(jsonpath, responsepayload)

    return value

assertions={'ASSERTEQ':ASSERTEQ,'ASSERTNEQ':ASSERTNEQ,'ASSERTCONTAINS':ASSERTCONTAINS,'ASSERTOBJ':ASSERTOBJ,'ASSERTJSONSCHEMA':ASSERTJSONSCHEMA,
            'ASSERTFBVALUECHANGE':ASSERTFBVALUECHANGE,'ASSERTGE':ASSERTGE,'ASSERTLE':ASSERTLE,'ASSERTSORT':ASSERTSORT,'ASSERTNILEDATACHANGE':ASSERTNILEDATACHANGE}

def validateAsertions(assertion_list,response):
    for ass_list in assertion_list:
        actual_text=ass_list[1]
        actual=getValue(actual_text,response)
        assertion_type=ass_list[0]
        expected=ass_list[2]
        assertions[assertion_type](actual,expected)

