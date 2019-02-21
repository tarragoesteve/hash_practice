from utils.heuristics import Heuristics

class HeuristicInterface:

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