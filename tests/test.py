from basket.basket import *

# basic test to prove the given example is fullfilled, since that's the only verified solution
def test_basket():
    assert solve([2, 2, 2, 1, 1], [0, 0.05, 0.1, 0.2, 0.25], 8) == 51.2, \
            "basic logic/math failed"

#### place for more tests, noticed there is a lot more in testing to do



if __name__ == '__main__':
    test_basket()
    print("test passed")
