class IOHandler:
    def __init__(self, test_path):
        self.sep = input("What is your input/output separator: ")
        self.test_path = test_path
        self.dict = self.convert_to_dic()
        print(self.dict)
    
    def convert_to_dic(self):
        dic = {}
        with open(self.test_path, "r") as f:
            for line in f:
                inpt, expected = line.split(self.sep)
                inpt = inpt.strip()
                expected = expected.strip()
                dic[inpt] = expected
        return dic