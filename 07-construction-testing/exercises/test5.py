import pytest
import System

# This function allows the professor to add a student to a course.
# Verify that a student will be added to the correct course in the database.
# Fail: Outputs "TypeError: list indices must be integers or slices, not str", 
# in professor.py "self.users[self.name]['courses'][course] = assignments" should instead be "self.users[name]['courses'][course] = assignments"
def test_add_student(grading_system):
    professor_username = 'goggins'
    professor_password = 'augurrox'
    grading_system.login(professor_username,professor_password)
    student_username = 'akend3'
    course = 'software_engineering'
    grading_system.usr.add_student(student_username, course)
    
@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem