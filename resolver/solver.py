from resolver.divisor import *
from resolver.validator import *

def fill_one_grid(input_grid):   
    values_dict = set_grid_status(input_grid)
    values_to_fill = find_not_used_values(values_dict)

    value_to_fill = 0
    for index in range(len(input_grid)):
        if input_grid[index] == 0:
            input_grid[index] = values_to_fill[value_to_fill]
            value_to_fill = value_to_fill + 1

    print(input_grid)
    return input_grid

def find_empty_cells(grid):
    for row_number in range(len(grid)):
        for column_number in range(len(grid[row_number])):
            if(grid[row_number][column_number] == 0):
                values = get_values_to_cell(grid, [row_number, column_number])
                for value in values:
                    if(validate_value_in_grid(grid, [row_number, column_number], value)==True):
                        grid[row_number][column_number] = value
    return grid

def get_values_to_cell(grid, position):
        cell = grid_divisor(grid, position[0], position[1])
        used_values = set_grid_status(cell)
        clear_values = find_not_used_values(used_values)
        return clear_values

def set_grid_status(input_grid):
    values_dict = dict({1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0})
    for row in input_grid:
            for number in row:
                if number != 0:
                    values_dict[number] = 1
    return values_dict

def find_not_used_values(values_dict):
    values_to_fill=[]
    for value in values_dict.items():
        if value[1] == 0:
            values_to_fill.append(value[0])
    return values_to_fill