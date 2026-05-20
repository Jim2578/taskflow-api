from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def root_endpooint():
    return {
        "message": "hello world",
        "status": "ok"
    }

@app.get("/update")
def root_endpooint():
    return {
        "message": "Application Up-to-date",
        "versions": "2026.05.20"
    }

def hello():
    print("hello")