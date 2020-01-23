FROM python:3.7-alpine

WORKDIR /app

COPY . .

RUN apk update && apk upgrade &&\
    apk add gcc git openssh-client linux-headers libc-dev
    
RUN pip install --no-cache-dir -r requirements.txt