import requests
BASE_URL = 'http://127.0.0.1:8000'


def test_create_student(run_around_tests):
    body = {
        "email": "test@test.com",
        "name": "test",
        "surname": "test"
    }
    response = requests.post(url=f'{BASE_URL}/students', json=body)
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
    requests.post(url=f'{BASE_URL}/students', json=body1)
    response = requests.post(url=f'{BASE_URL}/students', json=body2)
    assert response.status_code == 400


def test_get_students(run_around_tests):
    for i in range(3):
        body1 = {
            "email": f"test{i}@test.com",
            "name": "test",
            "surname": "test"
        }
        requests.post(url=f'{BASE_URL}/students', json=body1)
    response = requests.get(url=f'{BASE_URL}/students')
    assert response.status_code == 200
    assert len(response.json()) == 3


def test_get_students_no_students(run_around_tests):
    response = requests.get(url=f'{BASE_URL}/students')
    assert response.status_code == 200
    assert response.json() == []


def test_get_student_by_id(run_around_tests):
    body = {
        "email": "test@test.com",
        "name": "test",
        "surname": "test"
    }
    test_id = requests.post(url=f'{BASE_URL}/students', json=body).json()['id']
    response = requests.get(url=f'{BASE_URL}/students/{test_id}')
    assert response.status_code == 200
    assert response.json()['id'] == test_id


def test_get_student_by_id_no_student_with_id(run_around_tests):
    test_id = 1
    response = requests.get(url=f'{BASE_URL}/students/{test_id}')
    assert response.status_code == 404
    assert response.json()['detail'] == 'Student not found'


def test_update_student(run_around_tests):
    body = {
        "email": "test@test.com",
        "name": "test",
        "surname": "test"
    }
    test_id = requests.post(url=f'{BASE_URL}/students', json=body).json()['id']
    body_updated = {
        "email": "test2@test.com",
        "name": "test2",
        "surname": "test2"
    }
    response = requests.put(url=f'{BASE_URL}/students/{test_id}', json=body_updated)
    assert response.status_code == 200
    assert response.json()['email'] == body_updated['email']
    assert response.json()['name'] == body_updated['name']
    assert response.json()['surname'] == body_updated['surname']


def test_update_student_no_student_with_id(run_around_tests):
    test_id = 1
    body_updated = {
        "email": "test2@test.com",
        "name": "test2",
        "surname": "test2"
    }
    response = requests.put(url=f'{BASE_URL}/students/{test_id}', json=body_updated)
    assert response.status_code == 404
    assert response.json()['detail'] == 'Student not found'


def test_delete_student(run_around_tests):
    body = {
        "email": "test@test.com",
        "name": "test",
        "surname": "test"
    }
    test_id = requests.post(url=f'{BASE_URL}/students', json=body).json()['id']
    response = requests.delete(url=f'{BASE_URL}/students/{test_id}')
    assert response.status_code == 204


def test_delete_student_no_student_with_id(run_around_tests):
    test_id = 1
    response = requests.delete(url=f'{BASE_URL}/students/{test_id}')
    assert response.status_code == 404
    assert response.json()['detail'] == 'Student not found'
