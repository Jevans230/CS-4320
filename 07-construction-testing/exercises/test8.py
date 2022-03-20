import pytest
import System

# This function checks if an assignment is submitted on time. 
# Verify that it will return true if the assignment is on time, and false if the assignment is late.
# Fail: Does not change ontime status, always returns true
def test_assignment_ontime(grading_system):   
    grading_system.login('akend3', '123454321')
    assert grading_system.usr.check_ontime('3/1/20','2/2/20') == False 

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem