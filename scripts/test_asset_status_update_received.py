from .HALTestbase import HALTestbase
from utils.RandomGenerator import *
from utils.APIRequests import *

class TestCase(HALTestbase):

    def test_asset_status_update_received_with_valid_payload(self):
        baseurl = self.Templates.getFromConfig('$baseurl')

        asset_id = 'api-' + generateRandom(RandomDataType.STRING, 10)  # Creating a random asset id
        HALTestbase.commonAction.createAsset(asset_id)  # calling create asset from common function

        HALTestbase.commonAction.reserveAsset(asset_id)
        HALTestbase.commonAction.reservation_confirmed(asset_id)

        api_path = self.Templates.getFromApiPaths('vi_action')
        api_path = api_path.replace('#asset_id', asset_id)

        header = self.Templates.getFromHeaders('vendor_initiated')
        payload = self.Templates.getFromPayload('asset_status_update_received')

        response_status, response_payload, response_headers = doPut(baseurl + api_path, header, payload)
        assert response_status == 204

    def test_asset_status_update_received_with_blank_ble_key(self):
        baseurl = self.Templates.getFromConfig('$baseurl')

        asset_id = 'api-' + generateRandom(RandomDataType.STRING, 10)  # Creating a random asset id
        HALTestbase.commonAction.createAsset(asset_id)  # calling create asset from common function

        HALTestbase.commonAction.reserveAsset(asset_id)
        HALTestbase.commonAction.reservation_confirmed(asset_id)

        api_path = self.Templates.getFromApiPaths('vi_action')
        api_path = api_path.replace('#asset_id', asset_id)

        header = self.Templates.getFromHeaders('vendor_initiated')
        payload = self.Templates.getFromPayload('asset_status_update_received')
        payload['ble_key']=''

        response_status, response_payload, response_headers = doPut(baseurl + api_path, header, payload)
        assert response_status == 400

        assert 'No key sent: a key is required for this request' in json.dumps(response_payload)

    def test_asset_status_update_received_with_no_synthesis(self):
        baseurl = self.Templates.getFromConfig('$baseurl')

        asset_id = 'api-' + generateRandom(RandomDataType.STRING, 10)  # Creating a random asset id
        HALTestbase.commonAction.createAsset(asset_id)  # calling create asset from common function

        HALTestbase.commonAction.reserveAsset(asset_id)
        HALTestbase.commonAction.reservation_confirmed(asset_id)

        api_path = self.Templates.getFromApiPaths('vi_action')
        api_path = api_path.replace('#asset_id', asset_id)

        header = self.Templates.getFromHeaders('vendor_initiated')
        payload = self.Templates.getFromPayload('asset_status_update_received')
        del payload['synthesis']

        response_status, response_payload, response_headers = doPut(baseurl + api_path, header, payload)
        assert response_status == 400

        assert 'Missing Synthesis Data: Request requires complete synthesis data' in json.dumps(response_payload)
