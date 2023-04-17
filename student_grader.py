from iohandler import IOHandler
from student import Student
from classroom import Classroom
import os

class Student_Grader(IOHandler):
    def __init__(self, testpath, method, class_room):
        super().__init__(testpath)
        self.method = method
        self.class_room = class_room
    
    def grade_assignments(self):
        for student, fname in zip(self.class_room.students, self.class_room.folder.assignments):
            count = 0
            for inpt, output in self.dict.items():
                current_output = self.run(fname, inpt)
                if (current_output == output):
                    count += 1
            student.grade = count / len(self.dict.keys())

    def run(self, file_path, inputs):
        with open(file_path, "r") as f:
            file_str = f.read()
        # Compiles the script into a module
        module = compile(file_str, file_path, "exec")
        # Executes the module's specified method with provided inputs
        namespace = {}
        exec(module, namespace)
        result = namespace[self.method](inputs)
        return result