import pytest
import Student
import System
import Staff
import User

def test_view(grading_system):
	student = 'hdjsr7'
	password = 'pass1234'
	grading_system.login(student, password)
	course = 'databases'
	assert grading_system.usr.view_assignments(course) == '[[assignment1, N/A]]'

@pytest.fixture
def grading_system():
	gradingSystem = System.System()
	gradingSystem.load_data()
	return gradingSystem
