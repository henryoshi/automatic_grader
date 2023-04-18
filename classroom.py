from assignment_folder import AssignmentFolder as AF

class Classroom:
    """
    A Class representing a classroom, that is, a list of students
    the course title, and the directory of this classrooms folder
    of assignments. 
    """
    def __init__(self, course_title, students, folder_dir):
        """
        A Constructor that takes in a course title (String), a List of Students
        and the directory needed for file grading (String). Also, calls
        the Assignments class to create a list of the filenames inside
        of the provided directory.
        """
        self.course_title = course_title
        self.students = students
        self.directory = folder_dir
        self.folder = AF(folder_dir)

    def generate_grades(self):
        """
        A method that appends to the previously created text file the 
        grades of each student as well as their name by calling the 
        built in __str__ function of each student in the field students.
        """
        with open(f"{self.course_title}_grades.txt", "w") as f:
            for student in self.students:
                f.write(str(student) + "\n")