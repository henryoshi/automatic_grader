import os

class Assignments:
    def __init__(self, directory):
        self.directory = directory
        self.assignments = self.get_assignments()

    def get_assignments(self):
        all_files = []
        os_directory = os.fsencode(self.directory)
        for file in os.listdir(os_directory):
            filename = os.fsdecode(file)
            if filename.endswith(".py"):
                all_files.append(filename)
        return all_files