from fastapi import FastAPI, Request
from src.error import DomainException
from fastapi.responses import JSONResponse

app = FastAPI()

@app.exception_handler(DomainException)
async def domain_exception_handler(request: Request, exc: DomainException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )

@app.get("/")
def get_root():
    return {
        "ok": True
    }