import pytest
import System
import Staff
import User
import Professor

def test_create(grading_system):
        assignment = 'ajklfsajaklfj;aalkf'
        due = '3/25/22'
        course = 'ajkfjaiowf'
        prof = 'saab'
        password = 'boomr345'
        grading_system.login(prof, password)
        grading_system.usr.create_assignment(assignment, due, course)

@pytest.fixture
def grading_system():
        gradingSystem = System.System()
        gradingSystem.load_data()
        return gradingSystem
