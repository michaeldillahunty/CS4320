import pytest
import System

def test_username(grading_system):
	user = '12849_dakjhf'
	grading_system.login(user, 'dakf')

@pytest.fixture
def grading_system():
	gradingSystem = System.System()
	gradingSystem.load_data()
	return gradingSystem
