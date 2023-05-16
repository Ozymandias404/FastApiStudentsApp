
def mock_get_existing_student(*args, **kwargs):
    student_id = kwargs['student_id']
    return {'id': student_id, 'email': 'test', 'name': 'name', 'surname': 'surname'}


def mock_get_non_existing_student(*args, **kwargs):
    return None

