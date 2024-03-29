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

from fastjsonschema import compile

from .urls import TIMETABLE_DATA


validate = compile({
    '$schema': 'http://json-schema.org/draft-07/schema#',
    'type': 'array',
    'minItems': 0,
    'uniqueItems': True,
    'items': {
        'type': 'object',
        'properties': {
            'form_number': {'type': 'integer', 'minimum': 0},
            'form_letter': {'type': 'string'},
            'lessons': {
                'type': 'array',
                'minItems': 0,
                'maxItems': 42,
                'uniqueItems': True,
                'items': {
                    'type': 'object',
                    'properties': {
                        'day_of_week': {'type': 'integer',
                                        'minimum': 1, 'maximum': 8},
                        'lesson_number': {'type': 'integer',
                                          'minimum': 1, 'maximum': 7},
                        'subject': {'type': 'string', 'minLength': 1},
                        'classroom': {'type': 'string', 'minLength': 0}
                    },
                    'additionalProperties': False,
                    'required': ['day_of_week', 'lesson_number',
                                 'subject', 'classroom']
                }
            }
        }
    }
})

url = f'{TIMETABLE_DATA}?form_number='

cases = (
    (TIMETABLE_DATA, 200),
    (f'{url}-1',     200),
    (f'{url}0',      200),
    (f'{url}9',      200),
    (f'{url}999',    200),
    (f'{url}abc',    200),
    (url,            200)
)
