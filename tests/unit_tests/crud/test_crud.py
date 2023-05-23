import pytest
from domain import crud
from fastapi import HTTPException
DB_STUB = None
from db import models


def test_get_existing_student(mock_existing_user):
    result = crud.get_student(DB_STUB, 1)
    assert result['id'] == 1


def test_get_non_existing_student(mock_non_existing_user):
    with pytest.raises(HTTPException) as exc:
        crud.get_student(DB_STUB, 1)
    assert isinstance(exc.value, HTTPException)
    assert exc.value.status_code == 404
    assert exc.value.detail == "User not found"


def test_get_all_students(mock_students_list):
    result = crud.get_students(DB_STUB, 1)
    assert isinstance(result, list)


def test_create_student_successful(mock_student_created):
    student = models.Student(email='mail', name='name', surname='surname')
    result = crud.create_student(DB_STUB, student=student)
    assert isinstance(result, models.Student)


def test_create_student_unsuccessful(mock_student_not_created):
    student = models.Student(email='mail', name='name', surname='surname')
    with pytest.raises(HTTPException) as exc:
        crud.create_student(DB_STUB, student=student)
    assert isinstance(exc.value, HTTPException)
    assert exc.value.status_code == 400
    assert exc.value.detail == "Email already registered"


def test_update_student_successful(mock_student_updated):
    student = models.Student(email='mail', name='name', surname='surname')
    result = crud.update_student(DB_STUB, student_id=1, student=student)
    assert isinstance(result, models.Student)


def test_update_student_unsuccessful(mock_student_not_updated):
    student = models.Student(email='mail', name='name', surname='surname')
    with pytest.raises(HTTPException) as exc:
        crud.update_student(DB_STUB, student_id=1, student=student)
    assert isinstance(exc.value, HTTPException)
    assert exc.value.status_code == 404
    assert exc.value.detail == "Student not found"


def test_delete_student_successful(mock_student_deleted):
    result = crud.delete_student(DB_STUB, student_id=1)
    assert result == {"Message": f"Successfully deleted student with id: 1"}


def test_delete_student_unsuccessful(mock_student_not_deleted):
    with pytest.raises(HTTPException) as exc:
        crud.delete_student(DB_STUB, student_id=1)
    assert isinstance(exc.value, HTTPException)
    assert exc.value.status_code == 404
    assert exc.value.detail == "Student not found"

