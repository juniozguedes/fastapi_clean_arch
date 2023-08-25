from fastapi import APIRouter, Request

# Import adapters
from src.main.adapters.request_adapter import request_adapter

# Import composers
from src.main.composers import post_finder_composer
from src.main.composers.post_creation_composer import post_creation_composer

router = APIRouter()


@router.get("/posts")
def post_finder(request: Request):
    http_response = request_adapter(request, post_finder_composer)
    return http_response


@router.post("/posts")
def post_creation(request: Request):
    http_response = request_adapter(request, post_creation_composer)
    return http_response
