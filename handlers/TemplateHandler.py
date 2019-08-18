from utils.JsonReader import JsonReader
from os import listdir
from utils.Constants import *
from .VariableEvalHandler import *
from utils.LogInitilizer import *
import copy
logger=LogInitilizer.getLogger()

class TemplateHandler:
    '''
        Singleton class which reads the template data for payload,headers,configs and api_paths
    '''

    class LoadTemplates:
        def __init__(self,environment):
            logger.debug("Created instance of TemplateHandler")
            self.__headers = dict()           # Initialising the headers dictionary.
            self.__payload = dict()           # Initialising the payload dictionary.
            self.__config = dict()            # Initializing the config dictionary.
            self.__api_path=dict()            # Initializing the api_path dictionary.
            jsonReader = JsonReader()
            variable_eval = VariableEvalHandler()

            # Read api path data
            self.__api_path = jsonReader.getData(API_PATH + '/' + 'api_paths' + '.json')     #Reads the path api based and stores as dict.

            # Read config data
            self.__config = jsonReader.getData(CONFIGS + '/' + environment + '.json')        #Reads the config file based on --env passed as command line

            # Read headers and add them to headers dict
            header_file_list = listdir(HEADERS + '/')                 # Reads Headers from file headers.json
            for file in header_file_list:
                self.__headers[file.split('.')[0]] = variable_eval.evaluateVariable(         #Evaluates any  variable with $ .
                    jsonReader.getData(HEADERS + '/' + file), self.__config)

            # Read payload templates and add them to payload dict
            payload_file_list = listdir(TEMPLATES + '/')
            for file in payload_file_list:
                self.__payload[file.split('.')[0]] = variable_eval.evaluateVariable(    #Evaluates any variables with $
                    jsonReader.getData(TEMPLATES + '/' + file), self.__config)

        def getFromConfig(self,config):
            return self.__config[config]

        def getFromHeaders(self,header):
            return copy.deepcopy(self.__headers[header])

        def getFromPayload(self,payload):
            return copy.deepcopy(self.__payload[payload])

        def getFromApiPaths(self,api_path):
            return self.__api_path[api_path]

        def getConfig(self):
            return self.__config



    __instance = None

    @staticmethod
    def getTemplates(environment):
         if TemplateHandler.__instance is None:
             TemplateHandler.__instance=TemplateHandler.LoadTemplates(environment)
             return TemplateHandler.__instance
         return TemplateHandler.__instance



