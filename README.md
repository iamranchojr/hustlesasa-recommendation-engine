### Hustlesasa Recommendation Engine
A simple recommendation engine built using FastAPI that provides product recommendations based on user order history or product popularity.

### Features
Recommend products based on:

- User's order history (if authenticated).
- Popular products (if unauthenticated).
- API endpoints exposed via FastAPI.

## Live Deployment

A ready-to-test version of the recommendation engine has been deployed to Heroku and is accessible at the following URL:

[https://hustlesasa-recommend-engine-699e1f9da4f3.herokuapp.com/docs](https://hustlesasa-recommend-engine-699e1f9da4f3.herokuapp.com/docs)

### Requirements
Docker and Docker Compose installed.
Python 3.12+ (if running locally without Docker).


### Project Setup
Using Docker (Recommended)

1. Clone this repository:

```bash
git clone https://github.com/iamranchojr/hustlesasa-recommendation-engine
cd recommendation-engine
```

2. Build and run the Docker container:

```bash
docker-compose up --build -d
```

3. Access the API at:

- Base URL: http://localhost:7777
- Documentation: http://localhost:7777/docs

### API Endpoints
`/api/v1/recommend-products`
- GET: Fetches product recommendations.
- Query Parameters
`user_id` (optional): Fetch recommendations for a specific user if authenticated.

### Example Request
```bash
curl -X GET "http://localhost:7777/api/v1/recommend-products?user_id=1"
```

### Example Response
```json
[
  {
    "id": 48,
    "name": "Product 48",
    "description": "Premium acoustic guitar strings.",
    "price": 19.99,
    "category": "Instruments",
    "quantity": 20,
    "is_active": true,
    "popularity_score": 85
  },
  ...
]
```

### Project Structure
```graphql
recommendation-engine/
├── app/
│   ├── main.py                # FastAPI entry point
│   ├── config.py              # Configuration settings
│   ├── router.py              # FastAPI routes
│   ├── models/                # Pydantic models for data
│   ├── repositories/          # Repository layer for data access
│   ├── services/              # Business logic for recommendations
│   ├── data/                  # Sample JSON data for testing
│   └── tests/                 # Unit tests for the application
├── Dockerfile                 # Docker build file
├── docker-compose.yml         # Docker Compose setup
├── requirements.txt           # Python dependencies
├── runtime.txt                # Python runtime version for Heroku
├── Procfile                   # Heroku entry point
├── .gitignore                 # Git ignored files
├── README.md                  # Project documentation   
```

### Testing
Run tests using:

```bash
pytest
```

## Design Document

For a detailed overview of the architecture, algorithms, technologies, and system design, refer to the complete design document hosted on Notion:

[Architectural Document for Hustlesasa Recommendation Engine](https://www.notion.so/Architectural-Document-for-Hustlesasa-Recommendation-Engine-14a87b447495803e8555e506dc891ed0?pvs=4)
