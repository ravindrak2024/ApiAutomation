from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from utils.LogInitilizer import LogInitilizer
import re
logger=LogInitilizer.getLogger()

class GoogleSheetRead:
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
    RANGE='!A1:H'

    def __init__(self,SAMPLE_SPREADSHEET_ID,SHEET_NAME):
        self.SAMPLE_SPREADSHEET_ID=SAMPLE_SPREADSHEET_ID
        self.SAMPLE_RANGE_NAME=SHEET_NAME+self.RANGE
        self.SHEET_NAME=SHEET_NAME

    def getIndex(self,lst,str):
        try:
            index=[idx for idx, s in enumerate(lst) if str in s][0]
        except IndexError as ie:
            pass
        return index

    def readTestCases(self):
            """Shows basic usage of the Sheets API.
            Prints values from a sample spreadsheet.
            """
            logger.info("Reading data from path {}".format(self
                                                           .SAMPLE_SPREADSHEET_ID))
            creds = None
            # The file token.pickle stores the user's access and refresh tokens, and is
            # created automatically when the authorization flow completes for the first
            # time.
            if os.path.exists('token.pickle'):
                with open('token.pickle', 'rb') as token:
                    creds = pickle.load(token)
            # If there are no (valid) credentials available, let the user log in.
            if not creds or not creds.valid:
                if creds and creds.expired and creds.refresh_token:
                    creds.refresh(Request())
                else:
                    flow = InstalledAppFlow.from_client_secrets_file(
                        '.\credentials.json', self.SCOPES)
                    creds = flow.run_local_server()
                # Save the credentials for the next run
                with open('token.pickle', 'wb') as token:
                    pickle.dump(creds, token)

            service = build('sheets', 'v4', credentials=creds)

            # Call the Sheets API
            sheet = service.spreadsheets()
            result = sheet.values().get(spreadsheetId=self.SAMPLE_SPREADSHEET_ID,
                                        range=self.SAMPLE_RANGE_NAME).execute()
            values = result.get('values', [])
            #print(values)
            lst=[",".join(dat) for dat in values]
            for index, data in enumerate(lst):
                if len(data) == 0:
                    lst[index] = ',,,,,,'
                lst[index] = self.SHEET_NAME + ',' + lst[index]
                lst[index] = str(index) + ',' + lst[index]
            data_tc = []
            #print(lst)
            templst = []
            for dat in lst:
                if re.search('[0-9]+\,[a-zA-Z0-9]+\,{7}',dat):
                    data_tc.append(templst)
                    templst=[]
                else:
                    templst.append(dat)
            data_tc.append(templst)
            # while True:
            #     try:
            #         start_index = 0
            #         end_index = self.getIndex(lst,',,,,,,,')
            #         data_tc.append(lst[start_index:end_index])
            #         lst = lst[end_index + 1:]
            #     except ValueError as notfound:
            #         data_tc.append(lst)
            #         break;
            logger.debug("Data read - {}".format(data_tc))
            return data_tc

