import pytest
import System

# Fail: Funtion tried to submit uncreated assignment 
def test_submit_assignment(grading_system):   
    grading_system.login('hdjsr7', 'pass1234')
    grading_system.usr.submit_assignment('03/01/20')

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem