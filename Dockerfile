FROM python:3.10.4-alpine3.15

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /api
WORKDIR /api
COPY ./api /api

RUN adduser -D recipr
USER recipr