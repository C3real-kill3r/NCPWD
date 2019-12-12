FROM python:3.7-slim

RUN python -m pip install --upgrade pip

COPY setup.py setup.py
RUN python3 setup.py install

COPY . .