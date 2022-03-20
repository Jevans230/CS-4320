import pytest
import System

# Fail: Funtion tries to change grade on assignment in uncreated course
def test_submit_assignment(grading_system):   
    professor_username = 'saab'
    professor_password = 'boomr345'
    grading_system.login(professor_username,professor_password)
    username = 'akend3'
    course = 'English'
    assignment = 'assignment1'
    grade = 0
    grading_system.usr.change_grade(username, course, assignment, grade)

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem