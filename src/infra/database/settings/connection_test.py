import pytest
from .connection import DatabaseHandler


@pytest.mark.skip(reason="Sensitive test")
def test_create_database_engine():
    db_handler = DatabaseHandler()
    engine = db_handler.get_engine()
    assert engine is not None
