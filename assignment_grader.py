from iohandler import IOHandler
from student import Student
from classroom import Classroom
import os

class AssignmentGrader(IOHandler):
    """
    A class representing an assignment grader, that is, a class to run
    on a script and compare the expected output with the experimental
    result.
    """
    def __init__(self, expecteds_path, classroom):
        """
        A constructor that takes in the path of the expected outputs
        and inputs, and a classroom to modify each student's tracking of 
        correct answers as the program checks the respective script.
        """
        super().__init__(expecteds_path)
        self.classroom = classroom
        self.total_size = self.get_total_size()
    
    def get_total_size(self):
        """
        A helper method that gets the total number of answers to compare.
        """
        count = 0
        for method in self.dict.keys():
            for item in self.dict[method].values():
                count += 1
        return count

    def grade_assignments(self):
        """
        A method that iterates through each method and within each method iterates through
        test cases, comparing the .run of the respective script with the expected output, and 
        modifying the current student's grade as it does so.
        """
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
        """
        A method that runs ONE method in ONE script with ONE input specified by the various
        parameters.  
        """
        with open(file_path, "r") as f:
            file_str = f.read()
        # Compiles the script into a module
        module = compile(file_str, file_path, "exec")
        # Executes the module's specified method with provided inputs
        namespace = {}
        # Using the prior defined namespace, executes the packaged module
        exec(module, namespace)
        # Returns the execution of the given input on the given method
        result = namespace[method](inpt)
        return result