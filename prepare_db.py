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

import os

from utils import db


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'schoolmate.settings')
APPS = (
    'school',
    'account',
    'news',
    'timetable',
    'diary',
    'notebook'
)


def prepare():
    import django
    django.setup()
    from django.conf import settings
    _db = db.Db(settings.DATABASES['default'], settings.BASE_DIR)

    for a in reversed(APPS):
        _db.clear(a)
    for a in APPS:
        _db.populate(a)


if __name__ == '__main__':
    prepare()
