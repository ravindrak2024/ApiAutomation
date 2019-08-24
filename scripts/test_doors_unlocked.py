from .HALTestbase import HALTestbase
from utils.RandomGenerator import *
from utils.APIRequests import *
from pytest_testrail.plugin import pytestrail

class TestCaseDoorsUnlocked(HALTestbase):

    @pytestrail.case('C9')
    def test_doors_unlocked_with_valid_values(self):
        baseurl = self.Templates.getFromConfig('$baseurl')

        asset_id = 'api-'+generateRandom(RandomDataType.STRING, 10)  # Creating a random asset id
        HALTestbase.commonAction.createAsset(asset_id)  # calling create asset from common function

        HALTestbase.commonAction.reserveAsset(asset_id)
        HALTestbase.commonAction.reservation_confirmed(asset_id)

        api_path = self.Templates.getFromApiPaths('vi_action')
        api_path = api_path.replace('#asset_id', asset_id)

        header = self.Templates.getFromHeaders('vendor_initiated')
        payload = self.Templates.getFromPayload('doors_unlocked')

        response_status, response_payload, response_headers = doPut(baseurl + api_path, header, payload)
        assert response_status == 204


    @pytestrail.case('C10')
    def test_doors_unlocked_with_invalid_rfid_key_val(self):
        baseurl = self.Templates.getFromConfig('$baseurl')

        asset_id = 'api-'+generateRandom(RandomDataType.STRING, 10)  # Creating a random asset id
        HALTestbase.commonAction.createAsset(asset_id)  # calling create asset from common function

        HALTestbase.commonAction.reserveAsset(asset_id)
        HALTestbase.commonAction.reservation_confirmed(asset_id)

        api_path = self.Templates.getFromApiPaths('vi_action')
        api_path = api_path.replace('#asset_id', asset_id)

        header = self.Templates.getFromHeaders('vendor_initiated')
        payload = self.Templates.getFromPayload('doors_unlocked')
        payload['rfid_key_map']['1234'] = '453'

        response_status, response_payload, response_headers = doPut(baseurl + api_path, header, payload)

        assert response_status == 400
        assert 'Matching key not found in RFIDs or Device ID keys' in json.dumps(response_payload)

    @pytestrail.case('C11')
    def test_doors_unlocked_with_blank_rfid_key_val(self):
        baseurl = self.Templates.getFromConfig('$baseurl')

        asset_id = 'api-'+generateRandom(RandomDataType.STRING, 10)  # Creating a random asset id
        HALTestbase.commonAction.createAsset(asset_id)  # calling create asset from common function

        HALTestbase.commonAction.reserveAsset(asset_id)
        HALTestbase.commonAction.reservation_confirmed(asset_id)

        api_path = self.Templates.getFromApiPaths('vi_action')
        api_path = api_path.replace('#asset_id', asset_id)

        header = self.Templates.getFromHeaders('vendor_initiated')
        payload = self.Templates.getFromPayload('doors_unlocked')
        del payload['rfid_key_map']['1234']
        payload['rfid_key_map'][''] = ''

        response_status, response_payload, response_headers = doPut(baseurl + api_path, header, payload)

        assert response_status == 400
        assert 'Matching key not found in RFIDs or Device ID keys' in json.dumps(response_payload)


    @pytestrail.case('C12')
    def test_doors_unlocked_with_missing_synthesis(self):
        baseurl = self.Templates.getFromConfig('$baseurl')

        asset_id = 'api-'+generateRandom(RandomDataType.STRING, 10)  # Creating a random asset id
        HALTestbase.commonAction.createAsset(asset_id)  # calling create asset from common function

        HALTestbase.commonAction.reserveAsset(asset_id)
        HALTestbase.commonAction.reservation_confirmed(asset_id)

        api_path = self.Templates.getFromApiPaths('vi_action')
        api_path = api_path.replace('#asset_id', asset_id)

        header = self.Templates.getFromHeaders('vendor_initiated')
        payload = self.Templates.getFromPayload('doors_unlocked')

        del payload['synthesis']

        response_status, response_payload, response_headers = doPut(baseurl + api_path, header, payload)
        assert response_status == 400
        assert 'Missing Synthesis Data: Request requires complete synthesis data' in json.dumps(response_payload)

    @pytestrail.case('C13')
    def test_doors_unlocked_with_missing_raw_synthesis(self):
        baseurl = self.Templates.getFromConfig('$baseurl')

        asset_id = 'api-'+generateRandom(RandomDataType.STRING, 10)  # Creating a random asset id
        HALTestbase.commonAction.createAsset(asset_id)  # calling create asset from common function

        HALTestbase.commonAction.reserveAsset(asset_id)
        HALTestbase.commonAction.reservation_confirmed(asset_id)

        api_path = self.Templates.getFromApiPaths('vi_action')
        api_path = api_path.replace('#asset_id', asset_id)

        header = self.Templates.getFromHeaders('vendor_initiated')
        payload = self.Templates.getFromPayload('doors_unlocked')

        del payload['raw_synthesis']

        response_status, response_payload, response_headers = doPut(baseurl + api_path, header, payload)
        assert response_status == 400
        assert 'Missing Synthesis Data: Request requires complete synthesis data' in json.dumps(response_payload)
