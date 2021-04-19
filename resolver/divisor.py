def grid_divisor(input_grid, cell_row, cell_column):
    cell_row = cell_row*3
    cell_column = cell_column*3    

    cell = [[input_grid[cell_row][cell_column], input_grid[cell_row][cell_column + 1], input_grid[cell_row][cell_column+2]],
            [input_grid[cell_row + 1][cell_column], input_grid[cell_row + 1][cell_column + 1], input_grid[cell_row + 1][cell_column + 2]],
            [input_grid[cell_row + 2][cell_column], input_grid[cell_row + 2][cell_column + 1], input_grid[cell_row + 2][cell_column + 2]]]   
    return cell
