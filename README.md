# API Gateway Microservice

This is a production-ready FastAPI-based API Gateway microservice for routing, rate limiting, monitoring, and proxying requests to backend microservices.

## Features
- Centralised routing and proxy logic
- Rate limiting (via external microservice)
- Monitoring and logging
- Robust error handling
- Unit and integration tests
- Configuration via `.env` file

## Configuration

All sensitive and environment-specific settings are managed via a `.env` file. Example:

```
SERVICE1_URL=http://localhost:8001
SERVICE2_URL=http://localhost:8002
```

These are loaded automatically by the gateway using `python-dotenv`.

## Usage

### Local Development

Install dependencies:
```
pip install -r requirements.txt
```

Run the gateway:
```
uvicorn app.api_gateway:app --reload --port 3001
```

### Docker

Build and run with Docker Compose:
```
docker compose up --build
```

## Testing

Run all tests:
```
pytest tests/
```
Or in Docker:
```
docker compose run --rm api-gateway pytest tests/
```

## Microservice Architecture

- **API Gateway:** Proxies requests, enforces rate limiting, and logs/monitors traffic.
- **Rate Limiting Service:** (external) Handles request quotas and usage tracking.
- **Authentication Service:** (external) Issues and validates JWTs or other tokens.
- **Backend Services:** Actual business logic, accessed via URLs in `.env`.

## Security

- Do not store secrets in source code. Use `.env` and environment variables.
- For production, run behind HTTPS (e.g., with Nginx or Traefik).

## Extending

- Add more backend services by updating `.env` and `config.py`.
- Integrate with monitoring tools (Prometheus, Grafana, etc.)

## Licence
MIT
