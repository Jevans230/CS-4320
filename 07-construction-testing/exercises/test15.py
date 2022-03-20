import pytest
import System

# Fail: Funtion logs in with incorrect username
def test_password(grading_system):
    username = 'cmhbf5'
    password =  'wrongUsername'
    assert grading_system.check_password(username, password) == True    

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem