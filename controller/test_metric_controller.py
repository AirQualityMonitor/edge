from starlette import status

from controller import MetricController
from service import MetricServiceInterface
from model import Metric

METRIC = Metric(name="RH", unit="%", value=65.34)
JSON_METRIC = b'{"name":"RH","unit":"%","value":65.34}'


def test_add_metric(mocker):
    service: MetricServiceInterface = mocker.Mock()
    service.add_metric.return_value = ""
    spy = mocker.spy(service, "add_metric")
    controller = MetricController(service)
    response = controller.add_metric(METRIC)
    assert response.status_code == status.HTTP_201_CREATED
    assert response.body == JSON_METRIC
    assert spy.call_count == 1


def test_get_empty_metric(mocker):
    service: MetricServiceInterface = mocker.Mock()
    service.get_last_metric.return_value = None
    controller = MetricController(service)
    response = controller.get_last_metric()
    assert response.status_code == status.HTTP_200_OK
    assert response.body == b"{}"


def test_get_last_metric(mocker):
    service: MetricServiceInterface = mocker.Mock()
    service.get_last_metric.return_value = METRIC
    controller = MetricController(service)
    response = controller.get_last_metric()
    assert response.status_code == status.HTTP_200_OK
    assert response.body == JSON_METRIC
