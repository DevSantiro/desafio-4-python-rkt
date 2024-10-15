from flask import request as FlaskRequest
from typing import Dict, List
from src.drivers.interfaces.driver_handler_interface import (
    DriverHandlerInterface
)
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError


class Calculator4:
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler

    def calculate(self, request: FlaskRequest) -> Dict:  # type: ignore
        body = request.json
        input_data = self.__validate_body(body)

        mean = self.__driver_handler.mean(input_data)

        return self.__format_response(mean=mean)

    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise HttpUnprocessableEntityError("body mal formatado!")

        input_data = body["numbers"]
        return input_data

    def __format_response(self, mean: float) -> Dict:
        return {
            "data": {
                "Calculator": 4,
                "value": mean,
                "Success": True,
            }
        }
