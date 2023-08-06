from GenerativeMusic import square


def test_square():
    res = square.square(10)
    assert res == 100
