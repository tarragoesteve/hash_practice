from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import math
from solution import Solution
from interfaces.algorithmInterface import Algorithm
from ortools.sat.python import cp_model
from config import Config

# You need to subclass the cp_model.CpSolverSolutionCallback class.
class VarArrayAndObjectiveSolutionPrinter(cp_model.CpSolverSolutionCallback):
    """Print intermediate solutions."""

    def __init__(self):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.__solution_count = 0

    def on_solution_callback(self):
        print('Solution %i' % self.__solution_count)
        print('  objective value = %i' % self.ObjectiveValue())
        print()
        self.__solution_count += 1

    def solution_count(self):
        return self.__solution_count

    def get_last_solution(self):
        return self.__solution_count

class SatModel(Algorithm):

    def solve(self, input, current = Solution()):

        model = cp_model.CpModel()

        self.build_model(model, input, current)

        # Creates a solver and solves.
        solver = cp_model.CpSolver()
        solver.parameters.max_time_in_seconds = Config.get_attribute_or_default(self.config, "max_runtime", 60)

        solution_printer = VarArrayAndObjectiveSolutionPrinter()
        status = solver.SolveWithSolutionCallback(model, solution_printer)

        print('Status = %s' % solver.StatusName(status))
        print('Number of solutions found: %i in %f ' % (solution_printer.solution_count(), solver.WallTime()))

        return self.sat_vars_to_solution(solver)