# Implement Merge Sort

def mergesort(arr):
    print(arr)
    sort(arr, 0, len(arr) - 1)
    return arr


def sort(arr, left_start, right_end):
    if left_start >= right_end:
        return
    
    mid = (left_start + right_end) // 2
    
    print('left', left_start, mid)
    sort(arr, left_start, mid)
    
    print('right', mid + 1, right_end)
    sort(arr, mid + 1, right_end)
    
    merge(arr, left_start, right_end)


def merge(arr, left_start, right_end):
    result = []
    left_end = (right_end + left_start) // 2
    right_start = left_end + 1
    size = right_end - left_start + 1

    left_pointer = left_start
    right_pointer = right_start

    while left_pointer <= left_end and right_pointer <= right_end:
        if arr[left_pointer] < arr[right_pointer]:
            result.append(arr[left_pointer])
            left_pointer += 1
        else:
            result.append(arr[right_pointer])
            right_pointer += 1
        
    
    # append any leftovers from left or right. There will only be laftovers in one list
    for i in range(left_pointer, left_end):
        result.append(arr[i])

    for j in range(right_pointer, right_end):
        result.append(arr[j])


    # Modify section of nums by replacing with sorted results
    for k, val in enumerate(result):
        arr[k + left_start] = val
    



  


if __name__ == '__main__':
    nums = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    nums = [5, 4, 3, 2, 1]
    print(mergesort(nums))