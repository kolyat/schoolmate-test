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

import pytest

import config
from . import urls, data_test_api_news


u = config.current_config.full_url


def test_news(apiclient):
    """Get news

    :param apiclient: :class:`utils.client.ApiClient` instance
    """
    response = apiclient.get(u(urls.NEWS))
    assert response.status_code == 200
    body = response.json()
    assert data_test_api_news.validate(body) is not None


if __name__ == '__main__':
    pytest.main()
