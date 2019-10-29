# Implement Merge Sort



def mergesort(nums):
    if len(nums) > 1:
        mid = int(len(nums) / 2)

        left, right = mergesort(nums[:mid]), mergesort(nums[mid:])

        return merge(left, right)
    else:
        return nums


def merge(left, right):
    print(left,right)
    result = []
    l_pointer = r_pointer = 0
    
    while l_pointer < len(left) and r_pointer < len(right):
        if left[l_pointer] < right[r_pointer]:
            result.append(left[l_pointer])
            l_pointer += 1
        else:
            result.append(right[r_pointer])
            r_pointer += 1

    result.extend(left[l_pointer:])
    result.extend(right[r_pointer:])

    print(left, right, result)
    return result


if __name__ == '__main__':
    nums = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(mergesort(nums))