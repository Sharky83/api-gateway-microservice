# Bonus: Dockerfile for containerization
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Set PYTHONPATH for module discovery
ENV PYTHONPATH=/app
# Default command runs the API Gateway
CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "app.api_gateway:app", "--bind", "0.0.0.0:3001"]

# To run tests, use:
# docker compose run --rm api-gateway pytest tests/
