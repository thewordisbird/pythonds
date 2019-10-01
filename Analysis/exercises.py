import timeit
import random

# Devise an experiment to verify that the list index operator is O(1)
def list_index_time():
    l1 = list(range(1000))
    return l1[random.randint(0, len(l1)-1)]




# Devise an experiment to verify that get item and set item are O(1) for dictionaries.
def dict_get_time():
    d1 = {j:None for j in range(1000)}
    return d1.get(random.randint(0, len(d1)))

def dict_set_time():
    d2 = {}
    for i in range(100):
        d2.__setitem__(random.randint(0, len(d2)), None)
    
# Devise an experiment that compares the performance of the del operator on lists and dictionaries.
def list_del_time():
    for i in range(1000, 10001, 200):
        x = list[range(i)]
        t = timeit.Timer("del(x[random.randint(0,i)", "from __main__ import random, x")
        lst_time = t.timeit(number=1000)

# Given a list of numbers in random order, write an algorithm that works in O(nlog(n)) to find the kth smallest number in the list.
def kth_smallest_1(arr,k):
    arr.sort() # This is O(nlogn)
    return arr[k-1]


# Can you improve the algorithm from the previous problem to be linear? Explain.
def kth_smallest_2(arr, k):
    pass
    # This isn't possible




if __name__ == '__main__':
    t = int(input('Which test? '))
    if t == 1:
        t1 = timeit.Timer ("list_index_time()", "from __main__ import list_index_time")
        for i in range(1000):
            lst_time = t1.timeit(number=1000)
            print(lst_time)
    elif t == 2:
        t2 = timeit.Timer("dict_get_time()", "from __main__ import dict_get_time")
        for i in range(1000):
            dget_time = t2.timeit(number=1000)
            print(dget_time)
    elif t == 3:
        t3 = timeit.Timer("dict_set_time()", "from __main__ import dict_set_time")
        for i in range(1000):
            dset_time = t3.timeit(number=1000)
            print(dset_time)
    elif t == 4:
        for i in range(1000, 100001, 1000):
            l4 = list(range(i))
            t4 = timeit.Timer("del l4[random.randint(0, len(l4) - 1)]", "from __main__ import l4, random")
            print(t4.timeit(number=1000))
    elif t == 5:
        for i in range(1000, 100001, 1000):
            d5 = {j:None for j in range(i)}
            l5 = list(range(i))
            random.shuffle(l5)

            t5 = timeit.Timer("del d5[l5.pop()]", "from __main__ import d5, random, l5")
            print(t5.timeit(number=1000))

    elif t == 6:
        arr = [-1, 5,2,9,58,-54,100]
        k = 4
        print(kth_smallest_1(arr, k))

    else:
        pass
    

        