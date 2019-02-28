# just a dummy algorithm that does nothing
from solution import Solution
from interfaces.algorithmInterface import Algorithm
from interfaces.heuristicInterface import HeuristicInterface
import queue

class Dissabte(Algorithm, HeuristicInterface):

    def omple_x(self, filled, x, y, pos1, pos2):
        for i in range(x, pos1):
            for j in range(y, pos2):
                filled[i][j] = True

    def troba_quadrat_maxim(self, input, filled, x, y):
        n = input.max_pieces
        m = 1
        while(n >= 1):
            x_found = False
            n_tom = 0
            n_mush = 0
            for i in range(x, int(min(x + n, input.rows))):
                for j in range(y, int(min(y + m, input.columns))):
                    if filled[i][j]:
                        x_found = True
                    
                    if (input.input_matrix[i][j] == "T"): 
                        n_tom += 1
                    elif (input.input_matrix[i][j] == "M"): 
                        n_mush += 1
            print([n_tom, n_mush])
            if (not x_found and n_tom >= input.min_ingredients and n_mush >= input.min_ingredients):
                return [True, i, j]
            n = n/2
            m = 2*m
        return [False, x, y]
    
    
    def solve(self, input, current = Solution()):
        cua = queue.Queue(0)
        cua.put([0,0])
        filled = [[False] * input.columns] * input.rows
        while (not cua.empty()):
            [x,y] = cua.get()
            [trobat, pos1, pos2] = self.troba_quadrat_maxim(input, filled,x,y)
            print([x,y, trobat, pos1, pos2])
            if (pos2 + 1 < input.columns):
                 cua.put([x, pos2 + 1])
            if (pos1 + 1 < input.rows):
                 cua.put([pos1 + 1, y])
            if(trobat):
                current.add_slice(x, y, pos1, pos2)
                self.omple_x(filled, x, y, pos1, pos2)

        

        
        input.input_matrix
        return current