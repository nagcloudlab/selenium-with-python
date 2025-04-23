import pytest
from pathlib import Path
from tempfile import TemporaryDirectory
import cards


# function
# class
# module
# package
# session


@pytest.fixture(scope="session")
def db():
    with TemporaryDirectory() as db_dir:
        db_path = Path(db_dir)
        _db = cards.CardsDB(db_path)

        yield _db

        _db.close()



@pytest.fixture(scope="function")
def cards_db(db):
    db.delete_all()
    return db