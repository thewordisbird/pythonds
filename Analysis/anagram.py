def anagram_solution_1(str1, str2):
    if len(str1) != len(str2):
        return False
    
    a_list = list(str2)
    pos1 = 0

    while pos1 < len(str1):
        pos2 = 0
        found = False

        while pos2 < len(a_list) and not found:
            if str1[pos1] == a_list[pos2]:
                found = True
            else:
                pos2 += 1

        if found:
            a_list[pos2] = None
        else:
            return False

        pos1 += 1
    
    return True

def anagram_solution_2(str1, str2):
    a_list1 = list(str1)
    a_list2 = list(str2)

    a_list1.sort()
    a_list2.sort()

    for i, s in enumerate(a_list1):
        if s != a_list2[i]:
            return False
    return True

def anagram_solution_3(str1, str2):
    char_count_a = [0] * 26
    char_count_b = [0] * 26

    # ord() gives the ansi number of the character
    for i in range(len(str1)):
        char_count_a[ord(str1[i]) - ord('a')] +=1

    for i in range(len(str2)):
        char_count_b[ord(str2[i]) - ord('a')] +=1

    for i, v in enumerate(char_count_a):
        print(v, char_count_b[i])
        if v != char_count_b[i]:
            return False
    
    return True
        


if __name__ == '__main__':
    str1 = 'justinisthebest'
    str2 = 'besttheisjustin'
    print(anagram_solution_1(str1, str2))
    print(anagram_solution_2(str1, str2))
    print(anagram_solution_3(str1, str2))

