class IOHandler:
    """
    A class representing IOHandling (Input - Output Handling). That is,
    the reading and conversion of the expected input - output text file into
    a usable dictionary.
    """
    def __init__(self, expecteds_path):
        """
        A constructor that takes in a path (String) to the expected input output text file,
        and calls a conversion method that changes that path's text into a readable
        dictionary.
        """
        # If an external text file is used, 
        # the separator can be changed to match
        self.sep = ":"
        self.expecteds_path = expecteds_path
        self.dict = self.convert_to_dic()
    
    def convert_to_dic(self):
        """
        A method that returns a dictionary of method keys linked to dictionaries
        of input keys linked to respective output values.
        """
        dic = {}
        with open(self.expecteds_path, "r") as f:
            # Converts all the text to one string
            whole_file = f.read().strip()
            # Divides the text by 'Method:' header
            file_arr = whole_file.split("Method:")
            for i in range(1, len(file_arr)):
                inner_dic = {}
                # Creates an array of values separated by newline characters 
                # if the result would not be empty.
                all_lines = [s for s in file_arr[i].split("\n") if s != ""]
                for j in range(1, len(all_lines)):
                    # Assigns the inner dictionary values, linking method's expected 
                    # inputs with their outputs
                    inpt, expected = all_lines[j].split(":")
                    inner_dic[inpt.strip()] = expected.strip()
                dic[all_lines[0]] = inner_dic
        return dic