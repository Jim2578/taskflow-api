from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def root_endpooint():
    return {
        "message": "allo le monde",
        "status": "ok",
        "version": "3.1.0"
    }

@app.get("/user")
def root_endpooint():
    return {
        "id": 1,
        "name": "Jim",
        "class": "LIT-B3"
    }

def hello():
    print("hello")