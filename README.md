# automatic_grader
Repository to store files for EECE 2140's, Student Automatic Grader Project.

Contains classes to represent:
- Classroom
    Fields:
      ArrayList of Students - students
- Student
    Fields:
      String - full_name
      Student_Folder - assignments

- Student_Folder of Work
    Fields:
      ArrayList of Homeworks - homeworks
- Homework
    Fields:
      String - inputs_file
    Methods:
      to_text_file(self)
- Grader
    Fields:
      String - outputs_file
      String - 
    Methods: 
      double getOneGrade()
      
