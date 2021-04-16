import pytest
from resolver.solver import *

def test_3x3_grid_correct():
    grid = fill_one_grid([1,2,3,4,0,6,7,8,9]);
    print(grid)
    assert grid == [1,2,3,4,5,6,7,8,9]