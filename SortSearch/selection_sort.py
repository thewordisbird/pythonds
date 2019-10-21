# Implement selection sort

def selection_sort_i(nums):
    for i in range(len(nums) - 1, 0, -1):
        pos_max = 0
        for j in range(i):
            if nums[j] > nums[pos_max]:
                pos_max = j
        print(nums[pos_max])
        nums[j], nums[-1] = nums[-1], nums[j]
    return nums

if __name__ == '__main__':
    print(selection_sort_i([3, 5, 1, 7, 4]))
    