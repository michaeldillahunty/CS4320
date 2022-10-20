import pytest
import System
import Staff
import User
import Professor

def test_create(grading_system):
	assignment = 'something'
	due = '3/25/22'
	course = 'comp_sci'
	prof = 'saab'
	password = 'boomr345'
	grading_system.login(prof, password)
	assert grading_system.usr.create_assignment(assignment, due, course) == None 

@pytest.fixture
def grading_system():
	gradingSystem = System.System()
	gradingSystem.load_data()
	return gradingSystem