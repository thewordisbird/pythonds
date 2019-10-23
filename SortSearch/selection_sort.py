# Implement selection sort

# Steps:
# 1. Set starting variable to track max position at 0
# 2. Iterate over list and check for highest number and set pos_max
# 3. Exchange num_max with num[-1] 
# 4. Repeate steps iterating to n -1

def selection_sort_i(nums):
    for i in range(len(nums), 0, -1):
        pos_max = 0
        for j in range(i):
            if nums[j] > nums[pos_max]:
                pos_max = j
        print(nums[pos_max])
        nums[pos_max], nums[i - 1] = nums[i - 1], nums[pos_max]
    return nums

def selection_sort_r(nums, n=None):
    if n == None:
        n = len(nums)
    if n == 0:
        return nums
    pos_max = 0
    for i in range(n):
        if nums[i] > nums[pos_max]:
            pos_max = i
    if pos_max > 0:
        nums[pos_max], nums[n] = nums[n], nums[pos_max]
    return selection_sort_r(nums, n - 1)
    




if __name__ == '__main__':
    print(selection_sort_i([0, -6, 3, 2, 1]))
    print(selection_sort_r([0, -6, 3, 2, 1]))
    
