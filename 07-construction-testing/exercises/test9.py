import pytest
import System

# This function returns the users grades for a specific course. Verify the correct grades are returned for the correct user.
# Pass 
def test_check_grades(grading_system):
    grading_system.login('akend3', '123454321')
    assert grading_system.usr.check_grades('comp_sci') == [['assignment1', 99], ['assignment2', 66]]
    
@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem