import pytest
from numb3rs import validate

def test_default():
    assert validate("127.0.0.1") == True

def test_value2():
    assert validate("255.255.255.255") == True

def test_first_byte_only():
    assert validate("127.512.512.512") == False
    
def test_value3():
    assert validate("1.2.3.1000") == False

def test_value():
    assert validate("cat") == False
