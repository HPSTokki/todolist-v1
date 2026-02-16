from fastapi import FastAPI
from src.routes import user_route 

app = FastAPI()

app.include_router(user_route.router)

@app.get('/')
async def get_root():
    return {
        "message": True
    }