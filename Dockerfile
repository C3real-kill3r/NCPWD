# pull official base image
FROM python:3.7.5-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PORT 8000
ENV HOST 0.0.0.0
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apk update && \
    apk add --virtual build-deps gcc python-dev musl-dev && \
    apk add postgresql-dev

# download the cloudsql proxy
RUN wget https://dl.google.com/cloudsql/cloud_sql_proxy.linux.amd64 -O /usr/src/app/cloud_sql_proxy
# make cloudsql proxy executable
RUN chmod +x /usr/src/app/cloud_sql_proxy

# install dependencies
RUN pip install --upgrade pip
COPY ./setup.py /usr/src/app/setup.py
RUN python3 setup.py install

# copy project
COPY . /usr/src/app/

#EXPOSE
EXPOSE 8000

CMD ["gunicorn", "--bind", ":8080", "--workers", "3", "NCPWD.wsgi:application"]
