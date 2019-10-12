# Given a string, write a recursive function that check if the given string is palindrome, else not palindrome.

# Examples :

# Input : malayalam
# Output : Yes
# Reverse of malayalam is also
# malayalam.

# Input : max
# Output : No
# Reverse of max is not max.

# This solution works from both ends so time complexity is O(log(n))

# NOTE: the use of the 'true and' allows for the evaluation to pass thrugh each recursion level.
# Without this only the first level teset would be returned

def palindrome(s):
    # base case len(s) == 1
    if len(s) > 1:
        if s[0] == s[-1]:
            return True and palindrome(s[1:-1])
        else:
            return False    
    return True
    

if __name__ == '__main__':
    s = 'rar'
    print(palindrome(s))