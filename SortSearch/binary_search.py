# Implementation of Binary Search

# Binary Search: Requires sorted list. Takes the list and compares the item at i = n//2 to the serached for item. 3 cases from this point
#   1. item = val => return True
#   2. val < item => reset bounds of items from 0 to old mid and re-search
#   3. val > item => reset bounds of items from old mid to n and re-search

# This can be implemented with iteration and recursion.

# Time complexity of the search process is O(log(n)), but keep in mind since the items will usually have to be sorted at a cost of O(nlogn) that becomes the time complexity

def binary_search_iter(items, val):
    left = 0
    right = len(items) - 1
    mid = (right + left) // 2

    while left <= right:
        if items[mid] == val:
            return True
        elif val < items[mid]:
            right = mid - 1
        else:
            left = mid + 1
        mid = (right + left) // 2
    return False

# This method is reccomended over slicing, because slicing has a time complexity O(k) which is larger than O(logn).
# By passing in the list with pointers, this is not the case and the time complexity stays O(logn)
def binary_search_rec(items, val, l=0, r=None):
    if r == None:
        r = len(items) - 1
    mid = (l + r) // 2
    if l > r:
        return False
    if val == items[mid]:
        return True
    elif val < items[mid]:
        return binary_search_rec(items, val, l, mid - 1)
    else:
        return binary_search_rec(items, val, mid + 1, r)

    


if __name__ == '__main__':
    items = [54, 26, 93, 17, 77, 31, 44, 55, 20, 65]

    # Sort items
    items.sort()
    print(binary_search_iter(items, 3))
    print(binary_search_iter(items, 55))
    print(binary_search_iter(items, 17))
    print(binary_search_iter(items, 93))

    print(binary_search_rec(items, 3))
    print(binary_search_rec(items, 55))
    print(binary_search_rec(items, 17))
    print(binary_search_rec(items, 93))
