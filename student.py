class Student:
    """
    A class representing a student who has a Boolean/int List representing
    how many questions were graded right (1) or wrong (0) and a full name.
    """
    def __init__(self, fname):
        """
        A constructor that takes in a String representing the student's name
        and initializes this Student's grades to be a new empty list.
        """
        self.fullname = fname
        self.grades = []
    
    def __str__(self):
        """
        A method to overwrite the built in object method __str__
        to display the student's name and grade.
        """
        return f'Final grade of {self.fullname} is {(self.average() * 100):.2f}%'
    
    def average(self):
        """
        A helper method to get the fraction of correct answers
        this student currently has reflected by their grades list.
        """
        total = 0
        for grade in self.grades:
            total += grade
        return total / len(self.grades)