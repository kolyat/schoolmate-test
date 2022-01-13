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

from django.core.management import base
from utils import rnd

from account import models as account_models
from notebook import models as notebook_models


def prepare_notebook():
    """Generate notebook testing data
    """
    print('Create data for NOTEBOOK app:')
    user = account_models.SchoolUser.objects.get(username='sam')
    n = 5
    print('    {:.<30}...'.format(f'sam - {n} records'), end='', flush=True)
    for i in range(n):
        note = rnd.new_note()
        notebook_models.NotebookRecord(
            user=user,
            title=note['title'],
            text=note['text']
        ).save()
    print('OK')


class Command(base.BaseCommand):
    requires_migrations_checks = False

    def handle(self, *args, **options):
        prepare_notebook()
