from typing import Dict, List
from src.domain.use_cases.post_finder import PostFinder as PostFinderInterface
from src.data.interfaces.posts_repository import PostsRepositoryInterface
from src.domain.models.posts import Posts
from src.errors.types import HttpBadRequestError, HttpNotFoundError

class PostFinder(PostFinderInterface):
    def __init__(self, posts_repository: PostsRepositoryInterface) -> None:
        self.__posts_repository = posts_repository

    def find(self, title: str) -> Dict:
        self.__validate_title(title)
        posts = self.__posts_repository.select_post(title)
        posts = self.__search_post(title)
        response = self.__format_response(posts)
        return response

    @classmethod
    def __validate_title(cls, title: str) -> None:
        # Validations
        if not title.isalpha():
            raise HttpBadRequestError("Invalid Name contains alphanumerics")

        if len(title) > 18:
            raise HttpBadRequestError("Name is above 18 characters")

    def __search_post(self, title: str) -> List[Posts]:
        posts = self.__posts_repository.select_post(title)
        if posts == []:
            raise HttpNotFoundError("Post not found")
        return posts

    @classmethod
    def __format_response(cls, posts: List[Posts]) -> Dict:
        attributes = []
        for post in posts:
            attributes.append({"title": post.title, "content": post.content})
        response = {"type": "Posts", "count": len(posts), "attributes": attributes}
        return response
