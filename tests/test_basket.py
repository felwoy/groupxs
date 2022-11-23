from basket.basket import *

# basic test to prove the given example is fullfilled, since that's the only verified solution
# could have been done via unittest as well
def test_basket():
    assert solve([2, 2, 2, 1, 1], [0, 0.05, 0.1, 0.2, 0.25], 8) == 51.2, \
            "example was not fulfilled"

    
# test that no books get lost by building sets, could do similar tests for all functions
def test_setfinding():
    basket = [3, 4, 2, 1, 1]
    basket_total = 11
    ret = find_big_sets(basket)
    ret_total  = 0
    for i in range(len(ret)):
        ret_total += (len(ret) - i) * ret[i]
    assert ret_total == basket_total, \
            "lost or found books during set_building"
#### place for more tests, noticed there is a lot more in testing to do



if __name__ == '__main__':
    test_basket()
    print("example test passed")
    test_setfinding()
    print("set building test passed")
