from file_handler import Grader
from student import Student
from student_folder import Student_Folder
from classroom import Classroom
import os

class Student_Grader(Grader):
    def __init__(self, testpath, class_room = Classroom()):
        super().__init__(testpath)
        self.class_room = class_room
    
    def grade_assignments(self):
        for student, fname in zip(self.class_room.students, self.class_room.folder.assignments):
            count = 0
            for input, output in super().dic.items:
                current_output = self.run(fname, input)
                if (current_output == output):
                    count += 1
            student.grade = count / len(super().dic)

    def run(self, file_path, method, inputs):
        with open(file_path, "r") as f:
            file_str = f.read()
        # Compiles the script into a module
        module = compile(file_str, file_path, "exec")
        # Executes the module's specified method with provided inputs
        namespace = {}
        exec(module, namespace)
        result = namespace[method](inputs)
        return result