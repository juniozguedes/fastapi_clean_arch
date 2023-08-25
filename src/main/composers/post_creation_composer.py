from src.infra.database.repositories.posts_repository import PostsRepository
from src.data.use_cases.post_creation import PostCreation
from src.presentation.controllers.post_creation_controller import PostCreationController


def post_creation_composer():
    repository = PostsRepository()
    use_case = PostCreation(repository)
    controller = PostCreationController(use_case)

    return controller.handle
