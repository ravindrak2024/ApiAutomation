from utils.LogInitilizer import LogInitilizer
from utils.CSVReader import CSVReader
from utils.GoogleSheetReader import GoogleSheetRead
logger=LogInitilizer.getLogger()

class SetupHandler:
    def __init__(self,path,spreadsheet):
        self.path=path
        self.spreadsheet=spreadsheet


    def get_all_tests_from_setup(self):
        if self.spreadsheet is not None and self.path is not None:
            logger.debug("Can't read from both google sheet and path")
            raise AttributeError
        if self.path is not None:
            logger.debug("Reading Setup from path {}".format(self.path))
            vs = CSVReader(None)
            return vs.readCsv(self.path)
        elif self.spreadsheet is not None:
            logger.debug("Reading Setup from google spreadsheet {}".format(self.spreadsheet))
            gs = GoogleSheetRead(self.spreadsheet, 'setup')
            return gs.readTestCases()
        else:
            logger.fatal("No path/spreedsheet mentioned")
            raise AttributeError


