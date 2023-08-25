from src.presentation.interfaces.controller_interface import ControllerInterface
from src.domain.use_cases.post_creation import PostCreation as PostCreationInterface
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse


class PostCreationController(ControllerInterface):
    def __init__(self, use_case: PostCreationInterface) -> None:
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        title = http_request.body["title"]
        content = http_request.body["content"]

        response = self.__use_case.create(title, content)

        return HttpResponse(status_code=200, body={"data": response})
