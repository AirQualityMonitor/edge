from typing import List, Union

from model import Metric
from service import MetricServiceInterface
from registery import TSDBInterface


class MetricService(MetricServiceInterface):
    def __init__(self, tsdb: TSDBInterface):
        self.tsdb = tsdb

    def add_metric(self, metric: Metric):
        self.tsdb.add_metric(metric)

    def get_last_metric(self) -> Union[Metric, None]:
        return self.tsdb.get_last_metric()
