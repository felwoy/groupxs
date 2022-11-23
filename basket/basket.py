def find_big_sets(basket):
    basket.sort()
    count = 0
    for i in range(len(basket)):
        basket[i] -= count
        count += basket[i]
    return basket

def prio_4sets(basket): #only works for this problem
    if basket[2] != 0 and basket[0] != 0:
        if basket[2] < basket[0]:
            basket[1] += 2*basket[2]
            basket[0] -= basket[2]
            basket[2] = 0
        else:
            basket[1] += 2*basket[0]
            basket[2] -= basket[0]
            basket[0] = 0
    return basket

def calculate_price(basket, discounts):
    assert len(basket) == len(discounts)
    ret = 0
    for i in range(len(basket)):
        ret += basket[i] * (1-discounts[-(i+1)]) * (5-i)
    return ret

def solve(basket, discounts, base_price):
    basket = find_big_sets(basket)
    basket = prio_4sets(basket)

    return calculate_price(basket, discounts) * base_price

if __name__ == "__main__":
    basket = [2, 2, 2, 1, 1]
    discounts = [0, 0.05, 0.1, 0.2, 0.25]
    base_price = 8

    print(solve(basket, discounts, base_price))