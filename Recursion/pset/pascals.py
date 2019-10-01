def factorial(num):
    if num < 2:
        return 1
    else:
        return num * factorial(num - 1)

def choose(num):
    nums = []
    n_fact = factorial(num)
    for k in range(num + 1):
        nums.append(n_fact//(factorial(k) * factorial(num - k)))
    return nums
    
def pascals(rows):
    row_matrix = []
    for r in range(rows):
        row_matrix.append(choose(r))
    return row_matrix

def print_pascals(row_matrix):
    width = len(row_matrix)
    for r in row_matrix:
        padding = ' ' * (width - len(r) + 1)
        print(padding + ' '.join(list(map(str,r))))



if __name__ == '__main__':
    r = int(input('How many rows: '))
    rows = pascals(r)
    print_pascals(rows)

    #  1 
    # 1 1
    #1 1 1