# Quick Start

Make sure you've read [What is Pinax?](what_is_ncpwd.md) to get a conceptual overview of NCPWD.

## Setup

Follow these instructions to start working locally on the project:

- Download & clone this repo:
```
https://github.com/C3real-kill3r/NCPWD.git
```

We strongly recommend running NCPWD in a virtual environment:

- Install python version specified on `runtime.txt`
  and run to setup virtual environment:

```shell
cd NCPWD
pipenv --three
make venv
```
- and install dependencies:

```bash
make install
```

- Migrate database:

```bash
python manage.py migrate
```

- Create django admin super user:

```bash
python manage.py createsuperuser
```

Once we have made the first time setup,
we can start everything up running:

```bash
make run
```
To build & run Docker
```
 docker-compose up
 ```