# Write a recursive fuction to reverse a list

def reverse_list(my_list, h=0, t=-1):
    print(my_list, h, t, my_list.index(my_list[h]) - my_list.index(my_list[t]) > -1)
    if my_list.index(my_list[h]) - my_list.index(my_list[t]) > -1:
        print(my_list)
        return my_list
    else:
        head = my_list[h]
        tail = my_list[t]
        my_list[h] = tail
        my_list[t] = head
        h += 1
        t -= 1
        return reverse_list(my_list,h, t)

if __name__ == '__main__':
    names = ['justin', 'lindsay', 'amanda', 'laurie', 'steve']
    print(reverse_list(names))