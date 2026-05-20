from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def root_endpooint():
    return {
        "message": "allo le monde",
        "status": "ok"
    }

def hello():
    print("hello")