from assignment_folder import Assignments as A

class Classroom:
    def __init__(self, full_course, students, folder_dir):
        self.full_course = full_course
        self.students = students
        self.directory = folder_dir
        self.folder = A(folder_dir)

    def generate_grades(self):
        with open(f"{self.full_course}_grades.txt", "w") as f:
            for student in self.students:
                f.write(str(student) + "\n")