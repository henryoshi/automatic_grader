import os

class Assignments:
    """
    A class to represent the folder of assignments, containing the necessary methods
    to pull filenames and organize the directory.
    """
    def __init__(self, directory):
        """
        A constructor that takes in a String representing the directory
        of the assignment folder.
        """
        self.directory = directory
        self.assignments = self.get_assignments()

    def get_assignments(self):
        """
        A method that returns an array of all file paths from the provided
        directory. Utilizes the os library, creating a shell to the cmd of 
        the system.
        """
        all_files = []
        os_directory = os.fsencode(self.directory)
        # encodes the filename into a usable object
        for file in os.listdir(os_directory):
            # decodes the file into string format for future use
            filename = os.fsdecode(file)
            # checks if the current file is a valid .py script
            if filename.endswith(".py"):
                # creates a full string of the directory and filename combined
                # for future use
                filepath = os.path.join(self.directory, filename)
                all_files.append(filepath)
        return all_files