FROM ubuntu:latest

ENV APP_COLOR="red"

RUN apt-get update && apt-get install -y python3 python3-flask

WORKDIR /app

COPY . .

ENTRYPOINT ["python3", "main.py"]
