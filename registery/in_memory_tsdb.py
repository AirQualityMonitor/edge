from typing import List, Union

from model import Metric
from registery import TSDBInterface


class InMemoryTSDB(TSDBInterface):
    def __init__(self):
        self.metrics: List[Metric] = []

    def add_metric(self, metric: Metric):
        self.metrics.append(metric)

    def get_last_metric(self) -> Union[Metric, None]:
        return self.metrics[-1] if len(self.metrics) else None
