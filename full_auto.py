from student import Student as S
from classroom import Classroom as C

fpath = "C:\Users\shiel\OneDrive - Northeastern University\Desktop\Northeastern\Spring2023\eece2140\Python\Final Project\automatic_grader\assignments"
expected_path = "expected_outputs.txt"

henry = S("Henry Shields")
jerry = S("Jerry Atrick")
maeve = S("Maeve Mace")
roger = S("Roger Moore")
chad = S("Chad Jock")

studs = list(henry, jerry, maeve, roger, chad)

classroom_tester = C("EECE 2140 Section 3", studs, fpath)


# https://docs.python.org/3/library/os.html
