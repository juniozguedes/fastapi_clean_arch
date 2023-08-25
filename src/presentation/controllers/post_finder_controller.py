from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.use_cases.post_finder import PostFinder as PostFinderInterface


class PostFinderController(ControllerInterface):
    def __init__(self, use_case: PostFinderInterface) -> None:
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        title = http_request.query_params["title"]

        response = self.__use_case.find(title)

        return HttpResponse(status_code=200, body={"data": response})
