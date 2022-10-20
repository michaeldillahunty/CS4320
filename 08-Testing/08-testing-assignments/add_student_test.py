import pytest
import System
import Staff
import User
import Professor

def test_addStudent(grading_system):
	name = 'x'
	course = 'comp_sci'
	prof = 'saab'
	password = 'boomr345'
	grading_system.login(prof, password)
	grading_system.usr.add_student(name, course)

@pytest.fixture
def grading_system():
	gradingSystem = System.System()
	gradingSystem.load_data()
	return gradingSystem
