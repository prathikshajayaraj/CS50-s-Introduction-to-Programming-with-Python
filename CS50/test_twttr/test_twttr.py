from twttr import shorten

def test_hello():
    assert shorten("hello, world") == "hll, wrld"

def test_upper():
    assert shorten("HOW IS LIFE?") == "HW S LF?"

def test_number():
    assert shorten("CS50") =="CS50"

def test_uplow():
    assert shorten("hAppy to see you!!")== "hppy t s y!!"

