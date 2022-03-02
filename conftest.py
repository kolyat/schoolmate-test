import pytest

from utils import client
import config
import prepare_db


def pytest_addoption(parser):
    parser.addoption('--prepare-db', action='store_const', const=True)


@pytest.fixture(scope='session', autouse=True)
def db_prepare(request):
    if request.config.getoption('--prepare-db'):
        prepare_db.prepare()


@pytest.fixture(scope='session')
def apiclient():
    user = config.current_config.get_user()
    _client = client.ApiClient(user['username'], user['password'])
    _client.login()
    yield _client
    _client.logout()


@pytest.fixture
def apiclient_init():
    return client.ApiClient()
