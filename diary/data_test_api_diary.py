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

from fastjsonschema import compile

import config
from utils import rnd


validate = compile({
    '$schema': 'http://json-schema.org/draft-07/schema#',
    'definitions': {
        'record': {
            'type': 'object',
            'properties': {
                'id': {'type': 'integer'},
                'user': {'type': 'string', 'minLength': 1},
                'date': {'type': 'string', 'format': 'date'},
                'lesson_number': {'type': 'integer',
                                  'minimum': 1, 'maximum': 7},
                'subject': {'type': 'string'},
                'text': {'type': 'string'},
                'marks': {'type': 'string'},
                'signature': {'type': 'string'},
            },
            'additionalProperties': False,
            'required': ['date', 'lesson_number', 'subject', 'text']
        }
    },
    'anyOf': [
        {
            'type': 'array',
            'minItems': 7,
            'maxItems': 7,
            'items': {'$ref': '#/definitions/record'}
        },
        {'$ref': '#/definitions/record'},
        {'properties': {'school_form': {'type': 'string'}}},
        {'properties': {'lesson_number': {'type': 'string'}}},
        {'properties': {'subject': {'type': 'string'}}},
    ]
})

auth_data = (
    (
        config.current_config.get_user(user='default')['username'],
        config.current_config.get_user(user='default')['password'],
        200
    ),
    (
        config.current_config.get_user(user='admin')['username'],
        config.current_config.get_user(user='admin')['password'],
        424
    )
)

template = {
    'lesson_number': 3,
    'subject': 'Физика',
    'text': 'Some text here'
}

positive_cases = (
    ({'lesson_number': 3}, 201),
    ({'lesson_number': 1}, 201),
    ({'lesson_number': 7}, 201),
    ({'subject': 'Алгебра'}, 202),
    ({'subject': ' '}, 202),
    ({'text': 'For testing'}, 202),
    ({'text': rnd.random_str(9000)}, 202),
    ({'text': ''}, 202)
)

negative_cases = (
    ({'lesson_number': -1}, 400),
    ({'lesson_number': 0}, 400),
    ({'lesson_number': 8}, 400),
    ({'lesson_number': 100}, 400),
    ({'lesson_number': 3.5}, 400),
    ({'lesson_number': '3'}, 201),
    ({'lesson_number': None}, 400),
    ({'subject': 'no_subject'}, 400),
    ({'subject': None}, 400),
    ({'subject': 123}, 400),
    ({'text': 123}, 202),
    ({'text': None}, 202)
)

incomplete_payload = (
    ({'subject': 'Физика', 'text': 'Some text here'}, 400),
    ({'lesson_number': 3, 'text': 'Some text here'}, 400),
    ({'lesson_number': 3, 'subject': 'Физика'}, 201)
)
