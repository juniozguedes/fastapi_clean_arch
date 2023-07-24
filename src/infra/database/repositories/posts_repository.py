from typing import List
from src.infra.database.settings.connection import DatabaseHandler
from src.infra.database.entities.posts import Posts as PostsEntity
from src.data.interfaces.posts_repository import PostsRepositoryInterface
from src.domain.models.posts import Posts


class PostsRepository(PostsRepositoryInterface):
    def insert_post(self, title: str, content: str) -> None:
        with DatabaseHandler() as db_session:
            try:
                post_db = PostsEntity(
                    title=title,
                    content=content,
                )
                db_session.add(post_db)
                db_session.commit()
            except Exception as exception:
                print(f"ex: {exception}")
                db_session.rollback()
                raise exception

    def select_post(self, title: str) -> List[Posts]:
        with DatabaseHandler() as db_session:
            try:
                post = (
                    db_session.query(PostsEntity)
                    .filter(PostsEntity.title == title)
                    .all()
                )
                return post
            except Exception as exception:
                print(f"ex: {exception}")
                db_session.rollback()
                raise exception
