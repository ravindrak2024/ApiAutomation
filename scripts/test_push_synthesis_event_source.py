from .HALTestbase import HALTestbase
from scripts.scriptutils.SynthesisConstants import *
from utils.RandomGenerator import *
from utils.APIRequests import *
from pytest_testrail.plugin import pytestrail

class TestCaseCheckPushSynthesisEventSourceWithValidRentalKey(HALTestbase):

    @pytestrail.case('C29')
    def test_synthesis_with_event_source_engine_on(self,client):
        baseurl = self.Templates.getFromConfig('$baseurl')

        api_path = self.Templates.getFromApiPaths('mensa_push_synthesis')

        header = self.Templates.getFromHeaders('mensa_push')
        payload = self.Templates.getFromPayload('mensa_push_synthesis')
        payload['synthesis']['eventSource']=SynthesisEventSourceEngineOn

        response_status, response_payload, response_headers = client.doPost(baseurl + api_path, header, payload)
        assert response_status == 200

    @pytestrail.case('C30')
    def test_synthesis_with_event_source_engine_off(self,client):
        baseurl = self.Templates.getFromConfig('$baseurl')

        api_path = self.Templates.getFromApiPaths('mensa_push_synthesis')

        header = self.Templates.getFromHeaders('mensa_push')
        payload = self.Templates.getFromPayload('mensa_push_synthesis')
        payload['synthesis']['eventSource']=SynthesisEventSourceEngineOn

        response_status, response_payload, response_headers = client.doPost(baseurl + api_path, header, payload)
        assert response_status == 200

    @pytestrail.case('C31')
    def test_synthesis_with_event_source_doors_open(self,client):
        baseurl = self.Templates.getFromConfig('$baseurl')

        api_path = self.Templates.getFromApiPaths('mensa_push_synthesis')

        header = self.Templates.getFromHeaders('mensa_push')
        payload = self.Templates.getFromPayload('mensa_push_synthesis')
        payload['synthesis']['eventSource']=SynthesisEventSourceDoorsOpen

        response_status, response_payload, response_headers = client.doPost(baseurl + api_path, header, payload)
        assert response_status == 200

    @pytestrail.case('C32')
    def test_synthesis_with_event_source_doors_locked(self,client):
        baseurl = self.Templates.getFromConfig('$baseurl')

        api_path = self.Templates.getFromApiPaths('mensa_push_synthesis')

        header = self.Templates.getFromHeaders('mensa_push')
        payload = self.Templates.getFromPayload('mensa_push_synthesis')
        payload['synthesis']['eventSource']=SynthesisEventSourceDoorsLocked

        response_status, response_payload, response_headers = client.doPost(baseurl + api_path, header, payload)
        assert response_status == 200

    @pytestrail.case('C33')
    def test_synthesis_with_event_source_doors_unlocked_allow_start(self,client):
        baseurl = self.Templates.getFromConfig('$baseurl')

        api_path = self.Templates.getFromApiPaths('mensa_push_synthesis')

        header = self.Templates.getFromHeaders('mensa_push')
        payload = self.Templates.getFromPayload('mensa_push_synthesis')
        payload['synthesis']['eventSource']=SynthesisEventSourceDoorsUnlockedAllowStart

        response_status, response_payload, response_headers = client.doPost(baseurl + api_path, header, payload)
        assert response_status == 200

    @pytestrail.case('C34')
    def test_synthesis_with_event_source_periodic_synthesis_update(self,client):
        baseurl = self.Templates.getFromConfig('$baseurl')

        api_path = self.Templates.getFromApiPaths('mensa_push_synthesis')

        header = self.Templates.getFromHeaders('mensa_push')
        payload = self.Templates.getFromPayload('mensa_push_synthesis')
        payload['synthesis']['eventSource']=SynthesisEventSourcePeriodicVehicleSynthesis

        response_status, response_payload, response_headers = client.doPost(baseurl + api_path, header, payload)
        assert response_status == 200
