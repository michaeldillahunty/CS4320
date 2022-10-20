import pytest
import System
import Student
import User
import Staff

def test_grades(grading_system):
        TA = 'cmhbf5'
        password = 'bestTA'
        grading_system.login(TA, password)
        assert grading_system.usr.check_grades('ajfkdja') == grading_system.usr.check_grades('databases')

@pytest.fixture
def grading_system():
        gradingSystem = System.System()
        gradingSystem.load_data()
        return gradingSystem
