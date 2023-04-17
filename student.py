class Student:
    def __init__(self, fname):
        self.fname = fname
        self.grade = 0
    
    def __str__(self):
        return f'Final grade of {self.fname} is {self.grade}'