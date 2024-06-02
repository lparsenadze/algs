from math import sqrt

def fibonacci_last_digit(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10


def fibonacci_last_digit_fast(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current % 10, (previous + current) % 10

    return current



if __name__ == '__main__':
    #from random import randint
    #for i in range(100):
    #    x = randint(0, 20)
    #    fn1 = fibonacci_last_digit(x)
    #    fn2 = fibonacci_last_digit_fast(x)
    #    print(f'fn1 {fn1}; fn2 {fn2}')
    #    if fn1 == fn2:
    #        print('OK')
    #    else:
    #        print('error')

    n = int(input())
    print(fibonacci_last_digit_fast(n))
