from src.infra.database.settings.connection import DatabaseHandler
from src.infra.database.entities.posts import Posts as PostsEntity


class PostsRepository:
    @classmethod
    def insert_post(cls, title: str, content: str) -> None:
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

    @classmethod
    def select_post(cls, title: str) -> any:
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
