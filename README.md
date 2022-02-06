# Test Task

News app task for DevelopsToday

## Table of Contents

* [Setup](#setup)
* [Postman documentation](#documentation)
* [Deployment link](#deployment-link)
* [Linting & Formatting & Typing](#linting-and-formatting-and-typing)

## Setup

### Docker

Install docker and docker-compose
```bash
docker-compose up --build
```

### Without docker

Install and create virtual environment

```bash
python3 -m venv env
```

Activate

```bash
. env/bin/activate
```

Use package manager to install requirements

```bash
pip3 install -r req.txt
```

Create .env and .db.env files.
[Example](.env.example) provided below

Provide migrations

```bash
python3 manage.py migrate
```

Run
```bash
python3 manage.py runserver
```

## Documentation

* Link to the [docs](https://documenter.getpostman.com/view/17936403/UVeGrRag)
* Link to the [collection](https://www.postman.com/collections/a688631a8e9f4c5650de)

## Deployment link
Deployed via Google Cloud Platform

http://34.141.56.231/

## Linting and Formatting and Typing

Formatting completed with black
```bash
black .
```

Linting completed with flake8
```bash
flake8 --ignore E501 .
```

Typing completed with pyright
```bash
pyright .
```

