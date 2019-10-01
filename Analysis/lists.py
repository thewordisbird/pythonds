from timeit import Timer

def test1():
    l = []
    for i in range(1000):
        l = l + [i]


def test2():
    l = []
    for i in range(1000):
        l.append(i)
    
def test3():
    l = [i for i in range(1000)]

def test4():
    l = list(range(1000))

popzero = Timer("x.pop(0)", "from __main__ import x")
popend = Timer("x.pop()", "from __main__ import x")


if __name__ == '__main__':
    # Compare pop speed of pop(0) vs pop()
    x = list(range(2000000))
    print("pop(0)", popzero.timeit(number=1000))

    x = list(range(2000000))
    print("pop()", popend.timeit(number=1000))

    # Confirm pop(0) is O(n) and pop() is O(1)
    for i in range(1000000,100000001,1000000):
        x = list(range(i))
        pt = popend.timeit(number=1000)
        x = list(range(i))
        pz = popzero.timeit(number=1000)
        print(f'{pz}, {pt}')




    t1 = Timer ("test1()", "from __main__ import test1")
    print("concat", t1.timeit(number=1000), "milliseconds")

    t2 = Timer ("test2()", "from __main__ import test2")
    print("append", t2.timeit(number=1000), "milliseconds")

    t3 = Timer ("test3()", "from __main__ import test3")
    print("comprehension", t3.timeit(number=1000), "milliseconds")

    t4 = Timer ("test4()", "from __main__ import test4")
    print("list(range())", t4.timeit(number=1000), "milliseconds")
