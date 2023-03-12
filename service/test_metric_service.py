from model import Metric
from service import MetricService


def test_init():
    service = MetricService()
    assert service.get_last_metric() is None


def test_get_first():
    service = MetricService()
    metric = Metric(name="RH", unit="%", value=65.34)
    service.add_metric(metric)
    assert service.get_last_metric() == metric


def test_second_first():
    service = MetricService()
    first_metric = Metric(name="RH", unit="%", value=65.34)
    second_metric = Metric(name="Temp", unit="C", value=65.34)
    service.add_metric(first_metric)
    service.add_metric(second_metric)
    assert service.get_last_metric() == second_metric
