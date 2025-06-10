FROM python:3.12.3-slim AS builder

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install --no-cache-dir "poetry==1.8.3"

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false \
    && poetry install --no-root --only main

FROM python:3.12.3-slim AS final

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH="/src:$PYTHONPATH"

WORKDIR /app

RUN apt-get update && apt-get install -y netcat-traditional curl

COPY --from=builder /usr/local/lib/python3.12 /usr/local/lib/python3.12
COPY --from=builder /usr/local/bin /usr/local/bin
COPY --from=builder /usr/local/include /usr/local/include

COPY . .

RUN chmod +x ./entrypoints/*.sh

ENTRYPOINT ["sh", "./entrypoints/file-app-entrypoint.sh"]