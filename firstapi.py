import fastapi 
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI(
    title="My First API",
    description="This is my first API built with FastAPI",
    version="1.0.0",
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    uvicorn.run("firstapi:app", host="127.0.0.1", port=8000, log_level="info", reload=True)