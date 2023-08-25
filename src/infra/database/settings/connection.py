import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# Set environment variables
os.environ[
    "SQLALCHEMY_DATABASE_URI"
] = "mysql+pymysql://root:mypassword@localhost:3306/flask_database"


class DatabaseHandler:
    def __init__(self) -> None:
        self.__connection_string = os.getenv("SQLALCHEMY_DATABASE_URI")
        self.__engine = self.__create_database_engine()
        self.session = None

    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine

    def get_engine(self):
        return self.__engine

    def __enter__(self):
        session_make = sessionmaker(bind=self.__engine)
        self.session = session_make()
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
