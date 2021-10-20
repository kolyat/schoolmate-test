import pytest

from utils import client
import config
import prepare_db


@pytest.fixture(scope='session', autouse=True)
def db_prepare():
    prepare_db.prepare()


@pytest.fixture(scope='session')
def apiclient():
    _client = client.ApiClient()
    _user = config.current_config.get_user()
    # _client.set_auth(_user['username'], _user['password'])
    _client.login(_user['username'], _user['password'])
    yield _client
    _client.logout()


@pytest.fixture
def apiclient_init():
    return client.ApiClient()
