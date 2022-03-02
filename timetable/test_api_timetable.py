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

from . import data_test_api_timetable


@pytest.mark.parametrize('url, response_status',
                         data_test_api_timetable.cases)
def test_get_timetable(apiclient, url: str, response_status: int):
    """Retrieve timetable.

    :param apiclient: :class:`utils.client.ApiClient` instance

    :param url: endpoint URL
    :type url: str

    :param response_status: expected response status
    :type response_status: int
    """
    response = apiclient.get(url)
    assert response.status_code == response_status
    body = response.json()
    assert data_test_api_timetable.validate(body) is not None


if __name__ == '__main__':
    pytest.main()
