def min_in_list_n(l):
    min = l[0]
    for i in l:
        if i < min:
            min = i
    return min

if __name__ == '__main__':
    l = [6, 3, 7, 1, 2, 9, -4]
    print(min_in_list_n(l))