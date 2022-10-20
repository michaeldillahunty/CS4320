import pytest
import System
import Staff
import User
import Professor

def test_dropStudent(grading_system):
	name = 'akend3'
	course = 'databases'
	prof = 'saab'
	password = 'boomr345'
	grading_system.login(prof, password)
	assert grading_system.usr.drop_student(name, course) == None

@pytest.fixture
def grading_system():
	gradingSystem = System.System()
	gradingSystem.load_data()
	return gradingSystem
