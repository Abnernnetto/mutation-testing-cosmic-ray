from src.calculator import add, subtract, is_positive

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 3) == 2

def test_is_positive():
    assert is_positive(10) is True