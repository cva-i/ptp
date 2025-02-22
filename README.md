# __P__DF __T__o __P__NG converter

## **Key Features:**

1. **Production-Grade Structure:**
- Proper FastAPI setup with dependency management
- Separate concerns (routes, models, utils)
- Pydantic validation for input parameters
- Error handling middleware

2. **OpenAPI Documentation:**
- Auto-generated docs at `/docs`
- YAML endpoint at `/openapi.yaml`
- Request/response schemas

3. **Deployment Ready:**
- Docker Compose for local development
- AWS Lambda compatible through Mangum
- Serverless Framework configuration

4. **Validation:**
- Base64 format validation
- DPI range validation (72-600)
- PDF content validation during conversion


## Development Setup

Get poetry
```bash
curl -sSL https://install.python-poetry.org | python3 -
```
Install dependencies
```sh
poetry install
```

Run locally
```bash
poetry run uvicorn app.main:app --reload
```

## Deployment


1. **local deployment:**
```bash
docker-compose up -d
```

Test conversion
```bash
curl -X POST "http://localhost:8000/convert" \
  -H "Content-Type: application/json" \
  -d '{"pdf": "'$(base64 -i input.pdf)'", "dpi": 200}'
```

2. **AWS Lambda Notes:**

```bash
npm install -g serverless
serverless deploy
```

