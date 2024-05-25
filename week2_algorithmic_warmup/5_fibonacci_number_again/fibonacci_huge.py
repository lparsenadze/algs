def fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

def get_pisano_period(m):
    previous, current = 0, 1
    for i in range(m * m):
        previous, current = current, (previous + current) % m
        # A Pisano period starts with 01
        if previous == 0 and current == 1:
            return i + 1

def fibonacci_huge_fast(n, m):
    if n <= 1:
        return n
    pisano_period = get_pisano_period(m)
    n = n % pisano_period

    previous = 0
    current = 1

    if n <= 1:
        return n

    for _ in range(n - 1):
        # Doing basic ops over large numbers is not trivial!
        previous, current = current, (previous + current) % m

    return current


if __name__ == '__main__':
    #from random import randint
    #import time
    #start = time.time()
    #for i in range(100):
    #    n = randint(1000, 100000)
    #    m = randint(1000, 100000)
    #    fn1 = fibonacci_huge_naive(n, m)
    #    fn2 = fibonacci_huge_fast(n, m)
    #    print(f'fn1 {fn1}; fn2 {fn2}')
    #    if fn1 == fn2:
    #       print('OK')
    #         pass
    #     else:
    #         print(n, m)
    #        print('error')
    #end = time.time()
    #print('passed', end - start)

    n, m = map(int, input().split())
    print(fibonacci_huge_fast(n, m))
