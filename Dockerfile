FROM python:3.7-slim as build
RUN pip install poetry
WORKDIR /app
COPY pyproject.toml poetry.lock /app/
RUN poetry config virtualenvs.in-project true && poetry install --no-root --no-interaction
COPY kafkarator /app/kafkarator/
COPY tests /app/tests/
RUN poetry run prospector && poetry run pytest --cov=kafkarator
RUN poetry install --no-dev --no-interaction

FROM python:3.7-slim

COPY --from=build /app/.venv /app/.venv/
COPY --from=build /app/kafkarator /app/kafkarator/

CMD /app/.venv/bin/hypercorn --access-logfile=- --bind 0.0.0.0 --error-logfile=- --debug --log-level debug kafkarator.main:app
