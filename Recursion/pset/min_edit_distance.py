def edit_distance_rec(str_x, str_y):
    #print(str_x, str_y)
    if str_x == '':
        return len(str_y)
    if str_y == '':
        return len(str_x)

    # If the characters are the same do nothing and check further substrings
    if str_x[0] == str_y[0]:
        cost = 0
    else:
        cost = 1

    return cost + min(
                    edit_distance_rec(str_x[1:], str_y),
                    edit_distance_rec(str_x, str_y[1:]),
                    edit_distance_rec(str_x[1:], str_y)
                    )


def LD(s, t):
    if s == "":
        return len(t)
    if t == "":
        return len(s)
    if s[-1] == t[-1]:
        cost = 0
    else:
        cost = 1
       
    res = min([LD(s[:-1], t)+1,
               LD(s, t[:-1])+1, 
               LD(s[:-1], t[:-1]) + cost])
    return res

if __name__ == '__main__':
    str_x = 'algorithm'
    str_y = 'alligator'

    print(edit_distance_rec(str_x, str_y))
    print(LD(str_x, str_y))