from src.errors.http_bad_request import HttpBadRequestError
from .calculator_4 import Calculator4
from typing import Dict, List
from pytest import raises


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

class MockDriverHandler:
    def mean(self, number: List[float]) -> float:
        import numpy
        return numpy.mean(number)

def test_calculate():
    mock_request = MockRequest({"numbers": [10,10,10,10]})
    calculator_4 = Calculator4(MockDriverHandler())

    response = calculator_4.calculate(mock_request)

    assert response == {
        'data': {
            'Calculator': 4,
            'value':      10,
            'Success':    True,
        }
    }

def test_calculate_invalid_body():
    mock_request = MockRequest({"number": [10, 10 , 10]})
    calculator_4 = Calculator4(MockDriverHandler())

    with raises(Exception) as excinfo:
        calculator_4.calculate(mock_request)

    assert str(excinfo.value) == "body mal formatado!"
