# Find all substrings of a given string. For example:
#   given 'abc' return 'a', 'b', 'c', 'ab', 'bc', 'ac', 'abc'

def substings_in_string(string, cache=[]):
    if len(string) == 0:
        return
    if string not in cache:
        cache.append(string)

    substings_in_string(string[1::], cache)
    substings_in_string(string[0:-1], cache)
    
    return cache

if __name__ =='__main__':
    s = 'abcd'
    print(substings_in_string(s))