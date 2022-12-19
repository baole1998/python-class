FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

RUN mkdir -p /code/db

RUN mkdir -p /code/logs

RUN mkdir -p /code/models

COPY . /code/

