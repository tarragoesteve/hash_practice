import fileinput
from interfaces.solutionInterface import SolutionInterface

class Solution(SolutionInterface):
    
    def __init__(self):
        # init code
        self.test = 0
        return

    def value(self):
        # return the cost of the solution
        return 0

    def render(self):
        # pretty print of the solution
        return