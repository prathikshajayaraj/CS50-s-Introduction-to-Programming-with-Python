from bank import value
def test_hello():
    assert value("Hello, Newman") == 0

def test_h():
    assert value("How you doing?") == 20

def test_no():
    assert value("What's happening?") == 100

def test_an():
    assert value("is that good day") == 100



    