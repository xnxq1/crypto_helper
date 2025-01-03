FROM python:3.12-alpine3.17

WORKDIR /src


RUN apk add --no-cache gcc musl-dev make
RUN pip install poetry

COPY pyproject.toml \
     poetry.lock \
     ./
RUN poetry config virtualenvs.create false

RUN poetry install --no-root --no-interaction

COPY ./ /src