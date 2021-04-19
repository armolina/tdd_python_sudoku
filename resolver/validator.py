from resolver.divisor import *
from resolver.solver import *

def validator(grid, cell):  

    parent_grid_cell = [int(cell[0]/3), int(cell[1]/3)]
    value = grid[cell[0]][cell[1]]

    result = validate_value_in_cell(grid, cell, value)
    return result

def validate_value_in_cell(grid, cell, value):
    parent_grid_cell = [int(cell[0]/3), int(cell[1]/3)]
    cell = grid_divisor(grid, parent_grid_cell[0], parent_grid_cell[1])
    grid_status= set_grid_status(cell)

    print(grid_status)

    return True

def validate_value_in_row(grid, value):
    return True