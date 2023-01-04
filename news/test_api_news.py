# Schoolmate - school management system
# Copyright (C) 2018-2023  Kirill 'Kolyat' Kiselnikov  <kks.pub@gmail.com>
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

from . import urls, data_test_api_news


def test_news(apiclient):
    """Get news.

    :param apiclient: :class:`utils.client.ApiClient` instance
    """
    response = apiclient.get(urls.NEWS)
    assert response.status_code == 200
    body = response.json()
    assert data_test_api_news.validate(body) is not None


if __name__ == '__main__':
    pytest.main()
