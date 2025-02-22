FROM python:3.13-slim-bookworm

RUN apt-get update && apt-get install -y \
    poppler-utils \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
ENV PYTHONPATH=/app/src

RUN pip install poetry

COPY pyproject.toml poetry.lock* ./

RUN poetry config virtualenvs.create false

RUN poetry install --only main --no-interaction --no-root

COPY src/ src/

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
