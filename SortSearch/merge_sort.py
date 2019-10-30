# Implement Merge Sort

# Merge sort is a recursive algorithm that continually splits a list in half. If the list is empty or has one item, it is sorted by definition (the base case). 
# If the list has more than one item, we split the list and recursively invoke a merge sort on both halves. Once the two halves are sorted, the fundamental operation, 
# called a merge, is performed. Merging is the process of taking two smaller sorted lists and combining them together into a single, sorted, new list.

# Implementation of Merger Sort using slicing. This method creates multiple tempory lists with every slice which add time complexity O(k) per step in the sort.
# This results in the sort being O(klong(n)) time the time complexity of O(n) for the merge resulting in a total time complexity of O(knlong(n)). 
# This should still operate in a space complexity of O(n), since at each recursive level you are splittig the list into smaller parts that still add to n.

def mergesort_slice(nums):
 
    if len(nums) > 1:
        
        # Calculate mid
        mid = len(nums) // 2

        # recursively call function to get left and right sorted sub lists
        left = mergesort_slice(nums[:mid])
        right = mergesort_slice(nums[mid:])

        # merge the sorted lists
        merge_slice(nums, left, right)
    
    return nums
    

def merge_slice(nums, left, right):
    
    # Set pointers and index
    left_pointer = 0
    right_pointer = 0
    index = 0
    
    # Two finger algorithm to merge sorted sub lists into main list
    while left_pointer < len(left) and right_pointer < len(right):
        if left[left_pointer] <= right[right_pointer]:
            nums[index] = left[left_pointer]
            left_pointer += 1
        else:
            nums[index] = right[right_pointer]
            right_pointer += 1
        
        index += 1

    # Clear reamining items from left if any
    while left_pointer < len(left):
        nums[index] = left[left_pointer]
        left_pointer += 1
        index += 1

    # Clear remaining items from right if any
    while right_pointer < len(right):
        nums[index] = right[right_pointer]
        right_pointer += 1
        index += 1

# Implementation of merge sort without slicing. The recursve mergesort function sets the left and right pointers that allow for a mergesort step at a cost of O(1) and also
# allow for inplace sort of the original list. This will be a true O(nlog(n)) time complexity and O(n) space complexity

def mergesort_pointer(nums, left_start=0, right_end=None):
    # Set right_end for first call
    if right_end == None:
        right_end = len(nums) - 1
    
    # Base case
    if left_start >= right_end:
        return
    else:
        mid = (left_start + right_end) // 2

        mergesort_pointer(nums, left_start, mid)
        mergesort_pointer(nums, mid + 1, right_end)

        merge_pointer(nums, left_start, right_end)

    return nums

def merge_pointer(nums, left_start, right_end):
    result = []

    left_end = (left_start + right_end) // 2
    right_start = left_end + 1
    left_pointer = left_start
    right_pointer = right_start
    index = left_pointer

    while left_pointer <= left_end and right_pointer <= right_end:
        if nums[left_pointer] < nums[right_pointer]:
            result.append(nums[left_pointer])
            left_pointer += 1
        else:
            result.append(nums[right_pointer])
            right_pointer += 1
        
    # Clear leftoveres
    for i in range(left_pointer, left_end + 1):
        result.append(nums[i])
    
    for j in range(right_pointer, right_end + 1):
        result.append(nums[j])

    # sort nums in place
    for val in result:
        nums[index] = val
        index += 1


if __name__ == '__main__':
    nums = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    #nums = [7, 6, 5, 4, 3, 2, 1]
    print(mergesort_slice(nums), nums)
    
    nums = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    #nums = [7, 6, 5, 4, 3, 2, 1]
    print(mergesort_pointer(nums), nums)