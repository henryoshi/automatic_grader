from student import Student as S
from classroom import Classroom as C
from assignment_grader import Assignment_Grader as AG

class Auto_Grader:
    def __init__(self, assignments_path, expecteds_path, prof):
        self.assignments_path = assignments_path
        self.expecteds_path = expecteds_path
        self.prof = prof
        self.grader = self.generate_grader()
    
    def generate_grader(self):
        return AG(self.expecteds_path, self.prof.classroom)
    
    def generate_grades(self):
        self.grader.grade_assignments()
