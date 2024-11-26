from fastapi import FastAPI

from app.router import router

app = FastAPI(title='Hustlesasa Recommendation Engine')


@app.get('/')
async def root():
    return {
        'message': 'Welcome to Hustlesasa Recommendation Engine v1.0'
    }


app.include_router(router, prefix='/api/v1')
