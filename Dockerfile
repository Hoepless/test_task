# pull official base image
FROM python:alpine

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0

# install psycopg2
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev \
    && pip install psycopg2 \
    && apk del build-deps

# install dependencies
COPY ./req.txt .
RUN pip install -r req.txt

# copy project
COPY . .

# run gunicorn
CMD gunicorn news.wsgi:application --log-level INFO --bind 0.0.0.0:$PORT