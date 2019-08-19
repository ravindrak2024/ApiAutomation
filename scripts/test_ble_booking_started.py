from .HALTestbase import HALTestbase
from utils.RandomGenerator import *
from utils.APIRequests import *

class TestCaseBleBookingStarted(HALTestbase):

    def test_ble_booking_started_with_valid_data(self):
        baseurl = self.Templates.getFromConfig('$baseurl')

        asset_id = 'api-' + generateRandom(RandomDataType.STRING, 10)  # Creating a random asset id
        HALTestbase.commonAction.createAsset(asset_id)  # calling create asset from common function

        HALTestbase.commonAction.reserveAsset(asset_id)
        HALTestbase.commonAction.reservation_confirmed(asset_id)

        api_path = self.Templates.getFromApiPaths('vi_action')
        api_path = api_path.replace('#asset_id', asset_id)

        header = self.Templates.getFromHeaders('vendor_initiated')
        payload = self.Templates.getFromPayload('ble_booking_started')

        response_status, response_payload, response_headers = doPut(baseurl + api_path, header, payload)
        assert response_status == 204

    def test_ble_booking_started_with_blank_ble(self):
        baseurl = self.Templates.getFromConfig('$baseurl')

        asset_id = 'api-' + generateRandom(RandomDataType.STRING, 10)  # Creating a random asset id
        HALTestbase.commonAction.createAsset(asset_id)  # calling create asset from common function

        HALTestbase.commonAction.reserveAsset(asset_id)
        HALTestbase.commonAction.reservation_confirmed(asset_id)

        api_path = self.Templates.getFromApiPaths('vi_action')
        api_path = api_path.replace('#asset_id', asset_id)

        header = self.Templates.getFromHeaders('vendor_initiated')
        payload = self.Templates.getFromPayload('ble_booking_started')
        payload['ble_key']=''

        response_status, response_payload, response_headers = doPut(baseurl + api_path, header, payload)
        assert response_status == 400
        assert 'No key sent: a key is required for this request' in json.dumps(response_payload)
