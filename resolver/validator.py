from resolver.divisor import *

def validate_value_in_grid(grid, cell, value):  
    result = validate_value_in_cell(grid, cell, value)
    
    if result == True:
        result = validate_value_in_horizontal_row(grid, cell, value)
        if result == True:
            result = validate_value_in_vertical_row(grid, cell, value)
    
    return result

def validate_value_in_cell(grid, cell, value):
    values_used_in_cell = dict({1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0})

    parent_grid_cell = [cell[0]//3*3, cell[1]//3*3]
    cell = grid_divisor(grid, parent_grid_cell[0], parent_grid_cell[1])

    for rows in cell:
        for number in rows:
            if number != 0:
                values_used_in_cell[number] = values_used_in_cell[number] + 1
    
    if(values_used_in_cell[value]==0): 
        return True
    return False

def validate_value_in_horizontal_row(grid, cell, value):
    values_used_in_horizontal_rows = dict({1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0})
    horizontal_row = grid_divisor_horizonal_row(grid, cell[0], cell[1])

    for number in horizontal_row:
        if number != 0:
            values_used_in_horizontal_rows[number] = values_used_in_horizontal_rows[number] + 1
    
    if(values_used_in_horizontal_rows[value]==0):
        return True
    return False

def validate_value_in_vertical_row(grid, cell, value):
    values_used_in_vertical_rows = dict({1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0})
    vertical_row = grid_divisor_vertical_row(grid, cell[0], cell[1])

    for number in vertical_row:
        if number != 0:
            values_used_in_vertical_rows[number] = values_used_in_vertical_rows[number] + 1
    
    if(values_used_in_vertical_rows[value]==0):
        return True
    return False