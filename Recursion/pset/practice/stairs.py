def climbStairs_rec(n, i=0):
    if n == 0:
        i += 1
    elif n > 1:
        climbStairs(n-2, i)
        climbStairs(n-1, i)
    else:
        climbStairs(n-1, i)
    return i

def climbStairs_dp(n, cache={}):
    if n in cache.keys():
        return cache[n]
    if n < 3:
        result = n
    else:
        result = climbStairs(n-1) + climbStairs(n-2)  
    cache[n] = result
    return result  

def climbStairs_x_dp(n, steps, cache={}):
    '''Generalized solution for any variations of allowable steps.
        min step val must be greater or equal to n'''
    if n in cache.keys():
        return cache[n]
    if n == 0:
        return 1
    
    result = 0
    for step in steps:
        #print(step,n)
        if n >= step:
            result += climbStairs_x_dp(n - step, steps)
    cache[n] = result
    return result

if __name__ == '__main__':
    n = 1
    x = [2]
    #print(climbStairs(n))
    print(climbStairs_x_dp(n, x))
    