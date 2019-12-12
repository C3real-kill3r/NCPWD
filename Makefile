

venv:
	${INFO} "Creating Python Virtual Environment"
	@ pipenv shell
	${SUCCESS} "Virtual Environment has be created successfully, run 'source env/bin/activate' to activate it"

install:
	${INFO} "Upgrading pip version"
	@ pip install --upgrade pip
	@ echo ''
	${INFO} "Installing Python Dependencies"
	@ pipenv install
	${SUCCESS} "Done.🎉 🤓 🎊"

run:
	@ python manage.py runserver

GREEN  := $(shell tput -Txterm setaf 2)
YELLOW := $(shell tput -Txterm setaf 3)
WHITE  := $(shell tput -Txterm setaf 7)
NC := "\e[0m"
RESET  := $(shell tput -Txterm sgr0)
# Shell Functions
INFO := @bash -c 'printf $(YELLOW); echo "~ $$1"; printf $(NC)' SOME_VALUE
SUCCESS := @bash -c 'printf $(GREEN); echo "~ $$1"; printf $(NC)' SOME_VALUE