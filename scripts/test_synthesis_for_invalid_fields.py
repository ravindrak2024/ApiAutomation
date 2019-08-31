from .HALTestbase import HALTestbase
from scripts.scriptutils.SynthesisConstants import *
from pytest_testrail.plugin import pytestrail


class TestCaseCheckPushSynthesisForInvalidFieldInputs(HALTestbase):

    @pytestrail.case('C35')
    def test_synthesis_with_front_driver_object_missing(self,client):
        baseurl = self.Templates.getFromConfig('$baseurl')

        api_path = self.Templates.getFromApiPaths('mensa_push_synthesis')

        header = self.Templates.getFromHeaders('mensa_push')
        payload = self.Templates.getFromPayload('mensa_push_synthesis')
        payload['synthesis']['eventSource']=SynthesisEventSourceDoorsLocked
        payload['asset_id']='assetwithkey-free-hwmsrswithnfckey-pushwithnokey-DOORS_LOCKED-ACCESSORY'
        del payload['synthesis']['doorStatus']['frontDriver']

        response_status, response_payload, response_headers = client.doPost(baseurl + api_path, header, payload)
        assert response_status == 400
        assert response_payload["mensa-api"]["serverError"]["message"] == MENV_SYNTHESIS_FRONT_DRIVER_DOOR_STATUS_MISSING
        assert response_payload["mensa-api"]["serverError"]["error"] == MENV_BAD_REQUEST_BODY

    @pytestrail.case('C36')
    def test_synthesis_with_ignition_object_missing(self,client):
        baseurl = self.Templates.getFromConfig('$baseurl')

        api_path = self.Templates.getFromApiPaths('mensa_push_synthesis')

        header = self.Templates.getFromHeaders('mensa_push')
        payload = self.Templates.getFromPayload('mensa_push_synthesis')
        payload['synthesis']['eventSource']=SynthesisEventSourceDoorsLocked
        payload['asset_id']='assetwithkey-free-hwmsrswithnfckey-pushwithnokey-DOORS_LOCKED-ACCESSORY'
        del payload['synthesis']['ignition']

        response_status, response_payload, response_headers = client.doPost(baseurl + api_path, header, payload)
        assert response_status == 400
        assert response_payload["mensa-api"]["serverError"]["message"] == MENV_SYNTHESIS_IGNITION_MISSING
        assert response_payload["mensa-api"]["serverError"]["error"] == MENV_BAD_REQUEST_BODY

    @pytestrail.case('C37')
    def test_synthesis_with_no_rental_keys_object(self,client):
        baseurl = self.Templates.getFromConfig('$baseurl')

        api_path = self.Templates.getFromApiPaths('mensa_push_synthesis')

        header = self.Templates.getFromHeaders('mensa_push')
        payload = self.Templates.getFromPayload('mensa_push_synthesis')
        payload['synthesis']['eventSource']=SynthesisEventSourceDoorsLocked
        payload['asset_id']='assetwithkey-free-hwmsrswithnfckey-pushwithnokey-DOORS_LOCKED-ACCESSORY'
        del payload['synthesis']['rentalKeys']

        response_status, response_payload, response_headers = client.doPost(baseurl + api_path, header, payload)
        assert response_status == 200

    @pytestrail.case('C38')
    def test_synthesis_with_doorStatus_object_missing(self,client):
        baseurl = self.Templates.getFromConfig('$baseurl')

        api_path = self.Templates.getFromApiPaths('mensa_push_synthesis')

        header = self.Templates.getFromHeaders('mensa_push')
        payload = self.Templates.getFromPayload('mensa_push_synthesis')
        payload['synthesis']['eventSource']=SynthesisEventSourceDoorsLocked
        payload['asset_id']='assetwithkey-free-hwmsrswithnfckey-pushwithnokey-DOORS_LOCKED-ACCESSORY'
        del payload['synthesis']['doorStatus']

        response_status, response_payload, response_headers = client.doPost(baseurl + api_path, header, payload)
        assert response_status == 400
        assert response_payload["mensa-api"]["serverError"]["message"] == MENV_SYNTHESIS_DOOR_STATUS_MISSING
        assert response_payload["mensa-api"]["serverError"]["error"] == MENV_BAD_REQUEST_BODY

