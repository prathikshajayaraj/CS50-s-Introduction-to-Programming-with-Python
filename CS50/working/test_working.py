from working import convert
import pytest

def test_default():
    assert convert("9 AM to 5 PM")=="09:00 to 17:00"

def test_default_1():
    assert convert("10:30 PM to 8 AM")=="22:30 to 08:00"
def test_default_2():
     assert convert("10 AM to 8:50 PM") =="10:00 to 20:50"

def test_str():
    with pytest.raises(ValueError):
        convert("9:60 AM to 12:60 PM")

def test_str2():
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")
