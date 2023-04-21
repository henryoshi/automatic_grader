import unittest
from assignment_folder import AssignmentFolder as AF
from assignment_grader import AssignmentGrader as AG
from classroom import Classroom as C
from prof_management import ProfManager as PM
from student import Student as S

s1 = S("Gandalf")
s2 = S("Voldemort")
s3 = S("Ernie")
s4 = S("Neil DeGrasse Tyson")
s5 = S("Elon Musk")
studs = [s1, s2, s3, s4, s5]
c1 = C("EECE 2140 - Section 1", studs,"C:/Users/shiel/OneDrive - Northeastern University/Desktop/assignments")
af1 = AF("C:/Users/shiel/OneDrive - Northeastern University/Desktop/assignments")
ag1 = AG("expected_outputs.txt", c1)
pm1 = PM()
dictionary = {"add_then_square" : {1 : 4, 2 : 9, 0 : 1, 10 : 121}, "add_abc" : {"abc" : "abcabc", "eece" : "eeceabc"}}

class TestStudent(unittest.TestCase):
    def test_student_before(self):
        self.assertEqual(s1.get_average, 0)
    ag1.grade_assignments()
    def test_student_after(self):
        self.assertEqual(s1.get_average, 1)

class TestAssignmentGrader(unittest.TestCase):
    def test_AG(self):
        self.assertEquals(ag1.convert_to_dic(), dictionary)

class TestAssignmentFolder(unittest.TestCase):
    def test_AF(self):
        self.assertEquals(af1.get_assignments, 
                          ["C:/Users/shiel/OneDrive - Northeastern University/Desktop/assignments/homework1.py", 
                           "C:/Users/shiel/OneDrive - Northeastern University/Desktop/assignments/homework2.py", 
                           "C:/Users/shiel/OneDrive - Northeastern University/Desktop/assignments/homework3.py", 
                           "C:/Users/shiel/OneDrive - Northeastern University/Desktop/assignments/homework4.py", 
                           "C:/Users/shiel/OneDrive - Northeastern University/Desktop/assignments/homework5.py"])