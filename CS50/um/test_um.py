from um import count

def test_default():
    assert(count("um"))== 1

def test_default1():
    assert(count("Um, thanks for the album"))==1

def test_default_2():
    assert(count("Um, thanks, um..")) ==2

def test_default_none():
    assert(count("hi,how are you")) == 0
