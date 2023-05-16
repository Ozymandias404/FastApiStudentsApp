import pytest
from controllers import repositories
from tests.mocks import mock_get_non_existing_student, mock_get_existing_student


@pytest.fixture
def mock_existing_user(monkeypatch):
    monkeypatch.setattr(repositories, "get_first_student_with_id", mock_get_existing_student)


@pytest.fixture
def mock_non_existing_user(monkeypatch):
    monkeypatch.setattr(repositories, "get_first_student_with_id", mock_get_non_existing_student)
