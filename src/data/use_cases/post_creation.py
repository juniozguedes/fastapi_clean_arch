from typing import Dict
from src.domain.use_cases.post_creation import PostCreation as PostCreationInterface
from src.data.interfaces.posts_repository import PostsRepositoryInterface
from src.errors.types import HttpBadRequestError


class PostCreation(PostCreationInterface):
    def __init__(self, posts_repository: PostsRepositoryInterface) -> None:
        self.__posts_repository = posts_repository

    def create(self, title: str, content: str):
        self.__validate_title(title)
        self.__register_post_information(title, content)
        response = self.__format_response(title, content)
        return response

    @classmethod
    def __validate_title(cls, title: str) -> None:
        # Validations
        if not title.isalpha():
            raise HttpBadRequestError("Invalid Name contains alphanumerics")

        if len(title) > 18:
            raise HttpBadRequestError("Name is above 18 characters")

    def __register_post_information(self, title: str, content: str) -> None:
        self.__posts_repository.insert_post(title, content)

    @classmethod
    def __format_response(cls, title: str, content: str) -> Dict:
        response = {
            "type": "Posts",
            "count": "1",
            "attributes": {"title": title, "content": content},
        }
        return response
