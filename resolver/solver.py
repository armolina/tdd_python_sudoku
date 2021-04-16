def fill_one_grid(input_grid):   
    values_dict = set_grid_status(input_grid)
    values_to_fill = find_not_used_values(values_dict)

    for index in range(len(input_grid)):
        if input_grid[index] == 0:
            input_grid[index] = values_to_fill[0]

    print(input_grid)
    return input_grid

def set_grid_status(input_grid):
    values_dict = dict({1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0})
    for number in input_grid:
        if number != 0:
            values_dict[number] = 1
    return values_dict

def find_not_used_values(values_dict):
    for value in values_dict.items():
        if value[1] == 0:
            return value