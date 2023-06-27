FROM python:3.10-alpine3.17

ENV PIP_NO_CACHE_DIR=yes

ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /code

COPY . .
RUN pip install pipenv
RUN pipenv install --ignore-pipfile --system
CMD ["python","main.py"]
