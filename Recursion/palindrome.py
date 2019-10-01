# Recursively check if a word is a palindrome

def pal_check(word):
    if len(word) > 1:
        if word[0] == word[-1]:
            return True and pal_check(word[1:-1])
        else:
            return False
    return True

def strip_word(word):
    return (''.join([c.lower() for c in word if c.isalpha()]))

if __name__ == '__main__':
    print(pal_check('racecar') == True)
    print(pal_check('justin') == False)
    print(strip_word('this is a test'))
    print(pal_check(strip_word('Live not on evil')) == True)
    print(pal_check(strip_word('Go hang a salami; I’m a lasagna hog.'))== True)