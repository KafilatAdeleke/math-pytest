from math_script import add_numbers, multiply_numbers

def test_add_numbers():
    result = add_numbers(2, 3)
    assert result == 5

def test_add_numbers_negative():
    result = add_numbers(-2, 3)
    assert result == 1

def test_add_numbers_float():
    result = add_numbers(2.5, 3.5)
    assert result == 6.0

def test_multiply_numbers():
    result = multiply_numbers(2, 3)
    assert result == 6

def test_multiply_numbers_negative():
    result = multiply_numbers(-2, 3)
    assert result == -6

def test_multiply_numbers_float():
    result = multiply_numbers(2.5, 3)
    assert result == 7.5
