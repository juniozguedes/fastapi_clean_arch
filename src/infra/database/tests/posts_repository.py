from typing import List
from src.domain.models.posts import Posts


class PostsRepositorySpy:
    def __init__(self) -> None:
        self.insert_post_attributes = {}
        self.select_post_attributes = {}

    def insert_post(self, title: str, content: str) -> None:
        self.insert_post_attributes["title"] = title
        self.insert_post_attributes["content"] = content

    def select_post(self, title: str) -> List[Posts]:
        self.select_post_attributes["title"] = title
        return [Posts(1, "title", "content"), Posts(2, "title", "content")]
