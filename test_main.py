'''
 * @author Anh Huy Nguyen
 * */
'''
# Fife for testing function in main FILE. 

import pytest
from main import add_binary, minus_binary
from function import _is_valid

def test_is_valid():
    a = '101011'
    b = 'abcdef'
    assert _is_valid(a) == True
    assert _is_valid(b) == False

def test_add_binary():
    x = '11010010'
    y='10010001'
    assert add_binary(x, y) == '101100011'

def test_minus_binary():
    x = '110111011101001'
    y = '11110110'
    assert minus_binary(x,y) == '110110111110011'

def test_minus_binary_negative():
    x ='101001'
    y = '110100'
    assert minus_binary(x,y) == '-1011'

def test_minus_binary_negative_1():
    x ='100000010001000111000000000100000101000000010010110001110000010'
    y = '1100100011000110010110000100010001111000011100011000111110011'
    assert minus_binary(x,y) == '10011101110000000101001111111110011000111110110011000110001111'