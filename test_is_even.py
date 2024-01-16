def test_is_even():
    assert is_even(2) == True
    assert is_even(3) == False
    assert is_even(4) == True
    assert is_even(5) == False

def is_even(num):
    return (num % 2 == 0)