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

from fastjsonschema import compile


validate = compile({
    '$schema': 'http://json-schema.org/draft-07/schema#',
    'type': 'object',
    'properties': {
        'username': {'type': 'string', 'minLength': 1},
        'first_name': {'type': 'string', 'minLength': 0},
        'last_name': {'type': 'string', 'minLength': 0},
        'patronymic_name': {'type': ['string', 'null']},
        'birth_date': {
            'anyOf': [
                {'type': 'string', 'format': 'date'},
                {'type': 'null'}
            ]
        },
        'email': {'type': 'string', 'format': 'idn-email'},
        'school_form': {
            'anyOf': [
                {'type': 'string', 'pattern': '\d+\D+'},
                {'type': 'null'}
            ]
        },
        'language': {'type': 'string', 'minLength': 2},
        'skin': {'type': 'string', 'minLength': 2},
        'languages': {
            'type': 'array',
            'minItems': 1,
            'uniqueItems': True,
            'items': {
                'type': 'object',
                'properties': {
                    'language_code': {'type': 'string', 'minLength': 2},
                    'language_name': {'type': 'string', 'minLength': 2},
                },
                'additionalProperties': False,
                'required': ['language_code', 'language_name']
            }
        },
        'skins': {
            'type': 'array',
            'minItems': 1,
            'uniqueItems': True,
            'items': {
                'type': 'object',
                'properties': {
                    'skin': {'type': 'string', 'minLength': 2},
                    'skin_name': {'type': 'string', 'minLength': 2},
                },
                'additionalProperties': False,
                'required': ['skin', 'skin_name']
            }
        }
    },
    'additionalProperties': False,
    'required': [
        'username',
        'first_name',
        'last_name',
        'patronymic_name',
        'birth_date',
        'email',
        'school_form',
        'language',
        'skin',
        'languages',
        'skins'
    ]
})

user_info_cases = (
    ({'language': 'de'}, 202, {'language': 'de'}),
    ({'language': 'xxx'}, 400, {}),
    ({'language': 123}, 400, {}),
    ({'language': ''}, 202, {}),
    ({'skin': 'material'}, 202, {'skin': 'material'}),
    ({'skin': 'xxx'}, 400, {}),
    ({'skin': 123}, 400, {}),
    ({'skin': ''}, 202, {}),
    ({'email': 'x@x.xx'}, 202, {}),
    ({}, 202, {})
)
