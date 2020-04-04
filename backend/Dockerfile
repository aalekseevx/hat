###########
# BUILDER #
###########

# pull official base image
FROM python:3.7.7-alpine as builder

# System deps:
RUN apk --no-cache add \
    build-base \
    gcc \
    bash \
    linux-headers \
    openssl-dev \
#    libressl-dev \
    libffi-dev

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.0.2 \
  GUNICORN_VERSION=20.0.4

# lint
RUN pip install --upgrade pip
RUN pip install flake8
COPY . /usr/src/app/
# TODO delte ignore
#RUN flake8 --ignore=E501,F401 .

# Use pip to ensure a consistent poetry version
RUN pip install poetry==${POETRY_VERSION}
# Disable virtualenvs - docker is isolated enough
RUN poetry config virtualenvs.create false

# install dependencies
COPY poetry.lock pyproject.toml ./
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels gunicorn==${GUNICORN_VERSION}
RUN poetry install --no-interaction --no-ansi $(test "$DJANGO_ENV" == production && echo "--no-dev")

#########
# FINAL #
#########

# pull official base image
FROM python:3.7.7-alpine

# create directory for the app user
RUN mkdir -p /home/app

# create the app user
RUN addgroup -S app && adduser -S app -G app

# create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/staticfiles
RUN mkdir $APP_HOME/mediafiles
WORKDIR $APP_HOME

# install dependencies
RUN apk update && apk add libpq
COPY --from=builder /usr/src/app/wheels /wheels
RUN pip install --upgrade pip
RUN pip install --no-cache /wheels/*

# Copy prebuilt libs
COPY --from=builder /usr/local /usr/local


# copy entrypoint-prod.sh
#COPY entrypoint.sh $APP_HOME

# copy project
COPY . $APP_HOME

# chown all the files to the app user
RUN chown -R app:app $APP_HOME


# change to the app user
USER app
