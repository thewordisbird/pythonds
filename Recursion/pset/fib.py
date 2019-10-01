import timeit

# Write a recursive function to compute the Fibonacci sequence. How does the performance of the recursive function compare to that of an iterative version?

def rec_fib(n):
    if n == 0:
        f = 0
    elif n == 1:
        f = 1
    else:
        f =  rec_fib(n - 1) + rec_fib(n - 2)
    return f

def iter_fib(n):
    fib = fib_m1 = fib_m2 = 0
    for i in range(n + 1):
        if i == 0:
            fib = 0
        if i == 1:
            fib =1
        else:
            fib = fib_m1 + fib_m2
        
        fib_m2 = fib_m1
        fib_m1 = fib
    return fib

memo = {}
def memo_fib(n):
    if n in memo.keys():
        return memo[n]
    else:
        if n == 0:
            f = 0
        elif n == 1:
            f = 1
        else:        
            f = rec_fib(n - 1) + rec_fib(n - 2)
        memo[n] = f
    return f
        


if __name__ == '__main__':
    for i in range(15):
        print(i ,rec_fib(i))
    
    for i in range(15):
        print(i ,iter_fib(i))
    
    for i in range(15):
        print(i ,memo_fib(i))

    t1 = timeit.Timer("rec_fib(20)", "from __main__ import rec_fib")
    rec_fib_time = t1.timeit(number=1000)
    print(rec_fib_time)
    # Average time of 1000 runs for fib 20 took 3.69 seconds

    t2 = timeit.Timer("iter_fib(20)", "from __main__ import iter_fib")
    iter_fib_time = t2.timeit(number=1000)
    print(iter_fib_time)
    # Average time of 100 runs for fib 20 too 0.0036 seconds

    t3 = timeit.Timer("memo_fib(20)", "from __main__ import memo_fib")
    memo_fib_time = t3.timeit(number=1000)
    print(memo_fib_time)
    # Average time of 100 runs for fib 20 too 0.0054 seconds