def combinations(n, k, combos=set(), i=0):
    if len(n) == k:
        combos.add(n)
    elif i < len(n):
        # recurse including char at i
        combinations(n, k, combos, i+1)
        # recurse excluding char at i
        combinations(n[0:i] + n[i+1::], k, combos, i)
    return combos



if __name__ == '__main__':
    n = '12345'
    k = 3
    print(combinations(n, k))