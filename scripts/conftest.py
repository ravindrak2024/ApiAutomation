import pytest
from handlers.ParametrizationDataHandler import ParameterizationHandler
from handlers.TemplateHandler import TemplateHandler
from utils.APIRequests import ApiRequests
import re

def pytest_addoption(parser):
     parser.addoption("--env", action="store", help="my option: type1 or type2")

@pytest.fixture
def client():
    api_client=ApiRequests()
    yield api_client
    api_client=None






def pytest_generate_tests(metafunc):
    '''
    Hook that generate the data from the method name.
    :param metafunc: Provided by pytest.
    :return: list if data in format step & validation
    '''
    if 'param' in metafunc.function.__name__:
        filename=re.findall('param[a-z]+_(.+)',metafunc.function.__name__)[0]
        parameter_handler = ParameterizationHandler('./resources/testdata/'+filename+'.xlsx',
                                                    TemplateHandler.getTemplates(metafunc.config.getoption("env")))


        return metafunc.parametrize("step,validations", parameter_handler.getParameters())
