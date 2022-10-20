import pytest
import System

def test_login(grading_system):
	username = 'cmhbf5'
	password = 'wrong'
	grading_system.login(username, password)
	assert grading_system.usr.name == 'cmhbf5' 

@pytest.fixture
def grading_system():
	gradingSystem = System.System()
	gradingSystem.load_data()
	return gradingSystem
