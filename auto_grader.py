from student import Student as S
from classroom import Classroom as C
from assignment_grader import AssignmentGrader as AG

class AutoGrader:
    """
    A Class that represents the automatic_grader for the entire folder.
    Holds the folder's class' professor as well.
    """
    def __init__(self, assignments_path, expecteds_path, prof):
        """
        A constructor that takes in the folder of assignment's path (String), 
        the expected in/outputs path (String), and the Professor linked to this grader.
        """
        self.assignments_path = assignments_path
        self.expecteds_path = expecteds_path
        self.prof = prof
        self.grader = self.generate_grader()
    
    def generate_grader(self):
        """
        Create an assignment grader object that will iterate through
        the students and assignments together, modifying the classroom's
        grades as it goes.
        """
        return AG(self.expecteds_path, self.prof.classroom)
    
    def generate_grades(self):
        """
        Calls the previously made assignment grader to grade the assignments at the 
        inputted folder directory.
        """
        self.grader.grade_assignments()
