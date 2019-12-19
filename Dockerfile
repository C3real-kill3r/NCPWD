# pull official base image
FROM python:3.8.0-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apk update && \
    apk add --virtual build-deps gcc python-dev musl-dev && \
    apk add postgresql-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./setup.py /usr/src/app/setup.py
RUN python3 setup.py install

# copy project
COPY . /usr/src/app/