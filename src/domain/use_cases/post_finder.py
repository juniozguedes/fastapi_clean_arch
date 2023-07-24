from abc import ABC, abstractmethod
from typing import Dict


class PostFinder(ABC):
    @abstractmethod
    def find(self, title: str) -> Dict:
        pass
