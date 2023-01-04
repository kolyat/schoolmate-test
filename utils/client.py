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

from typing import Union
import re
import logging
import json
import requests
from requests import auth

import config
from . import urls


log = logging.getLogger(__name__)


class ApiClient(requests.Session):
    """Class derived from :class:`requests.Session` with some custom methods.

    :ivar csrf_token: Cross-Site Request Forgery (CSRF) protection token
    """

    def __init__(self,
                 username: Union[None, str] = None,
                 password: Union[None, str] = None) -> None:
        """
        :param username: user's name
        :type username: str

        :param password: user's password
        :type password: str
        """
        super().__init__()
        self.username = username
        self.password = password
        self.csrf_token = None

    def request(self, method, url, **kwargs):
        """Modified version of `requests.Session.request`:
        - converts `url` parameter to fully qualified URL
        - logs body of a response
        """
        full_url = config.current_config.full_url(url)
        response = super().request(method, full_url, **kwargs)
        try:
            log.debug(response.json())
        except json.JSONDecodeError:
            log.debug(response.text)
        return response

    def set_auth(self,
                 username: Union[None, str] = None,
                 password: Union[None, str] = None) -> None:
        """Set up auth type. Now supports only basic authentication.

        :param username: user's name
        :type username: str

        :param password: user's password
        :type password: str
        """
        self.auth = auth.HTTPBasicAuth(
            username if username else self.username,
            password if password else self.password
        )

    def login(self,
              username: Union[None, str] = None,
              password: Union[None, str] = None) -> None:
        """Perform log-in.

        :param username: user's name
        :type username: str

        :param password: user's password
        :type password: str
        """
        response = self.get(urls.LOGIN)
        r = re.search(r"'csrfmiddlewaretoken' value='(\S+)'", response.text)
        try:
            csrf_token_form = r.group(1)
        except AttributeError:
            csrf_token_form = None
            log.warning('Could not find csrfmiddlewaretoken in login form')
        self.csrf_token = response.cookies.get('csrftoken', None)
        self.headers.update({'X-CSRFToken': self.csrf_token})
        auth_data = {
            'username': username if username else self.username,
            'password': password if password else self.password
        }
        auth_data.update({'csrfmiddlewaretoken': csrf_token_form}) \
            if csrf_token_form else None
        response = self.post(urls.LOGIN, data=auth_data)
        self.csrf_token = response.cookies.get('csrftoken', None)
        self.headers.update({'X-CSRFToken': self.csrf_token})

    def logout(self) -> None:
        """Perform log-out.
        """
        self.get(urls.LOGOUT)
        self.headers.pop('X-CSRFToken')
        self.csrf_token = None
