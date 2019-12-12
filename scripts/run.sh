RED='\033[0;31m'

if [ "$(flake8 . ; echo $? | grep 1)" ]
then
    tput setaf 5; echo "Flake8 Linter Warning(s):"
    echo -e "${RED} $(flake8 .)\n"; tput  sgr0;
    python manage.py runserver
else
     python manage.py runserver
fi
