# Implement Bubble Sort

def bubble_sort_r(nums, n=None):
    if n == None:
        n = len(nums) - 1
    if n == 1:
        return nums
    else:
        for i in range(n):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
        return bubble_sort_r(nums, n - 1)


def bubble_sort_i(nums):
    for i in range(len(nums) - 1, 0 , -1):
        for j in range(i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    return nums


if __name__ == '__main__':
    print(bubble_sort_r([2, 5, 1, 6, 3]))
    print(bubble_sort_i([2, 5, 1, 6, 3]))