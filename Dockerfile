FROM python:3.8.1-alpine
RUN apk update && \
    apk add --virtual build-deps gcc python-dev musl-dev && \
    apk add netcat-openbsd
