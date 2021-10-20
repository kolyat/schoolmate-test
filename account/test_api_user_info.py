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

import logging
import pytest

import config
from . import urls, data_test_api_user_info


u = config.current_config.full_url


def test_get_user_info(apiclient):
    """Get user info

    :param apiclient: :class:`utils.client.ApiClient` instance
    """
    response = apiclient.get(u(urls.USER_INFO))
    assert response.status_code == 200
    body = response.json()
    logging.debug(body)
    assert data_test_api_user_info.validate(body) is not None


@pytest.mark.parametrize('payload, response_status, response_body',
                         data_test_api_user_info.lang_cases)
def test_change_user_language(apiclient, payload: dict, response_status: int,
                              response_body: dict):
    """Change user language

    :param apiclient: :class:`utils.client.ApiClient` instance

    :param payload: request payload
    :type payload: dict

    :param response_status: expected response status
    :type response_status: int

    :param response_body: expected body in response
    :type response_body: dict
    """
    response = apiclient.patch(u(urls.USER_INFO), data=payload)
    assert response.status_code == response_status
    if response.status_code < 300:
        body = response.json()
        logging.debug(body)
        assert set(response_body.items()) <= set(body.items())


if __name__ == '__main__':
    pytest.main()
