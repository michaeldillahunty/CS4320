import pytest
import System
import User
import Student

def test_studentSubmit(grading_system):
	student = 'hdjsr7'
	password = 'pass1234'
	grading_system.login(student, password)
	course = 'aklfjaavafj'
	assignment = 'assignment1'
	submission = 'whatever'
	date = '3/5/12'
	grading_system.usr.submit_assignment(course, assignment, submission, date)

@pytest.fixture
def grading_system():
	gradingSystem = System.System()
	gradingSystem.load_data()
	return gradingSystem
