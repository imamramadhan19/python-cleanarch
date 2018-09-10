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

# FROM python:3.6-alpine as base

# FROM base as builder

# RUN mkdir /install 
# WORKDIR /install
# COPY requirements.txt /requirements.txt
# COPY requirements /requirements

# RUN apk update \
#     && apk add python3 postgresql-libs \
#     && apk add --update --no-cache --virtual .build-deps alpine-sdk python3-dev musl-dev postgresql-dev libffi-dev \
#     && pip install -U setuptools pip \
#     && pip install --install-option="--prefix=/install" -r /requirements.txt \
#     && apk --purge del .build-deps

# FROM base

# EXPOSE 8000

# COPY --from=builder . .
# COPY src /usr/app
# WORKDIR /usr/app


# CMD []
