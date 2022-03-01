# Schoolmate - school management system
# Copyright (C) 2018-2022  Kirill 'Kolyat' Kiselnikov  <kks.pub@gmail.com>
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
import pytest

from . import urls, data_test_api_diary


t = datetime.date.today()
d = datetime.timedelta(days=1)


@pytest.mark.parametrize('username, password, response_status',
                         data_test_api_diary.auth_data)
def test_get_record(apiclient_init,
                    username: str, password: str, response_status: int):
    """Retrieve diary record.

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
    url = f'{urls.DIARY}{t.year}/{t.month}/{t.day}/'
    response = apiclient_init.get(url)
    apiclient_init.logout()
    assert response.status_code == response_status


@pytest.mark.parametrize('payload, response_status, compare',
                         data_test_api_diary.positive_cases)
def test_edit_record_positive(apiclient, payload: dict, response_status: int,
                              compare: bool):
    """Create/update record: positive cases.

    :param apiclient: :class:`utils.client.ApiClient` instance

    :param payload: additional payload
    :type payload: dict

    :param response_status: expected response status
    :type response_status: int

    :param compare: if request payload need to be compared with response body
    :type compare: bool
    """
    _t = t + d
    url = f'{urls.DIARY}{_t.year}/{_t.month}/{_t.day}/'
    data = copy.deepcopy(data_test_api_diary.template)
    data.update(payload)
    response = apiclient.post(url, data=data)
    assert response.status_code == response_status
    body = response.json()
    assert data_test_api_diary.validate(body) is not None
    assert set(payload.items()) <= set(body.items()) if compare else True


@pytest.mark.parametrize('payload, response_status',
                         data_test_api_diary.negative_cases)
def test_edit_record_negative(apiclient, payload: dict, response_status: int):
    """Create/update record: negative cases.

    :param apiclient: :class:`utils.client.ApiClient` instance

    :param payload: additional payload
    :type payload: dict

    :param response_status: expected response status
    :type response_status: int
    """
    _t = t + d * 2
    url = f'{urls.DIARY}{_t.year}/{_t.month}/{_t.day}/'
    data = copy.deepcopy(data_test_api_diary.template)
    data.update(payload)
    response = apiclient.post(url, data=data)
    assert response.status_code == response_status


@pytest.mark.parametrize('payload, response_status',
                         data_test_api_diary.incomplete_payload)
def test_incomplete_payload(apiclient, payload: dict, response_status: int):
    """Create/update record: tests with incomplete payload.

    :param apiclient: :class:`utils.client.ApiClient` instance

    :param payload: incomplete payload
    :type payload: dict

    :param response_status: expected response status
    :type response_status: int
    """
    _t = t + d * 3
    url = f'{urls.DIARY}{_t.year}/{_t.month}/{_t.day}/'
    response = apiclient.post(url, data=payload)
    assert response.status_code == response_status


if __name__ == '__main__':
    pytest.main()
