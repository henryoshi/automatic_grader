from student import Student as S
from classroom import Classroom as C
from student_grader import Student_Grader as SG

class Auto_Grader:
    def __init__(self, assignments_path, expecteds_path):
        self.assignments_path = assignments_path
        self.expecteds_path = expecteds_path
        self.classroom = self.generate_classroom()
        self.grader = self.generate_grader()
    
    def generate_classroom(self):
        num = int(input("How many students in the class: "))
        students = []
        for i in range(num):
            name = input("Next student name: ")
            students.append(S(name))
        desc = input("Class name or description: ")
        classroom = C(desc, students, self.assignments_path)
        return classroom
    
    def generate_grader(self):
        return SG(self.expecteds_path, self.classroom)
    
    def generate_grades(self):
        self.grader.grade_assignments()
        self.classroom.generate_grades()
