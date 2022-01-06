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

from typing import Union, Any
import os
import json
import logging
import http.client

import config


class Reader:
    """File parsing utility.
    Supports only JSON files.
    """

    @staticmethod
    def read_json(file_name: str) -> Union[dict, None]:
        """Read JSON file.

        :param file_name: name of a JSON file
        :type file_name: str

        :return: deserialized JSON document
        :rtype: dict
        """
        _json = None
        try:
            fp = open(file_name)
            _json = json.load(fp)
            fp.close()
        except Exception as e:
            print(f'Error in processing {file_name}')
            print(e)
        return _json


class Config(dict):
    """Class for storing configuration options.

    * **target** - testing object/server data
    * **logging** - various logging options
    """

    def __init__(self):
        super().__init__()
        self['target'] = config.DEFAULT_TARGET_CONFIG.copy()
        self['logging'] = config.DEFAULT_LOGGING_CONFIG.copy()

    def update_config(self, config_file: str) -> None:
        """Load and update configuration options from a file.

        :param config_file: config file name
        :type config_file: str
        """
        _config = None
        _, ext = os.path.splitext(config_file)
        if ext == '.json':
            _config = Reader.read_json(config_file)
        else:
            print(f'Configuration file {config_file} is not supported')
        self.target.update(_config.get('target', {}))
        self.logging.update(_config.get('logging', {}))

    @property
    def target(self) -> dict:
        """
        :return: testing object/server data
        :rtype: dict
        """
        return self['target']

    @property
    def logging(self) -> dict:
        """
        :return: logging options
        :rtype: dict
        """
        return self['logging']

    def get_user(self, target: str = 'default', user: str = 'default') -> dict:
        """Get user's registration data

        :param target: testing target (set to "default")
        :type target: str

        :param user: selected user (set to "default")
        :type user: str

        :return: user's registration data
        :rtype: dict
        """
        _target = self.target[target]
        _user = _target['users'][user]
        return _user

    def full_url(self, path: str, target: str = 'default') -> str:
        """Returns fully qualified URL

        :param path: path to endpoint (e. g., "/endpoint/example")
        :type path: str

        :param target: testing target (set to "default")
        :type target: str

        :return: full URL (e. g., "https://localhost:8000/endpoint/example")
        :rtype: str
        """
        _target = self.target[target]
        _url = ''.join((_target['protocol'], '://', _target['server'], path))
        return _url


httpclient_logger = logging.getLogger('http.client')


def httpclient_logging_patch(level: int = logging.DEBUG) -> None:
    """Enable HTTPConnection debug logging to the logging framework

    :param level: logging level (logging.DEBUG = 10 by default)
    :type level: int
    """

    def httpclient_log(*args: Any) -> None:
        httpclient_logger.log(level, ' '.join(args))

    http.client.print = httpclient_log
    http.client.HTTPConnection.debuglevel = 1
