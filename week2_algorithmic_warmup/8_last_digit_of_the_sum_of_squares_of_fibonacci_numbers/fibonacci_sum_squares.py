def fibonacci_sum_squares(n):
    if n <= 1:
        return n

    previous, current, sum = 0, 1, 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10


def fibonacci_sum_squares_improved(n):
    pisano_period = 60
    sum_ = 1
    n %= pisano_period
    if n <= 1:
        return n
    prev, curr = 0, 1
    for _ in range(n - 1):
        prev, curr = curr, (prev + curr) % 10
        sum_ += (curr * curr) % 10
        sum_ %= 10
    return sum_ % 10


if __name__ == '__main__':
    #from random import randint
    #import time
    #start = time.time()
    #for _ in range(100):
        #n = randint(1000, 50000)
        #fn1 = fibonacci_sum_squares(n)
        #fn2 = F(n)
        #if fn1 == fn2:
        #    print("OK")
        #else:
        #    print(f"Error: {fn1} {fn2}")
        #    print(f"n: {n}")
    #end = time.time()
    #print(end - start)
    n = int(input())
    print(fibonacci_sum_squares_improved(n))