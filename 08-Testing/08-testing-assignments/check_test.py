import pytest
import System
import Student
import User
import Staff

def test_grades(grading_system):
   student = 'hdjsr7'
   password = 'pass1234'
   grading_system.login(student, password)
   course = 'afjaokjkd'
   assert grading_system.usr.check_grades(course) == grading_system.usr.check_grades(course)

@pytest.fixture
def grading_system():
   gradingSystem = System.System()
   gradingSystem.load_data()
   return gradingSystem
