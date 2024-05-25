def fibonacci_sum(n):
    if n <= 1:
        return n

    previous, current, _sum = 0, 1, 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        _sum += current

    return _sum % 10


def fibonacci_sum_fast(n):
    pisano_period = 60
    n = n % pisano_period
    def F(n):
        if n <= 1:
            return n
        previous, current = 0, 1

        for _ in range(n - 1):
            previous, current = current, (previous + current) % 10
        return current

    return (F(n + 2) - 1) % 10

if __name__ == '__main__':
    #from random import randint
    #import time
    #start = time.time()
    #for i in range(100):
    #    n = randint(1000, 100000)
    #    m = randint(1000, 100000)
    #    fn1 = fibonacci_sum(n)
    #    fn2 = fibonacci_sum_fast(n)
    #    print(f'fn1 {fn1}; fn2 {fn2}')
    #    if fn1 == fn2:
    #       print('OK')
    #        pass
    #    else:
    #        print(n)
    #        print('error')
    #end = time.time()
    #print('passed', end - start)

    n = int(input())
    print(fibonacci_sum_fast(n))
