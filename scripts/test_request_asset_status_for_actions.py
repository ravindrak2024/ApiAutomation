from .HALTestbase import HALTestbase
from scripts.scriptutils.SynthesisConstants import *
from pytest_testrail.plugin import pytestrail
import pytest

class TestRequestAssetStatusForDoorandEngineActions(HALTestbase):

    @pytestrail.case('C39')
    @pytest.mark.mensa_functional
    def test_request_asset_status_for_action_engine_started(self,client):
        baseurl = self.Templates.getFromConfig('$baseurl')

        api_path = self.Templates.getFromApiPaths('vendor_mensa')
        api_path=api_path.replace('#asset_id','assetwithkey-free-hwmsrswithnfckey-pushwithnfckey-ENGINE_ON-ACCESSORY')

        header = self.Templates.getFromHeaders('vendor_mensa_header')
        payload = self.Templates.getFromPayload('request_asset_status')

        response_status, response_payload, response_headers = client.doPut(baseurl + api_path, header, payload)

        assert response_status == 200
        assert response_payload["synthesis"]["key"] == 'bdb77cbb-9995-44cc-9b07-52354f8640a8'
        assert response_payload["synthesis"]["action"] == 'engine_started'

    @pytestrail.case('C40')
    @pytest.mark.mensa_functional
    def test_request_asset_status_for_action_engine_stopped(self,client):
        baseurl = self.Templates.getFromConfig('$baseurl')

        api_path = self.Templates.getFromApiPaths('vendor_mensa')
        api_path=api_path.replace('#asset_id','assetwithkey-free-hwmsrswithnfckey-pushwithnfckey-ENGINE_OFF-ACCESSORY')

        header = self.Templates.getFromHeaders('vendor_mensa_header')
        payload = self.Templates.getFromPayload('request_asset_status')

        response_status, response_payload, response_headers = client.doPut(baseurl + api_path, header, payload)

        assert response_status == 200
        assert response_payload["synthesis"]["key"] == 'bdb77cbb-9995-44cc-9b07-52354f8640a8'
        assert response_payload["synthesis"]["action"] == 'engine_stopped'

    @pytestrail.case('C41')
    @pytest.mark.mensa_functional
    def test_request_asset_status_for_action_doors_unlocked(self,client):
        baseurl = self.Templates.getFromConfig('$baseurl')

        api_path = self.Templates.getFromApiPaths('vendor_mensa')
        api_path=api_path.replace('#asset_id','assetwithkey-free-hwmsrswithnfckey-pushwithnfckey-DOORS_OPEN-ACCESSORY')

        header = self.Templates.getFromHeaders('vendor_mensa_header')
        payload = self.Templates.getFromPayload('request_asset_status')

        response_status, response_payload, response_headers = client.doPut(baseurl + api_path, header, payload)

        assert response_status == 200
        assert response_payload["synthesis"]["key"] == 'bdb77cbb-9995-44cc-9b07-52354f8640a8'
        assert response_payload["synthesis"]["action"] == 'doors_unlocked'

    @pytestrail.case('C42')
    @pytest.mark.mensa_functional
    def test_request_asset_status_for_action_doors_locked(self,client):
        baseurl = self.Templates.getFromConfig('$baseurl')

        api_path = self.Templates.getFromApiPaths('vendor_mensa')
        api_path=api_path.replace('#asset_id','assetwithkey-free-hwmsrswithnfckey-pushwithnfckey-DOORS_LOCKED-ACCESSORY')

        header = self.Templates.getFromHeaders('vendor_mensa_header')
        payload = self.Templates.getFromPayload('request_asset_status')

        response_status, response_payload, response_headers = client.doPut(baseurl + api_path, header, payload)

        assert response_status == 200
        assert response_payload["synthesis"]["key"] == 'bdb77cbb-9995-44cc-9b07-52354f8640a8'
        assert response_payload["synthesis"]["action"] == 'doors_locked'

    @pytestrail.case('C43')
    @pytest.mark.mensa_functional
    def test_request_asset_status_for_action_doors_unlocked_2(self,client):
        baseurl = self.Templates.getFromConfig('$baseurl')

        api_path = self.Templates.getFromApiPaths('vendor_mensa')
        api_path=api_path.replace('#asset_id','assetwithkey-free-hwmsrswithnfckey-pushwithnfckey-DOORS_UNLOCKED-ACCESSORY')

        header = self.Templates.getFromHeaders('vendor_mensa_header')
        payload = self.Templates.getFromPayload('request_asset_status')

        response_status, response_payload, response_headers = client.doPut(baseurl + api_path, header, payload)

        assert response_status == 200
        assert response_payload["synthesis"]["key"] == 'bdb77cbb-9995-44cc-9b07-52354f8640a8'
        assert response_payload["synthesis"]["action"] == 'doors_unlocked'

    @pytestrail.case('C44')
    @pytest.mark.mensa_functional
    def test_request_asset_status_for_action_DOORS_UNLOCKED_ALLOW_START(self, client):
        baseurl = self.Templates.getFromConfig('$baseurl')

        api_path = self.Templates.getFromApiPaths('vendor_mensa')
        api_path = api_path.replace('#asset_id',
                                    'assetwithkey-free-hwmsrswithnfckey-pushwithnfckey-DOORS_UNLOCKED_ALLOW_START-ACCESSORY')

        header = self.Templates.getFromHeaders('vendor_mensa_header')
        payload = self.Templates.getFromPayload('request_asset_status')

        response_status, response_payload, response_headers = client.doPut(baseurl + api_path, header, payload)

        assert response_status == 200
        assert response_payload["synthesis"]["key"] == 'bdb77cbb-9995-44cc-9b07-52354f8640a8'
        assert response_payload["synthesis"]["action"] == 'doors_unlocked'


    @pytestrail.case('C45')
    @pytest.mark.mensa_functional
    def test_request_asset_status_for_action_asset_status_update_received(self, client):
        baseurl = self.Templates.getFromConfig('$baseurl')

        api_path = self.Templates.getFromApiPaths('vendor_mensa')
        api_path = api_path.replace('#asset_id',
                                    'assetwithkey-free-hwmsrswithnfckey-pushwithnfckey-DTC-ACCESSORY')

        header = self.Templates.getFromHeaders('vendor_mensa_header')
        payload = self.Templates.getFromPayload('request_asset_status')

        response_status, response_payload, response_headers = client.doPut(baseurl + api_path, header, payload)

        assert response_status == 200
        assert response_payload["synthesis"]["key"] == 'bdb77cbb-9995-44cc-9b07-52354f8640a8'
        assert response_payload["synthesis"]["action"] == 'asset_status_update_received'


    @pytestrail.case('C46')
    @pytest.mark.mensa_functional
    def test_request_asset_status_for_action_engine_force_started(self, client):
        baseurl = self.Templates.getFromConfig('$baseurl')

        api_path = self.Templates.getFromApiPaths('vendor_mensa')
        api_path = api_path.replace('#asset_id',
                                    'assetwithkey-free-hwmsrswithnfckey-pushwithnokey-ENGINE_ON-ACCESSORY')

        header = self.Templates.getFromHeaders('vendor_mensa_header')
        payload = self.Templates.getFromPayload('request_asset_status')

        response_status, response_payload, response_headers = client.doPut(baseurl + api_path, header, payload)

        assert response_status == 200
        assert response_payload["synthesis"]["action"] == 'engine_force_started'

    @pytestrail.case('C47')
    @pytest.mark.mensa_functional
    def test_request_asset_status_for_action_engine_force_stopped(self, client):
        baseurl = self.Templates.getFromConfig('$baseurl')

        api_path = self.Templates.getFromApiPaths('vendor_mensa')
        api_path = api_path.replace('#asset_id',
                                    'assetwithkey-free-hwmsrswithnfckey-pushwithnokey-ENGINE_OFF-ACCESSORY')

        header = self.Templates.getFromHeaders('vendor_mensa_header')
        payload = self.Templates.getFromPayload('request_asset_status')

        response_status, response_payload, response_headers = client.doPut(baseurl + api_path, header, payload)

        assert response_status == 200
        assert response_payload["synthesis"]["action"] == 'engine_force_stopped'

    @pytestrail.case('C48')
    @pytest.mark.mensa_functional
    def test_request_asset_status_for_action_doors_force_unlocked(self, client):
        baseurl = self.Templates.getFromConfig('$baseurl')

        api_path = self.Templates.getFromApiPaths('vendor_mensa')
        api_path = api_path.replace('#asset_id',
                                    'assetwithkey-free-hwmsrswithnfckey-pushwithnokey-DOORS_OPEN-ACCESSORY')

        header = self.Templates.getFromHeaders('vendor_mensa_header')
        payload = self.Templates.getFromPayload('request_asset_status')

        response_status, response_payload, response_headers = client.doPut(baseurl + api_path, header, payload)

        assert response_status == 200
        assert response_payload["synthesis"]["action"] == 'doors_force_unlocked'

    @pytestrail.case('C49')
    @pytest.mark.mensa_functional
    def test_request_asset_status_for_action_doors_force_locked(self, client):
        baseurl = self.Templates.getFromConfig('$baseurl')

        api_path = self.Templates.getFromApiPaths('vendor_mensa')
        api_path = api_path.replace('#asset_id',
                                    'assetwithkey-free-hwmsrswithnfckey-pushwithnokey-DOORS_LOCKED-ACCESSORY')

        header = self.Templates.getFromHeaders('vendor_mensa_header')
        payload = self.Templates.getFromPayload('request_asset_status')

        response_status, response_payload, response_headers = client.doPut(baseurl + api_path, header, payload)

        assert response_status == 200
        assert response_payload["synthesis"]["action"] == 'doors_force_locked'

    @pytestrail.case('C50')
    @pytest.mark.mensa_functional
    def test_request_asset_status_for_action_doors_force_unlocked_DOORS_UNLOCKED(self, client):
        baseurl = self.Templates.getFromConfig('$baseurl')

        api_path = self.Templates.getFromApiPaths('vendor_mensa')
        api_path = api_path.replace('#asset_id',
                                    'assetwithkey-free-hwmsrswithnfckey-pushwithnokey-DOORS_UNLOCKED-ACCESSORY')

        header = self.Templates.getFromHeaders('vendor_mensa_header')
        payload = self.Templates.getFromPayload('request_asset_status')

        response_status, response_payload, response_headers = client.doPut(baseurl + api_path, header, payload)

        assert response_status == 200
        assert response_payload["synthesis"]["action"] == 'doors_force_unlocked'

    @pytestrail.case('C51')
    @pytest.mark.mensa_functional
    def test_request_asset_status_for_action_doors_force_unlocked_DOORS_UNLOCKED_ALLOW_START(self, client):
        baseurl = self.Templates.getFromConfig('$baseurl')

        api_path = self.Templates.getFromApiPaths('vendor_mensa')
        api_path = api_path.replace('#asset_id',
                                    'assetwithkey-free-hwmsrswithnfckey-pushwithnokey-DOORS_UNLOCKED_ALLOW_START-ACCESSORY')

        header = self.Templates.getFromHeaders('vendor_mensa_header')
        payload = self.Templates.getFromPayload('request_asset_status')

        response_status, response_payload, response_headers = client.doPut(baseurl + api_path, header, payload)

        assert response_status == 200
        assert response_payload["synthesis"]["action"] == 'doors_force_unlocked'
