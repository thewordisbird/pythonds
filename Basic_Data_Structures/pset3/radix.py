# Implement a radix sorting machine. A radix sort for base 10 integers is a mechanical sorting 
# technique that utilizes a collection of bins, one main bin and 10 digit bins. Each bin acts 
# like a queue and maintains its values in the order that they arrive. The algorithm begins by 
# placing each number in the main bin. Then it considers each value digit by digit. The first value 
# is removed and placed in a digit bin corresponding to the digit being considered. For example, 
# if the ones digit is being considered, 534 is placed in digit bin 4 and 667 is placed in digit bin 7. 
# Once all the values are placed in the corresponding digit bins, the values are collected from bin 0 to bin 9 
# and placed back in the main bin. The process continues with the tens digit, the hundreds, and so on. 
# After the last digit is processed, the main bin contains the values in order.

# Notes:
# Time Complexity = O(d(n+b)) 
# This is faster than quick sort (O(nlogn)) for range of 1 to n^2
# pre-read code. In this one you fought with errors because in the first nested loop
#   you were working with 'nums', not 'main'. Minimize those errors, by a thorough 
#   read through after coding

# Constant sub problems:
#   - working with digits in numbers
#   - 
from collections import deque
def radix_sort(nums):
    digits = max_digits(max(nums))
    main = nums
    sub = [deque() for x in range(10)]

    digit = 1
    for i in range(digits):
        # append to subs ques from main for each digit
        for j in range(len(main)):
            bin = get_digit(main[j], digit)
            
            sub[bin].append(main[j])
        print(main, sub)
        
        # append from subs to main 
        main = []
        for k in range(len(sub)):
            while len(sub[k]) > 0:
                main.append(sub[k].popleft())
        
        print(main, sub)
        digit += 1

    return main
    
def max_digits(num):
    digit_count = 0
    while num > 0:
        num //= 10
        digit_count += 1
    return digit_count

def get_digit(num, digit):
    for i in range(digit - 1):
        num //= 10
    return num % 10