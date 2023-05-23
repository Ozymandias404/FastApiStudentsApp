import pytest
from controllers.repositories import clear_data
from db.database import engine
from sqlalchemy.orm import Session


@pytest.fixture(autouse=True)
def run_around_tests():
    yield
    clear_data(Session(engine))