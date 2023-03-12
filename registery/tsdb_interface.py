from abc import ABC, abstractmethod
from typing import Union

from model import Metric


class TSDBInterface(ABC):
    @abstractmethod
    def add_metric(self, metric: Metric):
        pass

    @abstractmethod
    def get_last_metric(self) -> Union[Metric, None]:
        pass
