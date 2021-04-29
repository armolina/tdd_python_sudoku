import pytest 
from resolver.validator import *
from resolver.solver import *

full_sudoku = [
        [5,3,4, 6,7,8, 9,1,2],
        [6,7,2, 1,9,5, 3,4,8],
        [1,9,8, 3,4,2, 5,6,7],
        
        [8,5,9, 7,6,1, 4,2,3],
        [4,2,6, 8,5,3, 7,9,1],
        [7,1,3, 9,2,4, 8,5,6],
        
        [9,6,1, 5,3,7, 2,8,4],
        [2,8,7, 4,1,9, 6,3,5],
        [3,4,5, 2,8,6, 1,7,9]
    ]

easy_sudoku_1 = [
        [5,0,4, 6,7,8, 9,1,2],
        [6,7,2, 1,9,5, 0,4,8],
        [1,9,8, 3,4,2, 5,6,7],
        
        [8,5,9, 7,6,1, 4,2,3],
        [4,2,6, 8,5,0, 7,9,1],
        [7,1,3, 9,2,4, 8,5,6],
        
        [9,6,0, 5,3,7, 2,8,4],
        [2,8,7, 4,1,9, 6,3,5],
        [3,4,5, 2,8,6, 1,7,9]
    ]

expert_sudoku_1 = [
        [0,9,0, 0,0,7, 0,0,0],
        [0,0,0, 0,0,0, 0,4,5],
        [7,0,0, 0,8,0, 0,0,6],
        
        [0,0,0, 0,0,5, 3,0,0],
        [0,8,0, 0,0,0, 0,0,9],
        [0,0,4, 9,0,0, 0,6,0],
        
        [5,0,1, 6,0,0, 0,0,0],
        [0,0,0, 0,4,0, 0,1,0],
        [0,0,0, 0,0,0, 2,5,7]
    ]

def test_fill_one_cell():
    find_empty_cells(easy_sudoku_1)
    assert empty_1_cell_sudoku == full_sudoku

def test_validate_some_correct_and_incorrect_values_in_expert_sudoku():
    assert validate_value_in_grid(expert_sudoku_1, [0,0], 1)==True
    assert validate_value_in_grid(expert_sudoku_1, [0,0], 7)==False
    assert validate_value_in_grid(expert_sudoku_1, [0,0], 5)==False
    assert validate_value_in_grid(expert_sudoku_1, [4,3], 1)==True

def test_resolve_easy_sudoku():
    resolve = find_empty_cells(easy_sudoku_1)
    print(resolve)
    assert True==False

def test_resolve_expert_sudoku():
    resolve = find_empty_cells(expert_sudoku_1)
    print(resolve)
    assert True==False