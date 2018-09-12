FROM python:3.6.2

WORKDIR /usr/app

COPY . .

RUN pip install -r requirements/dev.txt

RUN apt-get update && apt-get install -y supervisor

EXPOSE 8000

CMD []
