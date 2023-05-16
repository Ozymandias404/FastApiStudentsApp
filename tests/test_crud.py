import pytest
from domain import crud
from fastapi import HTTPException
DB_STUB = None


def test_get_existing_student(mock_existing_user):
    result = crud.get_student(DB_STUB, 1)
    assert result['id'] == 1


def test_get_non_existing_student(mock_non_existing_user):
    with pytest.raises(HTTPException) as exc:
        crud.get_student(DB_STUB, 1)
    assert isinstance(exc.value, HTTPException)
    assert exc.value.status_code == 404
    assert exc.value.detail == "User not found"

