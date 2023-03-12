from typing import Union

from starlette import status
from starlette.responses import JSONResponse

from controller import MetricControllerInterface
from service import MetricServiceInterface
from model import Metric


class MetricController(MetricControllerInterface):
    service: MetricServiceInterface

    def __init__(self, service: MetricServiceInterface):
        self.service = service

    def add_metric(self, metric: Metric) -> JSONResponse:
        self.service.add_metric(metric)
        return JSONResponse(content=metric.dict(), status_code=status.HTTP_201_CREATED)

    def get_last_metric(self) -> JSONResponse:
        metric = self.service.get_last_metric()
        content = {} if metric is None else metric.dict()
        return JSONResponse(content=content, status_code=status.HTTP_200_OK)
