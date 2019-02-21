import fileinput


class ProblemInput:
    
    def __init__(self, filepath):
        self.init_variables()

        with open(filepath) as fp:  
            for cnt, line in enumerate(fp):
                self.read_line(cnt, line)


    def init_variables(self):
        self.input_matrix = []
            

    def read_line(self, cnt, line):
        if cnt == 0:
            [self.rows, self.columns, self.min_ingredients, self.max_pieces] = map(int, line.split())
        else:
            self.input_matrix.append(line)
        