def grid_divisor(input_grid, cell_row, cell_column):
        cell_row = cell_row//3 * 3
        cell_column = cell_column//3 * 3    
        
        cell = [[input_grid[cell_row][cell_column], input_grid[cell_row][cell_column + 1], input_grid[cell_row][cell_column+2]],
            [input_grid[cell_row + 1][cell_column], input_grid[cell_row + 1][cell_column + 1], input_grid[cell_row + 1][cell_column + 2]],
            [input_grid[cell_row + 2][cell_column], input_grid[cell_row + 2][cell_column + 1], input_grid[cell_row + 2][cell_column + 2]]]       
        
        return cell


def grid_divisor_horizonal_row(input_grid, cell_row, cell_column):
        row_data = []
        for number in input_grid[cell_row]:
                row_data.append(number)

        return row_data

def grid_divisor_vertical_row(input_grid, cell_row, cell_column):
        row_data = []
        for row in input_grid:
                row_data.append(row[cell_column])

        return row_data