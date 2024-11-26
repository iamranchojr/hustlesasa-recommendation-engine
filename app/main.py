from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware

from app.config import settings
from app.router import router

app = FastAPI(title='Hustlesasa Recommendation Engine')

cors_allowed_origins = [
    'http://localhost',
    'http://localhost:7777',
    'https://hustlesasa-recommend-engine-699e1f9da4f3.herokuapp.com',
]


# apply cors
app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_allowed_origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

if settings.SECURE_SSL_REDIRECT:
    # apply redirect to https middleware
    app.add_middleware(HTTPSRedirectMiddleware)

    app.add_middleware(
        TrustedHostMiddleware,
        allowed_hosts=[
            'hustlesasa-recommend-engine-699e1f9da4f3.herokuapp.com',
        ]
    )


@app.get('/')
async def index():
    return {
        'message': 'Welcome to Hustlesasa Recommendation Engine v1.0'
    }


app.include_router(router, prefix='/api/v1')
