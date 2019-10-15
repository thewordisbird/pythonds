# Implementation of Sequential Seach

# Sequential Search: Iterate through items of list until the item is found (return True) or the end of the list is reached (return False).
# If the list is sorted iteration for a value can stop once the value at index i is greater than the value being searched for

# Time complexity is O(n) for either option, though on a sorted list it could perform slightly faster. 
# Note, optimal sorting algorithms run O(nlogn) so the total time complexity would be O(nlogn)


def sequential_search(items, val):
    for item in items:
        if item == val:
            return True
    return False


# This implementation would require a helper function to sum the ascii value of the val word and the item word to see if the value is greater
def sequential_search_sorted(items,val):
    '''Only works if list is sorted.'''
    for item in items:
        if item == val:
            return True
        elif item > val:
            return False
    return False

if __name__ == '__main__':
    items = [54, 26, 93, 17, 77, 31, 44, 55, 20, 65]
    print(sequential_search(items, 3))
    print(sequential_search(items, 93)) 

    # Sort Items
    items.sort()
    print(sequential_search_sorted(items, 3))
    print(sequential_search_sorted(items, 93)) 