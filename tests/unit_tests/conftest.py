import pytest
from controllers import repositories
from tests.unit_tests import mocks


@pytest.fixture
def mock_existing_user(monkeypatch):
    monkeypatch.setattr(repositories, "get_first_student_with_id", mocks.mock_get_existing_student)


@pytest.fixture
def mock_non_existing_user(monkeypatch):
    monkeypatch.setattr(repositories, "get_first_student_with_id", mocks.mock_get_non_existing_student)


@pytest.fixture
def mock_students_list(monkeypatch):
    monkeypatch.setattr(repositories, "get_all_students", mocks.mock_get_all_students)


@pytest.fixture
def mock_student_created(monkeypatch):
    monkeypatch.setattr(repositories, "get_first_student_with_email", mocks.mock_get_non_existing_student)
    monkeypatch.setattr(repositories, "create_student_with_data", mocks.mock_create_student_with_data)


@pytest.fixture
def mock_student_not_created(monkeypatch):
    monkeypatch.setattr(repositories, "get_first_student_with_email", mocks.mock_get_first_student_with_mail)
    monkeypatch.setattr(repositories, "create_student_with_data", mocks.mock_create_student_with_data)


@pytest.fixture
def mock_student_updated(monkeypatch):
    monkeypatch.setattr(repositories, "get_first_student_with_id", mocks.mock_get_existing_student)
    monkeypatch.setattr(repositories, "update_student_with_id", mocks.mock_create_student_with_data)


@pytest.fixture
def mock_student_not_updated(monkeypatch):
    monkeypatch.setattr(repositories, "get_first_student_with_id", mocks.mock_get_non_existing_student)
    monkeypatch.setattr(repositories, "update_student_with_id", mocks.mock_create_student_with_data)


@pytest.fixture
def mock_student_deleted(monkeypatch):
    monkeypatch.setattr(repositories, "get_first_student_with_id", mocks.mock_get_existing_student)
    monkeypatch.setattr(repositories, "delete_student_with_id", mocks.mock_delete_student)


@pytest.fixture
def mock_student_not_deleted(monkeypatch):
    monkeypatch.setattr(repositories, "get_first_student_with_id", mocks.mock_get_non_existing_student)
    monkeypatch.setattr(repositories, "delete_student_with_id", mocks.mock_delete_student)