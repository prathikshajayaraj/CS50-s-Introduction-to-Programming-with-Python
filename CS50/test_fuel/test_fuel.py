import pytest
from fuel import convert,gauge
def test_value1():
    assert gauge(convert("3/4")) == "75%"

def test_value2():
    assert gauge(convert("1/4")) == "25%"

def test_value_full():
    assert gauge(convert("4/4")) == "F"
    assert gauge(99) == "F"

def test_value_empty():
    assert gauge(convert("0/4")) == "E"
    assert gauge(1) == "E"

def test_zero():
    with pytest.raises(ZeroDivisionError):
        gauge(convert("4/0"))

def test_letter():
    with pytest.raises(ValueError):
        gauge(convert("three/four"))



