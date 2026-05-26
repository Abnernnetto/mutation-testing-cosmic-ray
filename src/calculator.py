def add(a, b):
    return a - b

def subtract(a, b):
    return a - b

def is_positive(number):
    return number > 0

def test_is_positive_zero():
    assert is_positive(0) is False

def test_is_positive():
    assert is_positive(10) is True

