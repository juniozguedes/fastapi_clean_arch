from ...infra.database.tests.posts_repository import PostsRepositorySpy
from .post_finder import PostFinder


def test_find():
    title = "title"

    repo = PostsRepositorySpy()
    post_finder = PostFinder(repo)

    response = post_finder.find(title)

    assert repo.select_post_attributes["title"] == title

    assert response["type"] == "Posts"


def test_find_error_in_valid_title():
    title = "Incorrect Title 123"

    repo = PostsRepositorySpy()
    post_finder = PostFinder(repo)

    try:
        post_finder.find(title)
        assert False
    except Exception as exception:
        assert str(exception) == "Invalid Name contains alphanumerics"


def test_find_error_in_long_title():
    title = "Thisnameiswayaboveeighteencharacters"

    repo = PostsRepositorySpy()
    post_finder = PostFinder(repo)

    try:
        post_finder.find(title)
        assert False
    except Exception as exception:
        assert str(exception) == "Name is above 18 characters"


def test_find_error_post_not_found():
    class PostsRepositoryError(PostsRepositorySpy):
        def select_post(self, title: str):
            return []

    title = "NA"
    repo = PostsRepositoryError()
    post_finder = PostFinder(repo)

    try:
        post_finder.find(title)
        assert False
    except Exception as exception:
        assert str(exception) == "Post not found"
