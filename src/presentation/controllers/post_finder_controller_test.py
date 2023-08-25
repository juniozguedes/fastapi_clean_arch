from src.presentation.controllers.post_finder_controller import PostFinderController
from src.data.tests.post_finder import PostFinderSpy
from src.presentation.http_types.http_response import HttpResponse


class HttpRequestMock:
    def __init__(self) -> None:
        self.query_params = {"title": "ThisisTitle"}


def test_handle():
    http_request_mock = HttpRequestMock()
    use_case = PostFinderSpy()
    post_finder_controller = PostFinderController(use_case)

    response = post_finder_controller.handle(http_request_mock)
    assert isinstance(response, HttpResponse)
    assert response.status_code == 200
    assert response.body["data"] is not None
