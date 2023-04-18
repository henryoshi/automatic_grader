from professor import Professor as P
from student import Student as S
from classroom import Classroom as C
from auto_grader import Auto_Grader as AG

class ProfManager:
    def __init__(self):
        self.prof = self.generate_prof()
        self.grader = AG(self.assignment_dir , "expected_outputs.txt", self.prof)

    def generate_prof(self):
        name = input("What is your name: ")
        num_students = int(input("How many students are in your class: "))
        studs = []
        for i in range(num_students):
            stu = S(input("Enter the next student name: "))
            studs.append(stu)
        course_desc = input("Enter course description: ")
        self.assignment_dir = input("Enter assignments' folder path: ")
        prof_classroom = C(course_desc, studs, self.assignment_dir)
        return P(name, prof_classroom)
    
    def grade_class(self):
        AG.generate_grades(self.grader)
        P.grade_classroom(self.prof)
    
    def write_expected_file(self):
        with open("expected_outputs.txt", "w") as f:
            ans = input("Enter method name to check or e (exit): ")
            while(ans != 'e'):
                f.write("Method:\n")
                f.write(f"{ans}\n")
                tempio = input("Enter input and output separated by space or e (exit): ")
                while (tempio != 'e'):
                    io = [value.strip() for value in tempio.split()]
                    f.write(f"{io[0]} : {io[1]}\n")
                    tempio = input("Enter input and output separated by space or e (exit): ")
                ans = input("Enter method name to check or e (exit): ")
        

