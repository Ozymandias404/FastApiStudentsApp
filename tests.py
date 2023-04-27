import unittest
import requests
BASE_URL = "http://127.0.0.1:8000"


class TestGetStudents(unittest.TestCase):
    url = BASE_URL + "/students"

    def test_gets_students_200(self):
        response = requests.get(url=self.url)
        self.assertEqual(response.status_code, 200)


class TestGetStudent(unittest.TestCase):
    url = BASE_URL + "/student"

    def test_gets_students_200(self):
        response = requests.get(url=f"{self.url}/1")
        self.assertEqual(response.status_code, 200)

    def test_gets_students_404(self):
        response = requests.get(url=f"{self.url}/2137")
        self.assertEqual(response.status_code, 404)


class TestGetStudent(unittest.TestCase):
    url = BASE_URL + "/student"

    def test_gets_students_200(self):
        response = requests.get(url=f"{self.url}/1")
        self.assertEqual(response.status_code, 200)

    def test_gets_students_404(self):
        response = requests.get(url=f"{self.url}/2137")
        self.assertEqual(response.status_code, 404)




# class TestStringMethods1(unittest.TestCase):
#
#     def test_upper(self):
#         self.assertEqual('foo'.upper(), 'FOO')