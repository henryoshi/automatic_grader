from classroom import Classroom as C

class Professor:
    """
    A class representing the user's information, which is their name (String)
    and their Classroom object.
    """
    def __init__(self, full_name, classroom):
        """
        A Constructor that assigns a full name of the user and links its
        Classroom
        """
        self.full_name = full_name
        self.classroom = classroom

    def grade_classroom(self):
        """
        A helper method that calls down to this professor's Classroom to
        generate the grades of the students.
        """
        C.generate_grades(self.classroom)