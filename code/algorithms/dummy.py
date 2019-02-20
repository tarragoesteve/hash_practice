# just a dummy algorithm that does nothing
from solution import Solution
from interfaces.algorithmInterface import Algorithm

class Dummy(Algorithm):
    
    def solve(self, input, current = Solution()):
        current.test = self.call_heuristic([1,2,3,4,5,6])
        return current