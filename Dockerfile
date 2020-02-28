FROM python:3.7-slim
RUN pip install poetry
WORKDIR /app
COPY pyproject.toml poetry.lock /app/
RUN poetry install --no-root --no-dev --no-interaction
COPY kafkarator /app/kafkarator/
RUN poetry install --no-dev --no-interaction

CMD hypercorn kafkarator.main:app
