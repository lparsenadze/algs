def fibonacci_number(n):
    if n <= 1:
        return n

    return fibonacci_number(n - 1) + fibonacci_number(n - 2)


def fibonacci_number_fast(n):
    if n <= 1:
        return n
    prev = 0
    curr = 1
    for i in range(n - 1):
        prev, curr = curr, prev + curr
    return curr


if __name__ == '__main__':
    #from random import randint
    #for i in range(100):
    #    x = randint(0, 20)
    #    fn1 = fibonacci_number(x)
    #    fn2 = fibonacci_number_fast(x)
    #    print(f'fn1 {fn1}; fn2 {fn2}')
    #    if fn1 == fn2:
    #        #print('OK')
    #        pass
    #    else:
    #        print(x)
    #        print('error')

    input_n = int(input())
    print(fibonacci_number_fast(input_n))
