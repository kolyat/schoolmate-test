# Schoolmate - school management system
# Copyright (C) 2018-2021  Kirill 'Kolyat' Kiselnikov  <kks.pub@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import copy
import datetime
import logging
import pytest

import config
from . import urls, data_test_api_diary


u = config.current_config.full_url

t = datetime.date.today()
d = datetime.timedelta(days=1)


@pytest.mark.parametrize('username, password, response_status',
                         data_test_api_diary.auth_data)
def test_retrieve(apiclient_init,
                  username: str, password: str, response_status: int):
    """Cases with response data

    :param apiclient_init: not authenticated instance of
                           :class:`utils.client.ApiClient`

    :param username: user's username
    :type username: str

    :param password: user's password
    :type password: str

    :param response_status: expected response status
    :type response_status: int
    """
    apiclient_init.login(username, password)
    url = u(urls.DIARY) + f'{t.year}/{t.month}/{t.day}/'
    response = apiclient_init.get(url)
    assert response.status_code == response_status
    logging.debug(response.json())
    apiclient_init.logout()


@pytest.mark.parametrize('payload, response_status',
                         data_test_api_diary.positive_cases)
def test_positive_cases(apiclient, payload: dict, response_status: int):
    """Positive create/update cases

    :param apiclient: :class:`utils.client.ApiClient` instance

    :param payload: additional payload
    :type payload: dict

    :param response_status: expected response status
    :type response_status: int
    """
    _t = t + d
    url = u(urls.DIARY) + f'{_t.year}/{_t.month}/{_t.day}/'
    data = copy.deepcopy(data_test_api_diary.template)
    data.update(payload)
    response = apiclient.post(url, data=data)
    assert response.status_code == response_status
    body = response.json()
    logging.debug(body)
    assert data_test_api_diary.validate(body) is not None
    assert set(payload.items()) <= set(body.items())


@pytest.mark.parametrize('payload, response_status',
                         data_test_api_diary.negative_cases)
def test_negative_cases(apiclient, payload: dict, response_status: int):
    """Negative create/update cases

    :param apiclient: :class:`utils.client.ApiClient` instance

    :param payload: additional payload
    :type payload: dict

    :param response_status: expected response status
    :type response_status: int
    """
    _t = t + d * 2
    url = u(urls.DIARY) + f'{_t.year}/{_t.month}/{_t.day}/'
    data = copy.deepcopy(data_test_api_diary.template)
    data.update(payload)
    response = apiclient.post(url, data=data)
    logging.debug(response.json())
    assert response.status_code == response_status


@pytest.mark.parametrize('payload, response_status',
                         data_test_api_diary.incomplete_payload)
def test_incomplete_payload(apiclient, payload: dict, response_status: int):
    """Negative tests with incomplete payload

    :param apiclient: :class:`utils.client.ApiClient` instance

    :param payload: incomplete payload
    :type payload: dict

    :param response_status: expected response status
    :type response_status: int
    """
    _t = t + d * 3
    url = u(urls.DIARY) + f'{_t.year}/{_t.month}/{_t.day}/'
    response = apiclient.post(url, data=payload)
    logging.debug(response.json())
    assert response.status_code == response_status


if __name__ == '__main__':
    pytest.main()
