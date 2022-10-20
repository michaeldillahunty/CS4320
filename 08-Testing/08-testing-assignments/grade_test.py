import pytest
import System
import Staff
import User
import Professor
import json

def test_grade(grading_system):
	user = 'akend3'
	course = 'comp_sci'
	assignment = 'assignment1'
	grade = '70'
	prof = 'saab'
	password = 'boomr345'
	grading_system.login(prof, password)
	assert grading_system.usr.change_grade(user, course, assignment, grade) == None
	

@pytest.fixture
def grading_system():
	gradingSystem = System.System()
	gradingSystem.load_data()
	return gradingSystem
