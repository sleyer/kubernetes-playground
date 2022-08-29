# syntax=docker/dockerfile:1
FROM python:3.10-slim-buster

COPY ./app/. .

CMD [ "python3", "webserver.py" ]