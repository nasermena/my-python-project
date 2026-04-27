from helper import add_numbers, multiply_numbers, subtract_numbers

def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(0, 0) == 0
    assert add_numbers(-1, 1) == 0

def test_multiply_numbers():
    assert multiply_numbers(2, 3) == 6
    assert multiply_numbers(0, 5) == 0
    assert multiply_numbers(-2, 3) == -6

def test_subtract_numbers():
    assert subtract_numbers(5, 3) == 2
    assert subtract_numbers(0, 0) == 0
    assert subtract_numbers(3, 5) == -2