from fastapi import FastAPI
from src.routes import user_routes

app = FastAPI()

app.include_router(user_routes.router)

@app.get("/")
async def get_root():
    return {
        "ok": True
    }