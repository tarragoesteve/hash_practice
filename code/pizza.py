class Pizza:
    """A simple example class"""
    board = []
    rows = 0
    columns = 0
    low = 0
    high = 0
    slides = []

    def __init__(self, rows,columns,low, high):
        self.rows = rows
        self.columns = columns
        self.low=low
        self.high = high

    def read_line(self, line):
        self.board.append(line)
    
    def save_result(self):
        sum = 0
        for cell in self.slides:
            sum += abs(cell[2] - cell[0]) * abs(cell[3] - cell[1])
        print(self.slides)
        print(sum)
    
    def solve(self):
        self.solve_recursive(0,0,self.rows,self.columns)
        pass

    def valid_slice(self,x1,y1,x2,y2):
        return self.count_cells(x1,y1,x2,y2) <= self.high and self.count_mushroms(x1,y1,x2,y2) >= self.low and (self.count_cells(x1,y1,x2,y2) - self.count_mushroms(x1,y1,x2,y2)) >= self.low
    
    def impossible_slice(self,x1,y1,x2,y2):
        return self.count_mushroms(x1,y1,x2,y2) < self.low or self.count_cells(x1,y1,x2,y2) - self.count_mushroms(x1,y1,x2,y2) < self.low

    def count_mushroms(self,x1,y1,x2,y2):
        mushroms = 0
        for i in range(x1,x2):
            for j in range(y1,y2):
                if(self.board[i][j] == 'M'):
                    mushroms = 1 + mushroms
        return mushroms

    def compute_score(self, x1,y1,x2,y2):
        mushroms = self.count_mushroms(x1,y1,x2,y2)
        tomatoes = self.count_cells(x1,y1,x2,y2) - mushroms
        total = mushroms + tomatoes
        if total == 0:
            return 0
        if (tomatoes < self.low or mushroms < self.low):
            return 0.0

        return 2 * (.5 - min(mushroms/total,tomatoes/total))

    def count_cells(self,x1,y1,x2,y2):
        return (x2 - x1) * (y2 - y1)

    def solve_recursive(self,x1,y1,x2,y2):
        if(self.valid_slice(x1,y1,x2,y2)):
            self.slides.append([x1,y1,x2,y2])
            return True
        if(self.impossible_slice(x1,y1,x2,y2)):
            return False
        best_score = 0
        best_division = [[0,0,0,0],[0,0,0,0]]
        for i in range(x1+1,x2):
            score = self.count_cells(x1,y1,i,y2)* self.compute_score(x1,y1,i,y2) + self.count_cells(i,y1,x2,y2)*self.compute_score(i,y1,x2,y2)
            if (score > best_score):
                best_division = [[x1,y1,i,y2],[i,y1,x2,y2]]
            
        for j in range(y1+1,y2):
            score = self.count_cells(x1,y1,x2,j)* self.compute_score(x1,y1,x2,j) + self.count_cells(x1,j,x2,y2)*self.compute_score(x1,j,x2,y2)
            if (score > best_score):
                best_division = [[x1,y1,x2,j],[x1,j,x2,y2]]


        self.solve_recursive(best_division[0][0],best_division[0][1],best_division[0][2],best_division[0][3])
        self.solve_recursive(best_division[1][0],best_division[1][1],best_division[1][2],best_division[1][3])


#Read input file
filepath = '../inputs/c_medium.in' 
with open(filepath) as fp:  
   for cnt, line in enumerate(fp):
        if cnt == 0:
           aux = line.split()
           my_pizza = Pizza(int(aux[0]),int(aux[1]), int(aux[2]), int(aux[3]))
        else:
            my_pizza.read_line(line)
        

my_pizza.solve()
my_pizza.save_result()