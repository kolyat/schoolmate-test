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

from . import urls, data_test_api_notebook


records = {}


def test_list_records(apiclient):
    """List records.

    :param apiclient: :class:`utils.client.ApiClient` instance
    """
    global records
    response = apiclient.get(urls.RECORDS)
    assert response.status_code == 200
    body = response.json()
    for el in body:
        records.update({el['pk']: el})


def test_retrieve_record(apiclient):
    """Retrieve record.

    :param apiclient: :class:`utils.client.ApiClient` instance
    """
    global records
    pk = min(records.keys())
    response = apiclient.get(f'{urls.RECORDS}{pk}/')
    assert response.status_code == 200
    body = response.json()
    assert data_test_api_notebook.validate(body) is not None


@pytest.mark.parametrize('payload, response_status',
                         data_test_api_notebook.create_cases)
def test_create_record(apiclient, payload: dict, response_status: int):
    """Create record.

    :param apiclient: :class:`utils.client.ApiClient` instance

    :param payload: payload
    :type payload: dict

    :param response_status: expected response status
    :type response_status: int
    """
    response = apiclient.post(urls.RECORDS, data=payload)
    assert response.status_code == response_status
    if response.status_code <= 300:
        body = response.json()
        assert data_test_api_notebook.validate(body) is not None


@pytest.mark.parametrize('payload, response_status',
                         data_test_api_notebook.update_cases)
def test_update_record(apiclient, payload: dict, response_status: int):
    """Update record.

    :param apiclient: :class:`utils.client.ApiClient` instance

    :param payload: payload
    :type payload: dict

    :param response_status: expected response status
    :type response_status: int
    """
    global records
    pk = sorted(records.keys())[2]
    response = apiclient.patch(f'{urls.RECORDS}{pk}/')
    assert response.status_code == response_status
    if response.status_code <= 300:
        body = response.json()
        assert data_test_api_notebook.validate(body) is not None


def test_destroy_update_record(apiclient):
    """Destroy/update record:
    1. Destroy record.
    2. Try to update destroyed record.
    3. Try to destroy record again.

    :param apiclient: :class:`utils.client.ApiClient` instance
    """
    global records
    pk = sorted(records.keys())[-1]
    url = f'{urls.RECORDS}{pk}/'
    response = apiclient.delete(url)
    assert response.status_code == 204
    response = apiclient.patch(url, data={})
    assert response.status_code == 404
    response = apiclient.delete(url)
    assert response.status_code == 404


if __name__ == '__main__':
    pytest.main()
