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


validate = compile({
    '$schema': 'http://json-schema.org/draft-07/schema#',
    'type': 'array',
    'minItems': 0,
    'uniqueItems': False,
    'items': {
        'type': 'object',
        'properties': {
            'created': {'type': 'string', 'format': 'date'},
            'title': {'type': 'string', 'minLength': 1},
            'content': {'type': 'string', 'minLength': 1},
            'author': {'type': ['string', 'null']},
        },
        'additionalProperties': False,
        'required': ['created', 'title', 'content', 'author']
    }
})
