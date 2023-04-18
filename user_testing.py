from prof_management import ProfManager as PM
tester = PM()
PM.write_expected_file(tester)
PM.grade_class(tester)

#auto_grader = AG(r"C:\Users\shiel\OneDrive - Northeastern University\Desktop\assignments", "expected_outputs.txt")
#AG.generate_grades(auto_grader)

# C:\Users\shiel\OneDrive - Northeastern University\Desktop\Northeastern\Spring2023\eece2140\Python\automatic_grader\assignments
# expected_path = "expected_outputs.txt"
# EECE 2140 Section 3
# add_then_square

# https://docs.python.org/3/library/os.html