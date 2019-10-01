def palindrome(string):
    # split string to list ignore non alpha characters
    char_list = [c for c in string if c.isalpha()]
    l = len(char_list) - 1
    for i, c in enumerate(char_list):
        if i >= l/2 and c.lower() != char_list[l - i].lower():
            return False
    
    return True