from testinits.TestBase import *
from .scriptutils.CommonActions import *
import pytest
#All hal specific initialization to take place here.
class HALTestbase(TestBase):
    commonAction=None

    @pytest.fixture(autouse=True)
    def setup(self):
        HALTestbase.commonAction = CommonActions(TestBase.Templates)

        response_status, response_payload, response_headers = HALTestbase.commonAction.createTenant()

        if response_status == 201:
            logger.debug("Tenant created sucessfully ")
        else:
            # assert response_payload['UserMessage']=='Tenant with this ID already exists'
            logger.debug("Tenant already exists!!!")

        response_status, response_payload, response_headers = HALTestbase.commonAction.createVendor()

        if response_status == 201:
            logger.debug("Vendor created sucessfully ")
        else:
            # assert response_payload['UserMessage']=='Vendor with this ID already exists'
            logger.debug("Vendor already exists!!!")

    def setup_method(self, method):
        """ setup any state tied to the execution of the given method in a
        class.  setup_method is invoked for every test method of a class.
        """
        logger.info("##############  Starting testcase {} ############### ".format(method.__name__))


    def teardown_method(self, method):
        """ teardown any state that was previously setup with a setup_method
        call.
        """
        logger.info("##############  Finished testcase {} ###############".format(method.__name__))

