from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def root_endpooint():
    return {
        "message": "allo le monde",
        "status": "ok",
        "version": "3.0.0"
    }

def hello():
    print("hello")