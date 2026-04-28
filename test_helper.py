from helper import add_numbers, divide_numbers, multiply_numbers, subtract_numbers

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

def test_divide_numbers():
    assert divide_numbers(6, 3) == 2
    assert divide_numbers(5, 2) == 2.5
    try:
        divide_numbers(5, 0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero"