import pytest
import System

# This function checks that the password is correct
#Enter several different formats of passwords to verify that the password returns correctly if the passwords are the same.
# Pass
def test_password(grading_system):
    username = 'cmhbf5'
    password =  'bestTA'
    assert grading_system.check_password(username, password) == True    

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem