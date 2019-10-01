# Calculate the sum of a list of numbers recursively
def list_sum(nums):
    if len(nums) > 1:
        return nums[0] + list_sum(nums[1:])
    else:
        return nums[0]

if __name__ == '__main__':
    print(list_sum(list(range(10))))