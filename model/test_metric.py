import pytest
from pydantic import ValidationError

from model import Metric


@pytest.mark.parametrize(
    "metric_dict, message",
    [
        ({"name": "Temp", "unit": "C", "value": "hot"}, "value is not a valid float"),
        (
            {"name": " space", "unit": "C", "value": 24.3},
            "must not contain a space",
        ),
        (
            {"name": "", "unit": "C", "value": 24.3},
            "name should contain from 1 to 7 characters",
        ),
        (
            {"name": "01234567", "unit": "C", "value": 24.3},
            "name should contain from 1 to 7 characters",
        ),
        (
            {"unit": "C", "value": 24.3},
            "field required",
        ),
    ],
)
def test_metric(metric_dict, message):
    try:
        Metric(**metric_dict)
        assert False
    except ValidationError as e:
        assert e.errors()[0]["msg"] == message
