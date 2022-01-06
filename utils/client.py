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

from typing import Union
import re
import logging
import requests
from requests import auth

import config
from . import urls


log = logging.getLogger(__name__)
u = config.current_config.full_url


class ApiClient(requests.Session):
    """Class derived from :class:`requests.Session` with some custom methods

    :ivar csrf_token: Cross-Site Request Forgery (CSRF) protection token
    """

    def __init__(self):
        super().__init__()
        self.csrf_token = None

    def set_auth(self,
                 username: Union[None, str] = None,
                 password: Union[None, str] = None) -> None:
        """Set up auth type. Now supports only basic authentication.

        :param username: user's name
        :type username: str

        :param password: user's password
        :type password: str
        """
        self.auth = auth.HTTPBasicAuth(username, password)

    def login(self,
              username: Union[None, str] = None,
              password: Union[None, str] = None) -> None:
        # TODO: description
        # TODO: add timeout
        response = self.get(u(urls.LOGIN))
        r = re.search(r"'csrfmiddlewaretoken' value='(\S+)'", response.text)
        try:
            csrf_token_form = r.group(1)
        except AttributeError:
            csrf_token_form = None
            log.warning('Could not find csrfmiddlewaretoken in login form')
        self.csrf_token = response.cookies.get('csrftoken', None)
        self.headers.update({'X-CSRFToken': self.csrf_token})
        auth_data = {}
        auth_data.update({'username': username}) if username else None
        auth_data.update({'password': password}) if password else None
        auth_data.update({'csrfmiddlewaretoken': csrf_token_form}) \
            if csrf_token_form else None
        # TODO: add timeout, resolve redirects
        response = self.post(u(urls.LOGIN), data=auth_data)
        self.csrf_token = response.cookies.get('csrftoken', None)
        self.headers.update({'X-CSRFToken': self.csrf_token})

    def logout(self) -> None:
        # TODO: description
        self.get(u(urls.LOGOUT))
        self.headers.pop('X-CSRFToken')
        self.csrf_token = None
