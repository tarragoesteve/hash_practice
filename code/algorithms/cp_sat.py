from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import math

from ortools.sat.python import cp_model

def build_model(self, model, input, current):

    # input
    input_matrix = []
    columns = 0
    rows = 0
    min_ingredients = 0
    max_pieces = 0

    max_num_squares = math.ceil(rows*columns/(min_ingredients * 4))

    #Here
    areas = []
    x_sizes = []
    y_sizes = []
    x_intervals = []
    y_intervals = []
    x_starts = []
    x_ends = []
    y_starts = []
    y_ends = []
    optionals = []
    multiple_mushrooms = []
    multiple_tomatoes = []

    # Creates intervals for the NoOverlap2D and size variables.
    for i in range(max_num_squares):
        optional = model.NewBoolVar('option_%i' % i)

        size_x = model.NewIntVar(0, max_pieces, 'size_x_%i' % i)
        size_y = model.NewIntVar(0, max_pieces, 'size_y_%i' % i)
        
        start_x = model.NewIntVar(0, rows, 'sx_%i' % i)
        end_x = model.NewIntVar(0, rows, 'ex_%i' % i)
        
        start_y = model.NewIntVar(0, columns, 'sy_%i' % i)
        end_y = model.NewIntVar(0, columns, 'ey_%i' % i)

        interval_x = model.NewOptionalIntervalVar(start_x, size_x, end_x, optional, 'ix_%i' % i)
        interval_y = model.NewOptionalIntervalVar(start_y, size_y, end_y, optional, 'iy_%i' % i)

        # calculate the area variable
        area = model.NewIntVar(0, max_pieces, 'area_%i' % i)
        model.AddProdEquality(area, [size_x, size_y])
        model.Add(area == 0).OnlyEnforceIf(optional.Not())

        # calculate the ammount of ingredients it has and force greater than the minimum
        tomatoes = []
        mushrooms = []

        for ii in range(rows):
            for ji in range(columns):
                b = model.NewBoolVar('b_%i_%i_%i' % (i, ii, ji))
                model.Add(ii >= start_x).OnlyEnforceIf(b)
                model.Add(ii < end_x).OnlyEnforceIf(b)
                model.Add(ji >= start_y).OnlyEnforceIf(b)
                model.Add(ji < end_y).OnlyEnforceIf(b)
                model.Add(b == 0).OnlyEnforceIf(optional.Not())
                if input_matrix[ii][ji] == "T":
                    mushrooms.append(b)
                elif input_matrix[ii][ji] == "M":
                    tomatoes.append(b)

        model.Add(sum(mushrooms) >= min_ingredients).OnlyEnforceIf(optional)
        model.Add(sum(tomatoes) >= min_ingredients).OnlyEnforceIf(optional)

        areas.append(area)
        optionals.append(optional)
        x_intervals.append(interval_x)
        y_intervals.append(interval_y)
        x_sizes.append(size_x)
        y_sizes.append(size_y)
        x_starts.append(start_x)
        x_ends.append(end_x)
        y_starts.append(start_y)
        y_ends.append(end_y)
        multiple_mushrooms.append(tomatoes)
        multiple_tomatoes.append(mushrooms)

    # Main constraint.
    model.AddNoOverlap2D(x_intervals, y_intervals)

    # Symmetry breaking
    for i in range(max_num_squares - 1):
        model.Add(areas[i] <= areas[i + 1])
        model.Add(optionals[i] <= optionals[i + 1])

        # Define same to be true iff sizes[i] == sizes[i + 1]
        same = model.NewBoolVar('same_%i' %  i)
        model.Add(areas[i] == areas[i + 1]).OnlyEnforceIf(same)
        model.Add(areas[i] < areas[i + 1]).OnlyEnforceIf(same.Not())

        # Tie break with starts.
        model.Add(x_starts[i] <= x_starts[i + 1]).OnlyEnforceIf(same)
    

    # Optimize
    model.Maximize(sum(areas))