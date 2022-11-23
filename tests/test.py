from basket.basket import *

def test_basket():
    assert solve([2, 2, 2, 1, 1], [0, 0.05, 0.1, 0.2, 0.25], 8) == 51.2, \
            "basic logic/math failed"

#### place for more tests, noticed that I should probably know more about testing



if __name__ == '__main__':
    test_basket()
    print("test passed")