import pytest
from resolver.solver import *

def test_3x3_1_valor_vacio_grid_correct():
    grid = fill_one_grid([1,2,3,4,0,6,7,8,9]);
    assert grid == [1,2,3,4,5,6,7,8,9]

def test_3x3_2_valor_vacio_grid_correct():
    grid = fill_one_grid([1,2,3,4,0,6,7,8,0]);
    assert grid == [1,2,3,4,5,6,7,8,9]

def test_3x3_5_valor_vacio_grid_correct():
    grid = fill_one_grid([0,2,0,4,0,6,0,8,0]);
    assert grid == [1,2,3,4,5,6,7,8,9]