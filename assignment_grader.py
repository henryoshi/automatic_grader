from iohandler import IOHandler
from student import Student
from classroom import Classroom
import os

class Assignment_Grader(IOHandler):
    def __init__(self, testpath, classroom):
        super().__init__(testpath)
        self.classroom = classroom
        self.total_size = self.get_total_size()
    
    def get_total_size(self):
        count = 0
        for method in self.dict.keys():
            for item in self.dict[method].values():
                count += 1
        return count

    def grade_assignments(self):
        for method in self.dict.keys():
            for student, fname in zip(self.classroom.students, self.classroom.folder.assignments):
                count = 0
                for inpt, output in self.dict[method].items():
                    
                    current_output = self.run(fname, method, inpt)
                    print(f"{student.fullname} on {inpt} is {current_output}")
                    if (str(current_output) == output):
                        student.grades.append(1)
                    else:
                        student.grades.append(0)

    def run(self, file_path, method, inpt):
        with open(file_path, "r") as f:
            file_str = f.read()
        # Compiles the script into a module
        module = compile(file_str, file_path, "exec")
        # Executes the module's specified method with provided inputs
        namespace = {}
        exec(module, namespace)
        result = namespace[method](inpt)
        return result