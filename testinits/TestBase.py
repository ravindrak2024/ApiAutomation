import pytest
from handlers.TemplateHandler import *

logger=LogInitilizer.getLogger()
class TestBase():
    environment=None
    Templates=None

    @pytest.fixture(autouse=True, scope='session')
    def env(self,request):
        logger.debug("Inside set Environment")
        TestBase.environment = request.config.getoption("--env")
        TestBase.Templates=TemplateHandler.getTemplates(TestBase.environment)

