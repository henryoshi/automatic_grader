
class Student:
    def __init__(self, fname):
        self.fullname = fname
        self.grades = []
    
    def __str__(self):
        return f'Final grade of {self.fullname} is {self.average() * 100}%'
    
    def average(self):
        total = 0
        for grade in self.grades:
            total += grade
        return total / len(self.grades)