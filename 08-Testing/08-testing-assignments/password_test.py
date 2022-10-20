import pytest
import System

def test_password(grading_system):
	username = 'goggins'
	password = 'augurrox'
	assert grading_system.check_password(username, password) == True

	username2 = 'calyam'
	password2 = '#yeet'
	assert grading_system.check_password(username2, password2) == True

	username3 = 'saab'
	password3 = 'boomr345'
	assert grading_system.check_password(username3, password3) == True

@pytest.fixture
def grading_system():
	gradingSystem = System.System()
	gradingSystem.load_data()
	return gradingSystem