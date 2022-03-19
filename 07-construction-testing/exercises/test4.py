import pytest
import System

# This function allows the staff to create a new assignment.  
# Verify that an assignment is created with the correct due date in the correct course in the database
# Pass 
def test_new_assignment(grading_system):
    professor_username = 'saab'
    professor_password = 'boomr345'
    grading_system.login(professor_username,professor_password)
    assignment = 'assignment3'
    date = '04/01/20'
    course = 'comp_sci'
    grading_system.usr.create_assignment(assignment, date, course)
  
@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem