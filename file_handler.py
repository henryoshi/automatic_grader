class Grader:
    def __init__(self, test_path):
        self.sep = input("What is your input/output separator: ")
        self.test_path = test_path
        self.dic = {}
    
    def convert_to_dic(self):
        with open(self.test_path, "r") as f:
            for line in f:
                input, expected = line.strip().split(self.sep)
                self.dic[input] = expected