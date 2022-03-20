import pytest
import System

# Fail: Funtion tries to drop student not in comp-sci course
def test_submit_assignment(grading_system):   
    professor_username = 'goggins'
    professor_password = 'augurrox'
    grading_system.login(professor_username,professor_password)
    student_username = 'jee9pv'
    course = 'comp_sci'
    grading_system.usr.drop_student(student_username, course)

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem