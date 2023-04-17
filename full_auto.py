from student import Student as S
from classroom import Classroom as C
#from iohandler import TestNamer
from student_grader import Student_Grader as SG

fpath = r"C:\Users\shiel\OneDrive - Northeastern University\Desktop\Northeastern\Spring2023\eece2140\Python\Final Project\automatic_grader\assignments"
expected_path = "expected_outputs.txt"

henry = S("Henry Shields")
jerry = S("Jerry Atrick")
maeve = S("Maeve Mace")
roger = S("Roger Moore")
chad = S("Chad Jock")

studs = [henry, jerry, maeve, roger, chad]

classroom_tester = C("EECE 2140 Section 3", studs, fpath)

stud_grader = SG(expected_path, "add_then_square", classroom_tester)
stud_grader.grade_assignments()

# https://docs.python.org/3/library/os.html
