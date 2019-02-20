from config import Config
from solution import Solution
from utils.preprocess import Preprocess
from utils.heuristics import Heuristics
import importlib

class Algorithm:

    def __init__(self):
        self.config = {}
        
        self.name = self.__class__.__name__.lower()
        if self.name in Config.get:
            self.config = Config.get[self.name]

    
    def run(self, queue, input, current = Solution()):

        # execute preprocess function
        if 'prefunction' in self.config:
            preprocess = Preprocess()
            input = getattr(preprocess, self.config['prefunction'])(input)
        
        # add the result of the algorithm to the main thread queue
        queue.put(self.solve(input, current))

    
    def call_heuristic(self, candidates, data = {}):
        heuristics = Heuristics()

        best_candidate = candidates.pop()
        max_value = getattr(heuristics, self.config['heuristic'])(best_candidate, data)

        for candidate in candidates:
            current_value = getattr(heuristics, self.config['heuristic'])(candidates, data)
            if current_value > best_candidate:
                best_candidate = candidate
                max_value = current_value

        return best_candidate


    def solve(self, input, current = Solution()):
        raise Exception('%s algorithm needs to implement solve function' % self.name)
