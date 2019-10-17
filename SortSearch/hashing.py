# Implementation of the Map abstract data type for storing data in a hash table

# Implemented without collision allows for search in constant time O(1)

# There are many hashing function that are far more complex than the ones used in this
# exercise to reduce the chance of collisions.

# This data type exists optimized in python in the form of a dictinoary. 


# Hashing functions:
# The goal with hashing functions is to create the minimal number of colisions
# while still being easy to compute and will evenly distribute the items in the hash table
def remainder_hash(size, item):
    '''Remainder method. Divide item by table size and return remainder.'''
    return item % size

def folding_hash(size, item, group=2):
    '''Folding method. Divides the item into equal sized pieces (default = 2) and 
        adds together the pieces to get the hash value. This is then processed
        with the remainder method to get the slot.'''
    # Split digits
    digits=[]
    while item > 0:
        digits.append(item%10)
        item = item // 10
    print(digits)
    # Create groups
    groups=[]
    for i in range(0, len(digits), group):
        n = 0
        for p in range(group):
            if i + p < len(digits):
                n += digits[i + p] * (10**p)
            else:
                break
            
        groups.append(n)
    print(groups)
    # Sum groups
    group_sum = sum(groups)
    # Return slot
    return group_sum % size


def mid_square_hash(size, item):
    '''Mid-Square Method. Square the item then extract th middle portion to perform
        the remainder method on.'''
    # Square item
    item_squared = item ** 2

    # Split digits
    digits = []
    while item_squared > 0:
        digits.append(item_squared%10)
        item_squared = item_squared // 10
    print(digits)
    # find mid digits
    len_digits = len(digits)
    half_digits = len_digits//2
    mid_range_start = half_digits //2
    print(len_digits, half_digits, mid_range_start)
    # We don't have to reverse this since the digits are stored in reverse order
    mid_val = 0      
    i = 0
    for p in range(half_digits):
        mid_val += digits[mid_range_start + i] * (10**p)
        i += 1
    # Return slot

    print(mid_val)
    return mid_val % size


def rehash(hash, size):
    return (hash + 1) % size
# Helper Function to convert string to a number
def convert_string(s):
    '''Returns a position weighted sum or unicode values of characters. This
        prevents anagram collisions'''
    string_sum = 0
    for i,c in enumerate(s):
        string_sum += (ord(c) * (i + 1))
    return string_sum

# Other functions of note
def load_factor(length, items):
    '''The amount of the hash table that is occupide.'''
    return items/length

class Map:
    '''Map abstract data structure. This will use the remainder hashing method'''
    def __init__(self, size):
        self.size = size
        self.slots = [None for x in range(self.size)]
        self.data = [None for x in range(self.size)]

    def put(self, key, val):
        slot = hash_1(self.size, key)
        if self.slots[slot] is None:
            self.slot[slot] = key
            self.data[slot] = val
        elif self.slot[slot] == key:
            self.data[slot] = val
        else:
            next_slot = rehash(slot, self.size)
            while self.slots[next_slot] != None and self.slots[next_slot] != key:
                next_slot = rehash(next_slot, self.size)
            if self.slots[next_slot] == None:
                self.slots[next_slot] = key
                self.data[next_slot] = val
            else:
                self.data[next_slot] = data

    def get(self, key):
        slot = hash_1(self.size, key)
        if self.slots[slot] == key:
            return self.data[slot]
        elif self.slots[slot] == None:
            return None
        else:
            next_slot = rehash(slot, self.size)
            while self.slots[next_slot] != key and next_slot != slot:
                if self.slots[next_slot] == key:
                    return self.data[next_slot]
                else:
                    next_slot = rehash[next_slot, self.size]
            return None


