import pytest
import System

# This function allows the professor to drop a student in a course. 
# Verify that the student is added and dropped from the correct course in the database.
# Pass 
def test_drop_student(grading_system):   
    professor_username = 'goggins'
    professor_password = 'augurrox'
    grading_system.login(professor_username,professor_password)
    student_username = 'akend3'
    course = 'comp_sci'
    grading_system.usr.drop_student(student_username, course)
    
@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem