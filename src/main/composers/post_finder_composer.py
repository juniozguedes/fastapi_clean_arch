from src.infra.database.repositories.posts_repository import PostsRepository
from src.data.use_cases.post_finder import PostFinder
from src.presentation.controllers.post_finder_controller import PostFinderController


def post_creation_composer():
    repository = PostsRepository()
    use_case = PostFinder(repository)
    controller = PostFinderController(use_case)

    return controller.handle
