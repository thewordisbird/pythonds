# Implement Bubble Sort

# The bubble sort makes multiple passes through a list. It compares adjacent items and exchanges those that are out of order. 
# Each pass through the list places the next largest value in its proper place. In essence, each item “bubbles” up to the location where it belongs.

# Recursive implementation of bubble sort
def bubble_sort_r(nums, n=None):
    if n == None:
        n = len(nums) - 1
    if n == 1:
        return nums
    else:
        exchange = False
        for i in range(n):
            if nums[i] > nums[i + 1]:
                exchange = True
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
        if exchange == False:
            return nums
        else:
            return bubble_sort_r(nums, n - 1)

# Iterative implementation of bubble sort
def bubble_sort_i(nums):
    for i in range(len(nums) - 1, 0 , -1):
        exchange = False
        for j in range(i):
            if nums[j] > nums[j + 1]:
                exchange = True
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
        if exchange == False:
            return nums

    return nums


if __name__ == '__main__':
    print(bubble_sort_r([2, 1, 3, 4]))
    print(bubble_sort_i([1, 2, 4, 3]))