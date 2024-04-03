'''
 * @author Anh Huy Nguyen
 * */
'''
# Fife for testing logical functions in the function FILE.  

import pytest

from function import  CARRY_BIT, BORROW_BIT, LESS_THAN
TRUTH_TABLE = [[0,0,0],[0,0,1],[0,1,0],[0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,1]]

def test_carry_bit():
    result = [int(CARRY_BIT(*i)) for i in TRUTH_TABLE]
    assert result[0] == 0
    assert result[1] == 0
    assert result[2] == 0
    assert result[3] == 1
    assert result[4] == 0
    assert result[5] == 1
    assert result[6] == 1
    assert result[7] == 1

def test_borrow_bit():
    result = [int(BORROW_BIT(i[1],i[2],i[0]))for i in TRUTH_TABLE]
    assert result[0] == 0
    assert result[1] == 1
    assert result[2] == 0
    assert result[3] == 0
    assert result[4] == 1
    assert result[5] == 1
    assert result[6] == 0
    assert result[7] == 1

def test_less_than():
    result = [int(LESS_THAN(i[1],i[2],i[0])) for i in TRUTH_TABLE]
    assert result[0] == 0
    assert result[1] == 1
    assert result[2] == 0
    assert result[3] == 0
    assert result[4] == 1
    assert result[5] == 1
    assert result[6] == 0
    assert result[7] == 1