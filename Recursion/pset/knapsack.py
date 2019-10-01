# Suppose you are a computer scientist/art thief who has broken into a major art gallery. 
# All you have with you to haul out your stolen art is your knapsack which only holds W pounds 
# of art, but for every piece of art you know its value and its weight. Write a dynamic programming 
# function to help you maximize your profit. Here is a sample problem for you to use to get started: 
# Suppose your knapsack can hold a total weight of 20. You have 5 items as follows:

# item     weight      value
#   1        2           3
#   2        3           4
#   3        4           8
#   4        5           8
#   5        9          10

# Solving Dynamic Programing problems:
# 1. Determine the sub problem:
#       The subproblem in the knapsack problem is looking at the suffixes
# 2. Start with a guess:
#       The item is or is not in the subset
# 3. Determine recurrance:

def knapsack_rec(W, wt, val, n):
    '''determines maximum combination of items n based on their
    value val and weight wt to maximize filling a bag with weight capacity W'''

    # Base cases:
    # 1. There are no items
    # 2. There is no capacity
    if n == 0 or W == 0:
        return 0

    # If weight of the nth item is more than the knapsack of capacity W,
    # then this item cannot be included in the optimal solution
    if(wt[n-1] > W):
        return knapsack_rec(W, wt, val, n-1)
    
    # Return the maximum of two cases:
    # 1. nth item included
    # 2. nth item not included
    else:
        return max(val[n-1] + knapsack_rec(W-wt[n-1], wt, val, n-1), knapsack_rec(W, wt, val, n-1))

# 4. Add memoization:
#   a. memoization with temp array in bottom up manner
def knapsack_a(w, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]

    # Build table K from the bottom up
    for row in range(n + 1):
        for col in range(W + 1):
            # Does the item fit?
            if row == 0 or col == 0:
                K[row][col] = 0
            elif wt[row - 1] <= col:
                K[row][col] = max(val[row - 1] + K[row - 1][col - wt[row - 1]], K[row - 1][col])
            else:
                K[row][col] = K[row - 1][col]
    return K[n][W]

#
if __name__ == '__main__':
    W = 20
    val = [3, 4, 8, 8, 10]
    wt = [2, 3, 4, 5, 9]
    n = len(val)
    print(knapsack_rec(W, wt, val, n))
    print(knapsack_a(W, wt, val, n))