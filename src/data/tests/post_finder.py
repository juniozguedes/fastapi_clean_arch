from typing import Dict


class PostFinderSpy:
    def __init__(self) -> None:
        self.find_attributes = {}

    def find(self, title: str) -> Dict:
        self.find_attributes["title"] = title

        return {
            "type": "Posts",
            "count": 1,
            "attributes": [{"title": title, "content": "something"}],
        }
