# just a dummy algorithm that does nothing
from solution import Solution

class Dummy:
    
    def solve(self, input, current):
        return current

    def run(self, queue, input, current = Solution()):
        queue.put(self.solve(input, current))


    