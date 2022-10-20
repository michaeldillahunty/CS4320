import pytest
import System
import Staff
import User
import Student
import Professor

def test_submit(grading_system):
	student = 'hdjsr7'
	password = 'pass1234'
	grading_system.login(student, password)
	course = 'databases'
	assignment = 'assignment1'
	submission = 'This is my submission'
	date = '3/18/22'
	assert grading_system.usr.submit_assignment(course, assignment, submission, date) == None

@pytest.fixture
def grading_system():
	gradingSystem = System.System()
	gradingSystem.load_data()
	return gradingSystem
