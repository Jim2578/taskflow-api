from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def root_endpoint():
    return {
        "message": "allo le monde",
        "status": "ok",
        "version": "3.1.0"
    }

@app.get("/user")
def user_endpoint():
    return {
        "id": 1,
        "name": "Jim",
        "class": "LIT-B3"
    }

def hello():
    print("hello")