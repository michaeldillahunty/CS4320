import pytest
import System
import Staff
import User
import Student

def test_ontime(grading_system):
	student = 'hdjsr7'
	password = 'pass1234'
	grading_system.login(student, password)
	submission_date = '3/4/22'
	due_date = '3/4/22'
	assert grading_system.usr.check_ontime(submission_date, due_date) == True
	submission2_date = '5/2/21'
	due_date2 = '5/1/21'
	assert grading_system.usr.check_ontime(submission2_date, due_date2) == False

@pytest.fixture
def grading_system():
	gradingSystem = System.System()
	gradingSystem.load_data()
	return gradingSystem
