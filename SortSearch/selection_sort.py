# Implement selection sort

# Description
# The selection sort improves on the bubble sort by making only one exchange for every pass through the list. 
# In order to do this, a selection sort looks for the largest value as it makes a pass and, after completing the pass, 
# places it in the proper location. As with a bubble sort, after the first pass, the largest item is in the correct place. 
# After the second pass, the next largest is in place. This process continues and requires n−1 passes to sort n items, 
# since the final item must be in place after the (n−1) st pass.


# Steps:
# 1. Set starting variable to track max position at 0
# 2. Iterate over list and check for highest number and set pos_max
# 3. Exchange num_max with num[-1] 
# 4. Repeate steps iterating to n -1

# Iterative implementation of selection sort
def selection_sort_i(nums):
    for i in range(len(nums), 0, -1):
        pos_max = 0
        for j in range(i):
            if nums[j] > nums[pos_max]:
                pos_max = j
        nums[pos_max], nums[i - 1] = nums[i - 1], nums[pos_max]
    return nums

# Recursive implementation of selection sort
def selection_sort_r(nums, n=None):
    # Set length of nums on first call
    if n == None:
        n = len(nums)
    
    # Base case, we have recursed through the list and everything is sorted. Return the sorted list
    if n == 0:
        return nums
    else:
        pos_max = 0 # Position of the maximum value
        for i in range(n):
            if nums[i] > nums[pos_max]:
                pos_max = i        
        # Exchange the maximum value to the n - 1th position
        nums[pos_max], nums[n - 1] = nums[n - 1], nums[pos_max]

        # Return is used to pass the solution at n = 0 up as the call stack is poped
        return selection_sort_r(nums, n - 1)
    

if __name__ == '__main__':
    print(selection_sort_i([0, -6, 3, 2, 1]))
    print(selection_sort_r([0, -6, 3, 2, 1]))
    
