#!/bin/sh

REPO=https://raw.githubusercontent.com/kolyat/schoolmate/master

for app in school account news timetable diary notebook
do
  curl ${REPO}/${app}/apps.py --output ./${app}/apps.py
  curl ${REPO}/${app}/models.py --output ./${app}/models.py
#  git archive --remote=git://github.com/kolyat/schoolmate \
#              master:schoolmate/${app} apps.py models.py | tar -C ./${app} -xv
done
