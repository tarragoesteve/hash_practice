import fileinput
from interfaces.solutionInterface import SolutionInterface

class Solution(SolutionInterface):
    
    # core functions

    def __init__(self):
        # init code
        self.slices = []
        self.cvalue = 0
        return


    def value(self):
        # return the cost of the solution            
        return self.cvalue


    def render(self):
        # pretty print of the solution
        return print(self.to_string())


    def to_string(self):
        ret = '%i\n' % len(self.slices)
        for sli in self.slices:
            for val in sli:
               ret += '%i ' % val
            ret += '\n'
        
        return ret


    # build functions

    def add_slice(self, x1, y1, x2, y2):
        self.slices.append([x1, y1, x2, y2])
        self.cvalue += abs(x2 - x1 + 1) * abs(y2 - y1 + 1)