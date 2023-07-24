from typing import List
from abc import ABC, abstractmethod
from src.domain.models.posts import Posts


class PostsRepositoryInterface(ABC):
    @abstractmethod
    def insert_post(self, title: str, content: str) -> None:
        pass

    @abstractmethod
    def select_post(self, title: str) -> List[Posts]:
        pass
