from fastapi import FastAPI
from prometheus_client import Counter
from starlette_exporter import PrometheusMiddleware, handle_metrics

app = FastAPI()
app.add_middleware(PrometheusMiddleware)
app.add_route("/metrics", handle_metrics)

TEST_COUNTER = Counter("test_counter", "A counter to test that the prometheus integration works")


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/count")
async def count(n: int = 1):
    TEST_COUNTER.inc(n)
    return {"message": f"Increased counter by {n}"}


@app.get("/isHealthy")
async def is_healthy():
    return "OK"


@app.get("/isReady")
async def is_ready():
    return "OK"
