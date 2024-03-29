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

from django.core.management import base

from schoolmate import settings
from school import models as school_models
from . import _db_data


def prepare_school():
    """Generate model of a school
    """
    print('Create data for SCHOOL app:')
    print('    {:.<30}...'.format('School forms'), end='', flush=True)
    for l in _db_data.FORM_LETTERS:
        school_models.FormLetter(letter=l).save()
    _letters = school_models.FormLetter.objects.all()
    for n in settings.FORM_NUMBERS:
        _number = school_models.FormNumber(number=n)
        _number.save()
        for l in _letters:
            school_models.SchoolForm(
                form_number=_number, form_letter=l
            ).save()
    print('OK')
    print('    {:.<30}...'.format('School subjects'), end='', flush=True)
    for s in _db_data.SUBJECTS:
        school_models.SchoolSubject(subject=s).save()
    print('OK')
    print('    {:.<30}...'.format('Daily schedule'), end='', flush=True)
    for d in _db_data.DAILY_SCHEDULE:
        school_models.DailySchedule(**d).save()
    print('OK')
    print('    {:.<30}...'.format('Year schedule'), end='', flush=True)
    _sy = school_models.SchoolYear(**_db_data.SCHOOL_YEAR)
    _sy.save()
    for y in _db_data.YEAR_SCHEDULE:
        school_models.YearSchedule(school_year=_sy, **y).save()
    print('OK')
    print('    {:.<30}...'.format('Classrooms'), end='', flush=True)
    for c in _db_data.CLASSROOMS:
        school_models.Classroom(**c).save()
    print('OK')


class Command(base.BaseCommand):
    requires_migrations_checks = False

    def handle(self, *args, **options):
        prepare_school()
