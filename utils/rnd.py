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

import random
import mimesis
import mimesis.builtins
from mimesis import enums, locales


LANGUAGES = ('ru', 'en', 'de')
SKINS = ('compact', 'contrast', 'flat', 'material', 'mini')
FORM_NUMBERS = range(1, 12)
FORM_LETTERS = 'АБ'


def random_char() -> str:
    """Get random UTF-8 character

    :return: non-space printable unicode character
    :rtype: str
    """
    random.seed()
    while True:
        char = chr(random.randint(0, 0x10FFFF))
        if char.isprintable() and not char.isspace():
            return char


def random_str(length: int = 9) -> str:
    """Get string with random UTF-8 characters

    :param length: string's length (default = 9)
    :type length: int

    :return: string with random characters
    :rtype: str
    """
    return ''.join([random_char() for _ in range(length)])


def random_numstr(length: int = 9) -> str:
    """Get string with digits

    :param length: string's length (default = 9)
    :type length: int

    :return: string with random digits
    :rtype: str
    """
    return ''.join([str(random.randint(0, 9)) for _ in range(length)])


def random_id() -> int:
    """Generate id between 100000 and 999999 inclusive

    :return: random id
    :rtype: int
    """
    random.seed()
    return random.randint(100000, 999999)


def new_schoolform() -> dict:
    """Generate school form data

    :return: dictionary with school form number and letter
    :rtype: dict
    """
    return {
        'form_number': random.choice(FORM_NUMBERS),
        'form_letter': random.choice(FORM_LETTERS)
    }


def new_schooluser() -> dict:
    """Generate data for fake school user

    :return: dictionary with personal data
    :rtype: dict
    """
    random.seed()
    _person = mimesis.Person(locales.RU)
    _person_ru = mimesis.builtins.RussiaSpecProvider()
    _date = mimesis.Datetime()
    _gender = random.choice((enums.Gender.MALE, enums.Gender.FEMALE))
    _username = _person.username('ld')
    return {
        'username': _username,
        'password': _username,
        'first_name': _person.name(_gender),
        'last_name': _person.surname(_gender),
        'patronymic_name': _person_ru.patronymic(_gender),
        'birth_date': _date.formatted_date(fmt='%Y-%m-%d',
                                           start=1990, end=2000),
        'email': _person.email(),
        'language': random.choice(LANGUAGES),
        'skin': random.choice(SKINS),
        'is_active': True,
        'is_staff': False,
        'is_superuser': False
    }


def new_article() -> dict:
    """Generate news article

    :return: dictionary with title and text
    :rtype: dict
    """
    random.seed()
    _text = mimesis.Text()
    return {
        'title': _text.title(),
        'content': _text.text(random.randint(3, 9))
    }
