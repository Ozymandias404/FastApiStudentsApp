from db import models


def mock_get_existing_student(*args, **kwargs):
    student_id = kwargs['student_id']
    return {'id': student_id, 'email': 'test', 'name': 'name', 'surname': 'surname'}


def mock_get_non_existing_student(*args, **kwargs):
    return None


def mock_get_all_students(*args, **kwargs):
    return [{'id': 1, 'email': 'test1', 'name': 'name', 'surname': 'surname'},
            {'id': 2, 'email': 'test2', 'name': 'name', 'surname': 'surname'},
            {'id': 3, 'email': 'test3', 'name': 'name', 'surname': 'surname'}]


def mock_get_first_student_with_mail(*args, **kwargs):
    return {'id': 1, 'email': 'test', 'name': 'name', 'surname': 'surname'}


def mock_create_student_with_data(*args, **kwargs):
    db_student = models.Student(email='mail', name='name', surname='surname')
    return db_student


def mock_delete_student(*args, **kwargs):
    student_id = kwargs['student_id']
    return {"Message": f"Successfully deleted student with id: {student_id}"}