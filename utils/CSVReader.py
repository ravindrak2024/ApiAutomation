import sys
from os import listdir
from os import path
from os.path import *
from utils.LogInitilizer import LogInitilizer

logger=LogInitilizer.getLogger()

class CSVReader:

    def __init__(self,path):
        self.path=path

    def readAllCsv(self):
        '''
        This function reads all the csv from the root path mentioned in the constructor
        :return: list of lines read
        '''
        logger.debug("Reading all csv from path %s",self.path)

        if isdir(self.path):
            lst = listdir(self.path)
        else:
            lst=[self.path]

        logger.debug("All file list {}".format(lst))
        tests = []
        for filelist in lst:
            if isdir(self.path):
                lines = open(self.path + filelist).read().split('\n')
            else:
                lines = open(filelist).read().split('\n')

            temp_lst = []
            for index, line in enumerate(lines):
                if isdir(self.path):
                    line = str(index) + ',' + filelist + ',' + line
                else:
                    head,tail =path.split(self.path)

                    line = str(index) + ',' + tail + ',' + line
                temp_lst.append(line.replace('""', '"'))
            tests.append(temp_lst)

        return tests

    def readCsv(self,filepath):
        logger.debug("Reading csv %s",filepath)
        lst=open(filepath).read().split('\n')
        tests=[]
        head,tail=path.split(filepath)
        for index,line in enumerate(lst):
            line=str(index)+','+tail+','+line
            tests.append(line)
        return tests

    def readCsv_without_index(self,filepath):
        logger.debug("Reading csv %s",filepath)
        lst=open(filepath).read().split('\n')
        tests=[]
        head,tail=path.split(filepath)
        for line in lst:
            tests.append(line)
        return tests

    def readCsvForParameterization(self, filepath):
        #logger.debug("Reading csv %s", filepath)
        lst = open(filepath).read().split('\n')
        tests = []
        head, tail = path.split(filepath)

        methods = ['POST','PUT','PATCH','GET','DELETE']

        steps=[]
        data = list()
        for line in lst:
            #logger.info("Read line  {}".format(line))
            action=line.split(',')[0]
            if action in methods:
               steps.append(data)
               data=list()
            data.append(line)
        steps.append(data)

        return steps



    def readAllCsvDemo(self):
        logger.debug("Reading all csv from path %s", self.path)
        lst = listdir(self.path)
        logger.debug("All file list {}".format(lst))
        tests = []
        for filelist in lst:
            lines = open(self.path + filelist).read().split('\n')
            tests.append(lines)
            # for index, line in enumerate(lines):
            #     line = str(index) + ',' + filelist + ',' + line
            #     temp_lst.append(line.replace('""', '"'))
        return tests