import pytest
import System

# This function will change the grade of a student and updates the database. 
# Verify that the correct grade is changed on the correct user in the database. 
# Fail: sets grade equal to 0 not matter what input is
def test_grade(grading_system):
    professor_username = 'saab'
    professor_password = 'boomr345'
    grading_system.login(professor_username,professor_password)
    username = 'akend3'
    course = 'comp_sci'
    assignment = 'assignment1'
    grade = 0
    grading_system.usr.change_grade(username, course, assignment, grade)
  
@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem