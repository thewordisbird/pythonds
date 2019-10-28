# Implementation of insertion sort.

# The insertion sort, although still O(n2), works in a slightly different way. 
# It always maintains a sorted sublist in the lower positions of the list. 
# Each new item is then “inserted” back into the previous sublist such that the sorted sublist is one item larger. 

# Steps:
# 1. 
#
#
#
#

# Using while loop
def insertion_sort(nums):
    for i in range(1, len(nums)):
        value = nums[i]
        insert_pos = i

        while insert_pos > 0 and nums[insert_pos - 1] > value:
            nums[insert_pos] = nums[insert_pos - 1]
            insert_pos = insert_pos - 1

        nums[insert_pos] = value
    return nums

# Using for loop
def insertion_sort_1(nums):
    for i in range(1, len(nums)):
        val = nums[i]
        ins_pos = i

        for j in range(i -1, -1, -1):
            if nums[j] > val:
                nums[j + 1] = nums[j]
                ins_pos = j
            else:
                break
        nums[ins_pos] = val
    return nums

# Using Recursion
def insertion_sort_r(nums, n=1):
    # base case, n = len(nums)
    if n == len(nums):
        return nums
    else:
        val = nums[n]
        ins_pos = n
        while ins_pos > 0 and nums[ins_pos - 1] > val:
            nums[ins_pos] = nums[ins_pos - 1]
            ins_pos = ins_pos - 1
        
        nums[ins_pos] = val
        return insertion_sort_r(nums, n + 1)


if __name__ == '__main__':
    print(insertion_sort([0, -6, 3, 2, 1]))
    print(insertion_sort_1([0, -6, 3, 2, 1]))
    print(insertion_sort_r([0, -6, 3, 2, 1]))