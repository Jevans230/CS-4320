import pytest
import System

# The login function takes a name and password and sets the user for the program. 
# Verify that the correct user is created with this test, and use the json files to check that it adds the correct data to the user.
# Pass
def test_login(grading_system): 
    username = 'cmhbf5'
    password =  'bestTA'
    grading_system.login(username,password)
    assert grading_system.usr.password == 'bestTA'


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem