FROM python:3
LABEL maintainer="Adam Frank afrank@mozilla.com"

WORKDIR /app

COPY setup.py /app
COPY googledirectory /app/googledirectory

RUN python setup.py build install
