from professor import Professor as P
from student import Student as S
from classroom import Classroom as C
from auto_grader import AutoGrader as AG
import os

class ProfManager:
    """
    The outer class of the auto grading project, taking in user-input and designating it
    to the appropriate subclass and their methods.
    """
    def __init__(self):
        """A constructor that takes in no values but calls methods to prompt the user
        for input that will create fields of type Professor and AutoGrader"""
        self.prof = self.generate_prof()
        self.grader = AG(self.assignment_dir , "expected_outputs.txt", self.prof)


    def generate_prof(self):
        """
        A Method that gets user input to create a professor object linked to this management class.
        This includes creating a directory String, Classroom, and course title.
        """
        name = input("What is your name: ")
        num_students = int(input("How many students are in your class: "))
        studs = []
        for i in range(num_students):
            stu = S(input("Enter the next student name: "))
            studs.append(stu)
        course_title = input("Enter course description: ")
        self.assignment_dir = input("Enter assignments' folder path: ")
        prof_classroom = C(course_title, studs, self.assignment_dir)
        return P(name, prof_classroom)
    
    def grade_class(self):
        """
        A Method that calls the previously made AutoGrader to grade the assignments.
        """
        AG.generate_grades(self.grader)
        P.grade_classroom(self.prof)
    
    def write_expected_file(self):
        """
        A Method that allows the user (professor) to write their own expected inputs and outputs
        including the method names to test.
        """
        with open("expected_outputs.txt", "w") as f:
            ans = input("Enter method name to check or e (exit): ")
            while(ans != 'e'):
                f.write("Method:\n")
                f.write(f"{ans}\n")
                tempio = input("Enter input and output separated by space or e (exit): ")
                while (tempio != 'e'):
                    # grabs a single input and output by splitting 
                    # the user's entered string at the spaces
                    io = [value.strip() for value in tempio.split()]
                    # writes this pair to the opened file.
                    f.write(f"{io[0]} : {io[1]}\n")
                    tempio = input("Enter input and output separated by space or e (exit): ")
                ans = input("Enter method name to check or e (exit): ")