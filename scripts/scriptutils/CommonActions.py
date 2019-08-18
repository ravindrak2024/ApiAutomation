# This file to contain all commonly used functions here like create tenant,vendor,asset.

from utils.APIRequests import *
from utils.RandomGenerator import *
import ast


class CommonActions:

    def __init__(self,templates):
        self.templates=templates
        self.baseurl=templates.getFromConfig('$baseurl')

    def createTenant(self):
        api_path = self.templates.getFromApiPaths('create_tenant')
        header = self.templates.getFromHeaders('summon_initiated')
        payload = self.templates.getFromPayload('create_tenant')
        print("Type of header {}".format(type(header)))
        print("Type of payload {}".format(type(payload)))
        response_status, response_payload, response_headers = doPost(self.baseurl + api_path, header, payload)
        return response_status, response_payload, response_headers
        # do assertion here

    def createVendor(self):
        api_path = self.templates.getFromApiPaths('create_vendor')
        header = self.templates.getFromHeaders('summon_initiated')
        payload = self.templates.getFromPayload('create_vendor')
        response_status, response_payload, response_headers = doPost(self.baseurl + api_path, header, payload)
        return response_status, response_payload, response_headers
        # do assertion here

    def createAsset(self,asset_id):
        api_path = self.templates.getFromApiPaths('create_asset')
        header = self.templates.getFromHeaders('summon_initiated')
        payload = self.templates.getFromPayload('create_asset')
        payload['id'] = asset_id
        response_status, response_payload, response_headers = doPost(self.baseurl + api_path, header, payload)
        assert response_status == 201
        return response_status, response_payload, response_headers
        #do assertion here


    def reserveAsset(self,asset_id,):
        api_path = self.templates.getFromApiPaths('si_action')
        api_path=api_path.replace('#asset_id',asset_id)
        header = self.templates.getFromHeaders('summon_initiated')
        payload = self.templates.getFromPayload('reserve')
        payload['key_validity_start_in_epoch']=generateRandom(RandomDataType.TIMESTAMP)
        payload['key_validity_stop_in_epoch']=generateRandom(RandomDataType.TIMESTAMP,future_time_in_min=60)
        response_status, response_payload, response_headers = doPut(self.baseurl + api_path, header, payload)
        assert response_status==200
        return response_status, response_payload, response_headers

    def reservation_confirmed(self,asset_id):
        api_path = self.templates.getFromApiPaths('vi_action')
        api_path = api_path.replace('#asset_id', asset_id)
        header = self.templates.getFromHeaders('vendor_initiated')
        payload = self.templates.getFromPayload('reservation_confirmed')
        response_status, response_payload, response_headers = doPut(self.baseurl + api_path, header, payload)
        assert response_status == 204
        return response_status, response_payload, response_headers


    def extractDataFromStep(self,step):
        '''
        Takes step list.
        :param step: [method,payload,header,status]
        :return: method,payload,header,status
        '''
        #ast.literal_eval(data)
        header=payload=dict()
        if isinstance(step[2],str):
            header=ast.literal_eval(step[2])
        else:
            header = step[2]

        if isinstance(step[1],str):
            payload=ast.literal_eval(step[1])
        else:
            payload=step[1]

        return step[0],payload,header,step[3]



