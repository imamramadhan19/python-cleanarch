FROM python:3.6-alpine

WORKDIR /usr/app

COPY . .
RUN apk update \
    && apk add python3 postgresql-libs \
    && apk add --update --no-cache --virtual .build-deps alpine-sdk python3-dev musl-dev postgresql-dev libffi-dev \
    && pip install -U setuptools pip \
    && pip install -r requirements.txt

EXPOSE 8000

CMD []
