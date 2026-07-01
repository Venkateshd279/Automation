from fastapi import FastAPI
from pydantic import BaseModel

#build fastapi to print hello world
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}