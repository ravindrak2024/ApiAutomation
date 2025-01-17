from .HALTestbase import HALTestbase
from utils.RandomGenerator import *
from utils.APIRequests import *
from pytest_testrail.plugin import pytestrail
import pytest

class TestCaseRfidBookingStarted(HALTestbase):

    @pytestrail.case('C26')
    @pytest.mark.hwms_functional
    def test_rfid_booking_started_with_valid_payload(self,configureTenantVendor,client):
        baseurl = self.Templates.getFromConfig('$baseurl')

        asset_id = 'api-' + generateRandom(RandomDataType.STRING, 10)  # Creating a random asset id
        HALTestbase.commonAction.createAsset(asset_id)  # calling create asset from common function

        HALTestbase.commonAction.reserveAsset(asset_id)
        HALTestbase.commonAction.reservation_confirmed(asset_id)

        api_path = self.Templates.getFromApiPaths('vi_action')
        api_path = api_path.replace('#asset_id', asset_id)

        header = self.Templates.getFromHeaders('vendor_initiated')
        payload = self.Templates.getFromPayload('rfid_booking_started')

        response_status, response_payload, response_headers = client.doPut(baseurl + api_path, header, payload)
        assert response_status == 204

    @pytestrail.case('C27')
    @pytest.mark.hwms_functional
    def test_rfid_booking_started_with_incorrect_rfid(self,configureTenantVendor,client):
        baseurl = self.Templates.getFromConfig('$baseurl')

        asset_id = 'api-' + generateRandom(RandomDataType.STRING, 10)  # Creating a random asset id
        HALTestbase.commonAction.createAsset(asset_id)  # calling create asset from common function

        HALTestbase.commonAction.reserveAsset(asset_id)
        HALTestbase.commonAction.reservation_confirmed(asset_id)

        api_path = self.Templates.getFromApiPaths('vi_action')
        api_path = api_path.replace('#asset_id', asset_id)

        header = self.Templates.getFromHeaders('vendor_initiated')
        payload = self.Templates.getFromPayload('rfid_booking_started')
        payload['rfid_key_map']['1234']='564'

        response_status, response_payload, response_headers = client.doPut(baseurl + api_path, header, payload)
        assert response_status == 400
        assert 'Matching key not found in RFIDs or Device ID keys' in json.dumps(response_payload)


    @pytestrail.case('C28')
    @pytest.mark.hwms_functional
    def test_rfid_booking_started_with_blank_rfid(self,configureTenantVendor,client):
        baseurl = self.Templates.getFromConfig('$baseurl')

        asset_id = 'api-' + generateRandom(RandomDataType.STRING, 10)  # Creating a random asset id
        HALTestbase.commonAction.createAsset(asset_id)  # calling create asset from common function

        HALTestbase.commonAction.reserveAsset(asset_id)
        HALTestbase.commonAction.reservation_confirmed(asset_id)

        api_path = self.Templates.getFromApiPaths('vi_action')
        api_path = api_path.replace('#asset_id', asset_id)

        header = self.Templates.getFromHeaders('vendor_initiated')
        payload = self.Templates.getFromPayload('rfid_booking_started')
        del payload['rfid_key_map']['1234']
        payload['rfid_key_map']['']=''

        response_status, response_payload, response_headers = client.doPut(baseurl + api_path, header, payload)
        assert response_status == 400
        assert 'Matching key not found in RFIDs or Device ID keys' in json.dumps(response_payload)