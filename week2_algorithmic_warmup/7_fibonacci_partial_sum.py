# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    _sum = 0

    current = 0
    _next  = 1

    for i in range(to + 1):
        if i >= from_:
            _sum += current

        current, _next = _next, current + _next

    return _sum % 10


def F(n):
    if n <= 1:
        return n
    prev, curr = 0, 1
    for _ in range(n - 1):
        prev, curr = curr, (prev + curr) % 10
    return curr

def fibonacci_partial_sum(n):
    return (F(n + 2) - 1) % 10

def fibonacci_partial_sum_improved(from_, to):
    pisano_period = 60
    from_ %= pisano_period
    to %= pisano_period
    F_from = fibonacci_partial_sum(from_ - 1)
    F_to = fibonacci_partial_sum(to)

    return (F_to - F_from) % 10


if __name__ == '__main__':
    #from random import randint
    #import time
    #start = time.time()
    ##for i in range(100):
    #    n = randint(100, 500)
    #    m = randint(500, 1000)
    #    fn1 = fibonacci_partial_sum_naive(n, m)
    #    fn2 = fibonacci_partial_sum_improved(n, m)
    #    print(f'fn1 {fn1}; fn2 {fn2}')
    #    if fn1 == fn2:
    #        print('OK')
    #        pass
    #    else:
    #        print(n, m)
    #        print('error')
    #end = time.time()
    #print('passed', end - start)

    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_improved(from_, to))