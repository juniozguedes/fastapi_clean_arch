from src.presentation.http_types.http_response import HttpResponse
from .types import HttpNotFoundError, HttpBadRequestError

def handle_errors(error: Exception) -> HttpResponse:
    if isinstance(error, (HttpBadRequestError, HttpNotFoundError)):
        # log this!
        return HttpResponse(
            status_code=error.status_code,
            body={
                "errors":[{
                    "title": error.name,
                    "detail": error.message
                }]
            }
        )

    return HttpResponse(
        status_code=500,
        body={
            "errors":[{
                "title": "Internal Server Error",
                "detail": str(error)
            }]
        }
    )
