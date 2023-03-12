from typing import Union

from fastapi import FastAPI, status

from model import Metric
from service import MetricService
from controller import MetricController

app = FastAPI(title="Edge - Air Quality Monitor")
service = MetricService()
controller = MetricController(service)


@app.post("/metric")
async def add_metric(metric: Metric):
    return controller.add_metric(metric)


@app.get("/metric", response_model=Metric)
async def get_last_metric():
    return controller.get_last_metric()
