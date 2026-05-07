from fastapi import FastAPI
import os
app = FastAPI()

@app.get("/end")
def root_endpooint():
    return {
        "message": "hello world",
        "status": "ok"
    }