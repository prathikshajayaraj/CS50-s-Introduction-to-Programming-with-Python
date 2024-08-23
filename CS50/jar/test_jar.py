from jar import Jar
import pytest


def test_init():
       j=Jar(12)
       assert j.capacity==12


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size ==5
    jar.deposit(7)
    assert jar.size==12
    with pytest.raises(ValueError):
        jar.deposit(1)



def test_withdraw():
    jar = Jar()
    jar.deposit(9)
    jar.withdraw(4)
    assert jar.size ==5
    jar.withdraw(5)
    assert jar.size==0
    with pytest.raises(ValueError):
        jar.withdraw(1)
    