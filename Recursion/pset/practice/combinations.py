# Given an array of size n, generate and print all possible combinations of k elements in array. 
# For example, if input array is {1, 2, 3, 4} and k is 2, then output should be 
# {1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4} and {3, 4}.

# Notes:
# This problem is similar to finding all substrings. For each recursion you either include the character at i or exclude it
# The character is added to the set when the length of the string is equal to the size of the combinations, k
# Because the base case doesn't stop the function from recursing further as it doesn't set any restrictions on i
# we need to include an exit case. In this case if i >= to len(n) the recursions are skipped and the set to that 
# point is returned

# This solution has a time complexity of O()

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