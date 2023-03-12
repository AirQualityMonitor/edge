from abc import ABC, abstractmethod
from model import Metric
from typing import Union


class MetricServiceInterface(ABC):
    @abstractmethod
    def add_metric(self, metric: Metric):
        pass

    @abstractmethod
    def get_last_metric(self) -> Union[Metric, None]:
        pass
