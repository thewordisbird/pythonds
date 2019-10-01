# Recursively convert and integer to a string in any base up to 16

def int_to_string(num, base):
    chars = '0123456789ABCDEF'
    if num < base:
        return chars[num]
    else:
        return int_to_string(num // base, base) + chars[num % base]

if __name__ == '__main__':
    print(int_to_string(10, 2) == '1010')
    print(int_to_string(255, 16) == 'FF')
    print(int_to_string(1453, 16) == '5AD')
