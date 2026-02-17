import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "src.main:app",
        port=8000,
        log_level=True,
        reload=True
    )
