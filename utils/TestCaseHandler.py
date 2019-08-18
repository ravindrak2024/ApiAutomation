
class TestCaseHandler:

    def __init__(self,testcases,setup):
        self.testcases=testcases
        self.setup=setup

#[['TESTCASE,create_ble_key_client,12146045,,,first', 'INCLUDE,Create tenant_vendor_asset_reserve_with_012345678_asset', 'HTTP,PUT,$$apigateway_url/hardware-integration/client/api/v3/asset/$asset_id_0_8/action,{"action":"create_ble_key", "rental_id":"1234rental","vendor_data": {"$vendor_id_0_8": "12345"},"key_validity_start_in_epoch": 1550643333,"key_validity_stop_in_epoch": 1550668696,"is_first_key_for_rental":"true"},{"Authorization-Microservice":"$$microservice_token_sum","Application-Id":"$$application_id_sum"},200,$HW_291_create_ble_res', 'ASSERTEQ,$HW_291_create_ble_res["ble_key"],ble_key_A'], ['TESTCASE,create_ble_key_client without reserving asset,12146046', 'INCLUDE,Create tenant_vendor_asset_reserve_with_012345678_asset', 'HTTP,PUT,$$apigateway_url/hardware-integration/client/api/v3/asset/$asset_id_0_8/action,{"action":"create_ble_key", "rental_id":"1234rental","vendor_data": {"$vendor_id_0_8": "12345"},"key_validity_start_in_epoch": 1550643333,"key_validity_stop_in_epoch": 1550668696,"is_first_key_for_rental":"true"},{"Authorization-Microservice":"$$microservice_token_sum","Application-Id":"$$application_id_sum"},200,$HW_291_create_ble_res', 'ASSERTEQ,$HW_291_create_ble_res["ble_key"],ble_key_A']]
    def searchTestCaseIndex(self,tag):
        for tc in self.testcases:
            for line in tc:
                if tag in line:
                    return tc
        return None


    def searchTestCaseByName(self,tcname):
        for tc in self.testcases:
            for line in tc:
                if tcname in line:
                    return tc
        return None