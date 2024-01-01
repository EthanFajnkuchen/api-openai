def test_even_odd():
    assert even_odd(2) == "Even"
    assert even_odd(3) == "Odd"
    assert even_odd(0) == "Even"
    assert even_odd(987654321) == "Odd"
    assert even_odd(-4) == "Even"

def even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

test_even_odd()