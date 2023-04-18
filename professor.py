from classroom import Classroom as C

class Professor:
    def __init__(self, full_name, classroom):
        self.full_name = full_name
        self.classroom = classroom

    def grade_classroom(self):
        C.generate_grades(self.classroom)
    