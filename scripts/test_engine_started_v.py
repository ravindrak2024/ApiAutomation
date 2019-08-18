from .HALTestbase import HALTestbase
from utils.RandomGenerator import *
from utils.APIRequests import *

class TestCaseEngineStarted(HALTestbase):

    def test_engine_started_with_valid_data(self):
        baseurl = self.Templates.getFromConfig('$baseurl')

        asset_id = 'api-'+generateRandom(RandomDataType.STRING, 10)  # Creating a random asset id
        HALTestbase.commonAction.createAsset(asset_id)  # calling create asset from common function

        HALTestbase.commonAction.reserveAsset(asset_id)
        HALTestbase.commonAction.reservation_confirmed(asset_id)

        api_path = self.Templates.getFromApiPaths('vi_action')
        api_path = api_path.replace('#asset_id', asset_id)

        header = self.Templates.getFromHeaders('vendor_initiated')
        payload = self.Templates.getFromPayload('engine_started')

        response_status, response_payload, response_headers = doPut(baseurl + api_path, header, payload)
        assert response_status == 204

    def test_engine_started_with_invalid_rfid_key_val(self):
        baseurl = self.Templates.getFromConfig('$baseurl')

        asset_id = 'api-'+generateRandom(RandomDataType.STRING, 10)  # Creating a random asset id
        HALTestbase.commonAction.createAsset(asset_id)  # calling create asset from common function

        HALTestbase.commonAction.reserveAsset(asset_id)
        HALTestbase.commonAction.reservation_confirmed(asset_id)

        api_path = self.Templates.getFromApiPaths('vi_action')
        api_path = api_path.replace('#asset_id', asset_id)

        header = self.Templates.getFromHeaders('vendor_initiated')
        payload = self.Templates.getFromPayload('engine_started')
        payload['rfid_key_map']['1234'] = '453'

        response_status, response_payload, response_headers = doPut(baseurl + api_path, header, payload)

        assert response_status == 400
        assert 'Matching key not found in RFIDs or Device ID keys' in json.dumps(response_payload)

    def test_engine_started_with_missing_synthesis(self):
        baseurl = self.Templates.getFromConfig('$baseurl')

        asset_id = 'api-'+generateRandom(RandomDataType.STRING, 10)  # Creating a random asset id
        HALTestbase.commonAction.createAsset(asset_id)  # calling create asset from common function

        HALTestbase.commonAction.reserveAsset(asset_id)
        HALTestbase.commonAction.reservation_confirmed(asset_id)

        api_path = self.Templates.getFromApiPaths('vi_action')
        api_path = api_path.replace('#asset_id', asset_id)

        header = self.Templates.getFromHeaders('vendor_initiated')
        payload = self.Templates.getFromPayload('engine_started')

        del payload['synthesis']

        response_status, response_payload, response_headers = doPut(baseurl + api_path, header, payload)
        assert response_status == 400
        assert 'Missing Synthesis Data: Request requires complete synthesis data' in json.dumps(response_payload)

    def test_engine_started_with_missing_raw_synthesis(self):
        baseurl = self.Templates.getFromConfig('$baseurl')

        asset_id = 'api-'+generateRandom(RandomDataType.STRING, 10)  # Creating a random asset id
        HALTestbase.commonAction.createAsset(asset_id)  # calling create asset from common function

        HALTestbase.commonAction.reserveAsset(asset_id)
        HALTestbase.commonAction.reservation_confirmed(asset_id)

        api_path = self.Templates.getFromApiPaths('vi_action')
        api_path = api_path.replace('#asset_id', asset_id)

        header = self.Templates.getFromHeaders('vendor_initiated')
        payload = self.Templates.getFromPayload('engine_started')

        del payload['raw_synthesis']

        response_status, response_payload, response_headers = doPut(baseurl + api_path, header, payload)
        assert response_status == 400
        assert 'Missing Synthesis Data: Request requires complete synthesis data' in json.dumps(response_payload)