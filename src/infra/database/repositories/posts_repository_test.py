from .posts_repository import PostsRepository


def test_insert_post():
    mocket_title = "title1"
    mocked_content = "content1"

    posts_repository = PostsRepository()
    posts_repository.insert_post(mocket_title, mocked_content)
