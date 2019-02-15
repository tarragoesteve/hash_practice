class Pizza:
    """A simple example class"""
    board = []
    rows = 0
    columns = 0
    low = 0
    high = 0

    def __init__(self, rows,columns, low, high):
        pass

    def read_line(self, line):
        self.board.append(line)


#Read input file
filepath = '../inputs/a_example.in'  
with open(filepath) as fp:  
   for cnt, line in enumerate(fp):
        if cnt == 0:
           aux = line.split()
           my_pizza = Pizza(int(aux[0]),int(aux[1]), int(aux[2]), int(aux[3]))
        else:
            my_pizza.read_line(line)
        

