import requests


def test_create_student(run_around_tests):
    body = {
        "email": "test@test.com",
        "name": "test",
        "surname": "test"
    }
    response = requests.post(url='http://127.0.0.1:8000/students', json=body)
    assert response.status_code == 201


def test_create_student_same_mail(run_around_tests):
    body1 = {
        "email": "test@test.com",
        "name": "test",
        "surname": "test"
    }
    body2 = {
        "email": "test@test.com",
        "name": "test",
        "surname": "test"
    }
    requests.post(url='http://127.0.0.1:8000/students', json=body1)
    response = requests.post(url='http://127.0.0.1:8000/students', json=body2)
    assert response.status_code == 400
