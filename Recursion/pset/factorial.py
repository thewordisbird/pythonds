# Write a recursive function to compute the factorial of a number

def factorial(n):
    if n > 1:
        return n * factorial(n - 1)
    else:
        return 1

if __name__ == '__main__':
    print(factorial(1), factorial(1) == 1)
    print(factorial(2), factorial(2) == 2)
    print(factorial(3), factorial(4) == 6)
    print(factorial(4), factorial(4) == 24)
    print(factorial(5), factorial(5) == 120)
    print(factorial(0), factorial(0) == 1)