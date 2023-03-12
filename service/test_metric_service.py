from model import Metric
from service import MetricService
from registery import InMemoryTSDB


def test_init():
    service = MetricService(InMemoryTSDB())
    assert service.get_last_metric() is None


def test_get_first():
    service = MetricService(InMemoryTSDB())
    metric = Metric(name="RH", unit="%", value=65.34)
    service.add_metric(metric)
    assert service.get_last_metric() == metric


def test_second_first():
    service = MetricService(InMemoryTSDB())
    first_metric = Metric(name="RH", unit="%", value=65.34)
    second_metric = Metric(name="Temp", unit="C", value=65.34)
    service.add_metric(first_metric)
    service.add_metric(second_metric)
    assert service.get_last_metric() == second_metric
