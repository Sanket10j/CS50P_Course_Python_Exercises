from jar import Jar
import pytest

def test_init():
    jar = Jar(10)
    assert jar.capacity == 10

def test_str():
    jar = Jar(10)
    jar.deposit(2)
    assert str(jar) == '🍪🍪'

def test_deposit():
    jar = Jar(10)
    jar.deposit(3)
    assert jar.current_size == 3
    with pytest.raises(ValueError):
        jar.deposit(8)

def test_withdraw():
    jar = Jar(10)
    jar.withdraw(7)
    assert jar.current_size == 3
    with pytest.raises(ValueError):
        jar.withdraw(2)

if __name__ == "__main__":
    pytest.main()

