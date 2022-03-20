import pytest
import System

# This function returns assignments and their due dates for a specific course. 
# Verify that the correct assignments for the correct course are returned.
# Pass
def test_view_assignments(grading_system):
    grading_system.login('akend3', '123454321')
    assert grading_system.usr.view_assignments('comp_sci') == [['assignment1', '2/2/20'], ['assignment2', '2/10/20']]
    
@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem