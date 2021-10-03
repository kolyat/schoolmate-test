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

import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

INSTALLED_APPS = [
    # Django apps
    'django.contrib.contenttypes',
    'django.contrib.auth',
    # Project apps
    'school.apps.SchoolConfig',
    'account.apps.AccountConfig',
    'news.apps.NewsConfig',
    'timetable.apps.TimetableConfig',
    'diary.apps.DiaryConfig'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'schoolmate',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

LANGUAGES = (
    ('ru', 'Русский'),
    ('en', 'English'),
    ('de', 'Deutsch')
)
LANGUAGE_CODE = LANGUAGES[0][0]

LATEST_NEWS_COUNT = 300