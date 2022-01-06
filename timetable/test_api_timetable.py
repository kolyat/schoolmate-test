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

import logging
import pytest

import config
from . import data_test_api_timetable


u = config.current_config.full_url


@pytest.mark.parametrize('url, response_status, validate',
                         data_test_api_timetable.positive_cases)
def test_positive_cases(apiclient, url: str, response_status: int, validate):
    """Positive cases with response data

    :param apiclient: :class:`utils.client.ApiClient` instance

    :param url: endpoint URL
    :type url: str

    :param response_status: expected response status
    :type response_status: int

    :param validate: schema validation function for response data
    """
    response = apiclient.get(u(url))
    assert response.status_code == response_status
    body = response.json()
    logging.debug(body)
    assert validate(body) is not None


@pytest.mark.parametrize('url, response_status, expected_body',
                         data_test_api_timetable.empty_cases)
def test_empty_cases(apiclient, url: str , response_status: int,
                     expected_body: list):
    """Cases with empty response data

    :param apiclient: :class:`utils.client.ApiClient` instance

    :param url: endpoint URL
    :type url: str

    :param response_status: expected response status
    :type response_status: int

    :param expected_body: expected body of response
    :type expected_body: list
    """
    response = apiclient.get(u(url))
    assert response.status_code == response_status
    body = response.json()
    logging.debug(body)
    assert body == expected_body


@pytest.mark.parametrize('url, response_status',
                         data_test_api_timetable.error_cases)
def test_error_cases(apiclient, url: str, response_status: int):
    """Test behaviour with invalid url

    :param apiclient: :class:`utils.client.ApiClient` instance

    :param url: endpoint URL
    :type url: str

    :param response_status: expected response status
    :type response_status: int
    """
    response = apiclient.get(u(url))
    assert response.status_code == response_status


if __name__ == '__main__':
    pytest.main()
