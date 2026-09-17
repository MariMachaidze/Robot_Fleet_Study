from fastapi import FastAPI

app = FastAPI()

@app.get("/health")

def health_check():
    return {"status": "ok"}

@app.get("/greet/{name}")

def greet(name:str):
    return {"message": f"Hello, {name}"}
