# syntax=docker/dockerfile:1
FROM python:3.10-slim-buster
RUN useradd -ms /bin/bash py-webserver
USER py-webserver
WORKDIR /home/py-webserver

COPY ./app/. .

CMD [ "python3", "webserver.py" ]