from plates import is_valid
def test_CS50():
    assert is_valid("CS50") == True

def test_CS0P():
    assert is_valid("CS0P") == False
    assert is_valid("CS50P") == False
    assert is_valid("CS05") == False
    assert is_valid("CS50CS") == False

def test_mix():
    assert is_valid("PI3.14") == False

def test_nu():
    assert is_valid("50") == False

def test_n():
    assert is_valid("a") == False
