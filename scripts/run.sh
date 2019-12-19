#!/bin/sh

RED='\033[0;31m'
python manage.py migrate

if [ "$(flake8 . ; echo $? | grep 1)" ]
then
    tput setaf 5; echo "Flake8 Linter Warning(s):"
    echo -e "${RED} $(flake8 .)\n"; tput  sgr0;
    tput setaf 5; echo "Mypy: Static Checker Warning(s):"
    echo -e "${RED} $(mypy .)\n"; tput  sgr0;

    python manage.py runserver

elif [ "$(flake8 . ; echo $? | grep 1)" ]
then
    tput setaf 5; echo "Flake8 Linter Warning(s):"
    echo -e "${RED} $(flake8 .)\n"; tput  sgr0;
     python manage.py runserver

elif [ "$(mypy . ; echo $? | grep 1)" ]
then
    tput setaf 5; echo "Mypy: Static Checker Warning(s):"
    echo -e "${RED} $(mypy .)\n"; tput  sgr0;
    python manage.py runserver
else
    python manage.py runserver
fi