from abc import ABC, abstractmethod
from typing import Dict


class PostCreation(ABC):
    @abstractmethod
    def create(self, title: str, content: str) -> Dict:
        pass
