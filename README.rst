**************************************************
Automated testing framework for Schoolmate project
**************************************************

Contents
========

* | Applications: ``account``, ``diary``, ``news``, ``school``, ``timetable``,
    ``notebook``.
  | Each directory contains Django application files (``apps.py``,
    ``models.py``), testing scripts with data and ``urls``, and database
    ``management`` commands with predefined test data.
* ``logs`` with stored requests and responses.
* ``schoolmate`` contains settings for proper database interaction.
* ``utils`` are the core of this testing framework.
* ``config.json`` and ``pytest.ini`` contain framework's settings.
* ``prepare_db.py`` is used to clear database and fill it with predefined test
  data.
* ``update_apps.sh`` is used to update ``apps.py`` and ``models.py`` of each
  application from Schoolmate repository.

Requirements
============

* Python 3.8 or higher
* Packages listed in ``requirements.txt``

How to use
==========

1. Clone ``schoolmate-test`` repository:
   ::
     git clone https://github.com/kolyat/schoolmate-test.git
     cd schoolmate-test
2. Create and activate
   `virtual environment <https://docs.python-guide.org/dev/virtualenvs/>`_:
   ::
     virtualenv -p /usr/bin/python3.8 venv
     source venv/bin/activate
3. Install requirements:
   ::
     pip install -r requirements.txt
4. Set up ``schoolmate/settings.py``, ``config.json``, ``pytest.ini``.
5. Run ``update_apps.sh``.
6. Run ``pytest`` (``prepare_db.py`` is launched automatically).
