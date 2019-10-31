# Implement Quick Sort:


def quicksort(nums, left=0, right=None):
    if right == None:
        right = len(nums) - 1

    if left < right:
        # Determine pivot value. In this case I'm using the mid point
        pivot = nums[(left + right) // 2]
        split = partition(nums, left, right, pivot)

        # Recursively run quicksort on both halves 
        # FIGURE OUT SOLUTION FOR: I think this has to do with using greater or ==. Investigate further.
        quicksort(nums, left, split)
        quicksort(nums, split + 1, right)
        #quicksort(nums, left, split - 1)
        #quicksort(nums, split, right)
    return nums

def partition(nums, left, right, pivot):
    print(nums[left:right + 1], pivot)
    while left <= right:
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

    # When a crossover is reached, return the left pointer which will be used as the split.
    return left


if __name__ == '__main__':
    nums = [54, 26, 93, 17, 77, 31, 44, 55, 20, 54]
    print(quicksort(nums), nums)