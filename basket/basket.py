def find_big_sets(basket): #builds sets, from big sets to small ones
    basket.sort()
    count = 0
    for i in range(len(basket)):
        basket[i] -= count
        count += basket[i]
    return basket

def prio_4sets(basket): #only works for THIS problem, combines sets of 3 and 5 to 2 sets of 4
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

def calculate_price(basket, discounts): # calculates price from given set_basket and discounts
    assert len(basket) == len(discounts), \
            "#discounts and #distinct books have to match"
    ret = 0
    for i in range(len(basket)):
        ret += basket[i] * (1-discounts[-(i+1)]) * (len(basket)-i)
    return ret

def find_prio_basket(discounts):
    max = 0
    max_index = -1
    for i in range(1, len(discounts)):
        if discounts[i] - discounts[i-1] > max:
            max = discounts[i] - discounts[i-1]
            max_index = i+1
    assert max_index > 0, \
           "failed to get a suitable max_index"
    return max_index

def prio_sets(prio, basket):
    if prio == len(basket):
        return basket
    if basket[-prio-1] != 0 and basket[-prio+1] !=0:
        if basket[-prio+1] < basket[-prio-1]:
            basket[-prio] += 2 * basket[-prio+1]
            basket[-prio-1] -= basket[-prio+1]
            basket[-prio+1] = 0
        else:
            basket[-prio] += 2 * basket[-prio-1]
            basket[-prio+1] -= basket[-prio-1]
            basket[-prio-1] = 0
    return basket




def solve(basket, discounts, base_price): #solves whole problem using 3 functions above
    basket = find_big_sets(basket)
    basket = prio_sets(find_prio_basket(discounts), basket)
    print(basket)
    return calculate_price(basket, discounts) * base_price

if __name__ == "__main__":
    basket = [2, 2, 2, 1, 1]
    discounts = [0, 0.05, 0.1, 0.2, 0.25]
    base_price = 8

    print(solve(basket, discounts, base_price))
    print(find_prio_basket(discounts))