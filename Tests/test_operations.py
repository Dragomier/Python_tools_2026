from math import isclose
import pytest

def mask_sum(data, mask):
    res = 0
    for val, mask_val in zip(data, mask):
       if mask_val != 0:
            res += val
    return res

def test_empty():
    assert mask_sum([], [0]) == 0

def test_zero():
    assert mask_sum([5,1,7], [0,0,0]) == 0

def test_ones():
    assert mask_sum([2,1,3,7], [1,1,1,1]) == 13

def mixed():
    assert mask_sum([2,3], [0, 1]) == 3