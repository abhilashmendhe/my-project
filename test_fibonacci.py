from fibonacci import fibonnaci


def test1():
    assert fibonnaci(1) == 0
    assert fibonnaci(2) == 1
    assert fibonnaci(3) == 1
    assert fibonnaci(4) == 2
    assert fibonnaci(5) == 3

def test2():
    assert fibonnaci(6) == 5
    assert fibonnaci(7) == 8
    assert fibonnaci(8) == 13
    assert fibonnaci(9) == 21
    assert fibonnaci(10) == 34

# def test3():
#     assert fibonnaci(10) == 12