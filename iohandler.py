class IOHandler:
    def __init__(self, test_path):
        self.sep = ":"
        self.test_path = test_path
        self.dict = self.convert_to_dic()
    
    def convert_to_dic(self):
        dic = {}
        with open(self.test_path, "r") as f:
            whole_file = f.read().strip()
            file_arr = whole_file.split("Method:")
            for i in range(1, len(file_arr)):
                inner_dic = {}
                current = [s for s in file_arr[i].split("\n") if s != ""]
                for j in range(1, len(current)):
                    inpt, expected = current[j].split(":")
                    inner_dic[inpt.strip()] = expected.strip()
                dic[current[0]] = inner_dic
        return dic