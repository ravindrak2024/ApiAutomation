import pytest
from testinits.TestBase import TestBase
from .HALTestbase import HALTestbase
from utils.LogInitilizer import LogInitilizer
from utils.APIRequests import *
from utils.RandomDataType import RandomDataType
from utils.RandomGenerator import *
from handlers.AssertionHandler import validateAsertions
import ast

class TestCaseReserveWithParameters(HALTestbase):

    def test_reserve_with_parameters_reserve_invalid_data(self,step,validations):
        method,payload,header,status=HALTestbase.commonAction.extractDataFromStep(step)    # extracting values from the test step

        asset_id = 'api-'+generateRandom(RandomDataType.STRING, 10)                               # generating random asset id
        HALTestbase.commonAction.createAsset(asset_id)                                     # Creating asset on the server

        url=TestBase.Templates.getFromConfig('$baseurl') + TestBase.Templates.getFromApiPaths('si_action').replace('#asset_id',asset_id)  # Creating url & adding asset to it
        statuscode,payload,header=keyword[method](url, header, payload)   # this is calling the required api

        validateAsertions(validations,payload)  # validating result
