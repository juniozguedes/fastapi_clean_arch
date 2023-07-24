from ...infra.database.tests.posts_repository import PostsRepositorySpy
from .post_creation import PostCreation


def test_creation():
    title = "title"
    content = "content"

    repo = PostsRepositorySpy()
    post_creation = PostCreation(repo)

    response = post_creation.create(title, content)

    assert repo.insert_post_attributes["title"] == title
    assert response["type"] == "Posts"
    assert response["count"] == "1"


def test_creation_title_error():
    title = "Title123"
    content = "content1234"
    repo = PostsRepositorySpy()
    post_creation = PostCreation(repo)

    try:
        post_creation.create(title, content)
        assert False
    except Exception as exception:
        assert str(exception) == "Invalid Name contains alphanumerics"
