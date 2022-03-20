import pytest
import System

# This function allows a student to submit an assignment. 
# Verify that the database is updated with the correct assignment, submission, submission date and in the correct course.
# Pass
def test_submit_assignment(grading_system):   
    grading_system.login('hdjsr7', 'pass1234')
    grading_system.usr.submit_assignment('cloud_computing', 'assignment1','Blahhhhh', '03/01/20')

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem