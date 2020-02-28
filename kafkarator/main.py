from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/isHealthy")
async def is_healthy():
    return "OK"


@app.get("/isReady")
async def is_ready():
    return "OK"
