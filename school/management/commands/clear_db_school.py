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

from school import models as school_models


def clear_school():
    """Remove school's model from database
    """
    print('Remove SCHOOL app data...', end=' ', flush=True)
    school_models.Classroom.objects.all().delete()
    school_models.YearSchedule.objects.all().delete()
    school_models.SchoolYear.objects.all().delete()
    school_models.DailySchedule.objects.all().delete()
    school_models.SchoolSubject.objects.all().delete()
    school_models.SchoolForm.objects.all().delete()
    school_models.FormNumber.objects.all().delete()
    school_models.FormLetter.objects.all().delete()
    print('OK')


class Command(base.BaseCommand):
    requires_migrations_checks = False

    def handle(self, *args, **options):
        clear_school()
