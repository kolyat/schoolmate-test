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

from utils import rnd


validate = compile({
    '$schema': 'http://json-schema.org/draft-07/schema#',
    'type': 'object',
    'properties': {
        'pk': {'type': 'integer'},
        'date_modified': {'type': 'string', 'format': 'date-time'},
        'title': {'type': ['string', 'null']},
        'text': {'type': ['string', 'null']},
    },
    'additionalProperties': False,
    'required': ['pk', 'title', 'text']
})

create_cases = (
    ({},                                                            201),
    ({'title': rnd.random_numstr(length=256), 'text': '256 chars'}, 201),
    ({'title': rnd.random_numstr(length=257), 'text': ''},          400)
)

update_cases = (
    ({},                                                            200),
    ({'title': rnd.random_numstr(length=256), 'text': '256 chars'}, 200),
    ({'title': rnd.random_numstr(length=257), 'text': ''},          200)
)
