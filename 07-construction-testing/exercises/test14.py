import pytest
import System

# Fail: Funtion tries to submit unassigned assignment
def test_submit_assignment(grading_system):   
    grading_system.login('hdjsr7', 'pass1234')
    grading_system.usr.submit_assignment('cloud_computing', 'assignment5','Blahhhhh', '03/01/20')

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem