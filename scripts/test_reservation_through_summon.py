from testinits.TestBase import *
from utils.RandomDataType import *
from utils.RandomGenerator import *
from .HALTestbase import *
import softest
#from utils.LogInitilizer import LogInitilizer

class TestCaseReserveThroughSummon(HALTestbase):

    def test_reserve_with_valid_inputs(self):
        asset_id = 'api-'+generateRandom(RandomDataType.STRING, 10)  # Creating a random asset id
        HALTestbase.commonAction.createAsset(asset_id)        # calling create asset from common function

        response_status, response_payload, response_headers=HALTestbase.commonAction.reserveAsset(asset_id)
        assert response_payload['ble_key']=='ble_key11'

    def test_reserve_with_invalid_start_time_in_epoch(self):
        baseurl = self.Templates.getFromConfig('$baseurl')      # Picking up the baseurl from the config file
        asset_id = 'api-'+generateRandom(RandomDataType.STRING, 10) # Creating a random asset id

        HALTestbase.commonAction.createAsset(asset_id)       # Creating asset on server

        api_path=TestBase.Templates.getFromApiPaths('si_action')    # Picking up api path
        api_path=api_path.replace('#asset_id',asset_id)      # Modifying payload with random generated asset id
        headers=TestBase.Templates.getFromHeaders('summon_initiated') # Picking up header from template
        payload=TestBase.Templates.getFromPayload('reserve')         # Picking up reserve payload from templates
        payload['key_validity_start_in_epoch']=-1             # Modifying the parameter key_validity start in epoch

        response_status, response_payload, response_headers=doPut(baseurl+api_path,headers,payload)
        assert response_status==400
        assert response_payload['UserMessage']=='Some error occurred in transition function execution (e.g. network call)'

    def test_reserve_with_invalid_stop_time_in_epoch(self):
        baseurl = self.Templates.getFromConfig('$baseurl')  # Picking up the baseurl from the config file
        asset_id = 'api-'+generateRandom(RandomDataType.STRING, 10) # Creating a random asset id

        HALTestbase.commonAction.createAsset(asset_id)       # Creating asset on server

        api_path = TestBase.Templates.getFromApiPaths('si_action')     #Picking up api path
        api_path=api_path.replace('#asset_id',asset_id)       # Modifying payload with random generated asset id
        headers = TestBase.Templates.getFromHeaders('summon_initiated') # Picking up the header from the templates
        payload = TestBase.Templates.getFromPayload('reserve')          # Picking up reserve payload from templates
        payload['key_validity_stop_in_epoch']=-1                # modifying key_validity_stop_in_epoch

        response_status, response_payload, response_headers=doPut(baseurl+api_path,headers,payload)
        assert response_status==400
        assert response_payload['UserMessage']=='Some error occurred in transition function execution (e.g. network call)'
