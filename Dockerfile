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
COPY hypercorn_config.py /app/hypercorn_config.py

CMD /app/.venv/bin/hypercorn --config python:/app/hypercorn_config.py kafkarator.main:app
