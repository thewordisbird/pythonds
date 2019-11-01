# Implement Quick Sort:


def quicksort(nums, left=0, right=None):
    print(f'quicksort({nums}, {left}, {right})')
    if right == None:
        right = len(nums) - 1

    if left < right:
        # Determine pivot value. In this case I'm using the mid point
        pivot = nums[(left + right) // 2]
        split = partition(nums, left, right, pivot)

        # Recursively run quicksort on both halves 
        quicksort(nums, left, split - 1)
        quicksort(nums, split, right)
    return nums

def partition(nums, left, right, pivot):
    print(f'\tpartition({nums}, {left}, {right}, {pivot})')
    while left < right:
        
        while nums[left] < pivot:
            # Important note: this increments forward upon true moving the pointer to the next element.
            # This will allow the pivot to be swapped if it is the next element. Therefore, we don't
            # need to use <=
            left += 1
            
        while nums[right] > pivot:
            right -= 1
      
        # Swap elements if neccessary
        if left <= right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
    
    print(f'\tpartition returning {left}')
    # When a crossover is reached, return the left pointer which will be used as the split.
    return left

def quicksort_b(nums, left=0, right=None):
    print(f'quicksort_b({nums}, {left}, {right})')
    if right == None:
        right = len(nums) - 1
    
    if left < right:
        # Determine pivot value. In this case I'm using the mid point
        pivot = nums[(left + right) // 2]
        split = partition_b(nums, left, right, pivot)

        # Recursively run quicksort on both halves 
        quicksort_b(nums, left, split)
        quicksort_b(nums, split + 1, right)
    return nums

def partition_b(nums, left, right, pivot):
    print(f'\tpartition_b({nums}, {left}, {right}, {pivot})')
    while left < right:

        while nums[left] < pivot:
            # Important note: this increments forward upon true moving the pointer to the next element.
            # This will allow the pivot to be swapped if it is the next element. Therefore, we don't
            # need to use <=
            left += 1
        
        while nums[right] > pivot:
            right -= 1

        # Swap elements if neccessary
        if left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
    
    print(f'\tpartition_b returning {left}')
    # When a crossover is reached, return the left pointer which will be used as the split.
    return left



if __name__ == '__main__':
    nums = [54, 26, 93, 17, 77, 31, 44, 55, 20, 54]
    print(f'Running quicksort on {nums}')
    print(quicksort(nums), nums)

    nums = [54, 26, 93, 17, 77, 31, 44, 55, 20, 54]
    print(f'Running quicksort_b on {nums}')
    print(quicksort_b(nums), nums)