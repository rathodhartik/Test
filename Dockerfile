FROM python:3

WORKDIR /app

ADD . /app/

COPY requirements.txt ./

RUN pip3 install -r requirements.txt


