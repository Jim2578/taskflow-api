from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def root_endpooint():
    return {
        "message": "allo le monde",
        "status": "ok",
        "version": "3.1.0"
    }

def hello():
    print("hello")