from typing import Callable
from fastapi import Request as FastApiRequest
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse


def request_adapter(request: FastApiRequest, controller: Callable) -> HttpResponse:
    http_request = HttpRequest(
        headers=request.headers,
        body=request.body,
        query_params=request.query_params,
        path_params=request.path_params,
        url=str(request.url),  # Convert URL to string
    )

    http_response = controller(http_request)
    return http_response
