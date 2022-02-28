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

import pytest

from . import urls, data_test_api_user_info


def test_get_username(apiclient):
    """Get username.

    :param apiclient: :class:`utils.client.ApiClient` instance
    """
    response = apiclient.get(urls.USER_NAME)
    assert response.status_code == 200
    body = response.json()
    assert body['username'] == apiclient.username


def test_change_username(apiclient):
    f"""Try to change username via {urls.USER_NAME}.

    :param apiclient: :class:`utils.client.ApiClient` instance
    """
    data = {'username': 'admin'}
    response = apiclient.post(urls.USER_NAME, data=data)
    assert response.status_code == 405
    response = apiclient.put(urls.USER_NAME, data=data)
    assert response.status_code == 405
    response = apiclient.patch(urls.USER_NAME, data=data)
    assert response.status_code == 405


def test_get_user_info(apiclient):
    """Get user info.

    :param apiclient: :class:`utils.client.ApiClient` instance
    """
    response = apiclient.get(urls.USER_INFO)
    assert response.status_code == 200
    body = response.json()
    assert data_test_api_user_info.validate(body) is not None


def test_change_user_info(apiclient):
    f"""Try to change username via {urls.USER_INFO}.

    :param apiclient: :class:`utils.client.ApiClient` instance
    """
    data = {'username': 'admin', 'email': 'email@changed.xxx'}
    response = apiclient.post(urls.USER_INFO, data=data)
    assert response.status_code == 405
    response = apiclient.put(urls.USER_INFO, data=data)
    assert response.status_code == 405
    response = apiclient.patch(urls.USER_INFO, data=data)
    assert response.status_code == 405


@pytest.mark.parametrize('payload, response_status, response_body',
                         data_test_api_user_info.user_settings)
def test_change_user_settings(apiclient, payload: dict, response_status: int,
                              response_body: dict):
    """Change user settings.

    :param apiclient: :class:`utils.client.ApiClient` instance

    :param payload: request payload
    :type payload: dict

    :param response_status: expected response status
    :type response_status: int

    :param response_body: expected body in response
    :type response_body: dict
    """
    response = apiclient.patch(urls.USER_SETTINGS, data=payload)
    assert response.status_code == response_status
    if response.status_code < 300:
        body = response.json()
        assert set(response_body.items()) <= set(body.items())


def test_change_user_email(apiclient):
    f"""Try to change e-mail via {urls.USER_SETTINGS}.

    :param apiclient: :class:`utils.client.ApiClient` instance
    """
    fake_email = 'x@x.xx'
    response = apiclient.patch(urls.USER_SETTINGS, data={'email': fake_email})
    assert response.status_code == 200
    response = apiclient.get(urls.USER_INFO)
    body = response.json()
    assert body['email'] != fake_email


if __name__ == '__main__':
    pytest.main()
