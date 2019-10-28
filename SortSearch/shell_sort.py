# Implementation of shell sort

# The shell sort, sometimes called the “diminishing increment sort,” improves on the insertion sort 
# by breaking the original list into a number of smaller sublists, each of which is sorted using an insertion sort. 
# The unique way that these sublists are chosen is the key to the shell sort. Instead of breaking the list into sublists 
# of contiguous items, the shell sort uses an increment i, sometimes called the gap, to create a sublist by choosing all items that are i items apart.

# Steps:
# Start with a gap of n // 2
# Run insertion sort
# recalculate gap = gap // 2
# Run insertion sort
# reapat above until gap = 1
# Retrun final insertiona sort

def shell_sort(nums):
    '''Calculates gap and passes information to gap_insertion_sort function for sorting'''
    gap = len(nums) // 2

    while gap > 0:
        for i in range(gap):
            gap_insertion_sort(nums, i, gap)
        
        gap = gap // 2

    return nums
    

def gap_insertion_sort(nums, pos_start, gap):
    for i in range(pos_start + gap, len(nums), gap):
        val = nums[i]
        ins_pos = i

        while ins_pos > pos_start and nums[ins_pos - gap] > val:
            nums[ins_pos] = nums[ins_pos - gap]
            ins_pos = ins_pos - gap

        nums[ins_pos] = val

    #return nums

if __name__ == '__main__':
    print(shell_sort([0, -6, 3, 2, 1]))