from typing import Dict
from .http_bad_request import HttpBadRequestError
from .http_unprocessable_entity import HttpUnprocessableEntityError

def handle_errors(error: Exception) -> Dict:
    if isinstance(error, (HttpUnprocessableEntityError, HttpBadRequestError)):
        return {
            "status_code": error.status_code,
            "body": {
                "erros": [
                    {
                        "title":  error.name,
                        "detail": error.message
                    }
                ]
            }
        }
    
    return {
        "status_code": 500,
        "body": {
            "erros": [
                {
                    "title":  "Server Error",
                    "detail": str(error)
                }
            ]
        }
    }