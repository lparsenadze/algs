def gcd(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

def gcd_fast(a, b):
    if b == 0:
        return a

    a_ = a % b
    return gcd_fast(b, a_)


if __name__ == "__main__":
    #from random import randint
    #for i in range(1000):
    #    x = randint(1, 500)
    #    y = randint(1, 500)
    #    fn1 = gcd(x, y)
    #    fn2 = gcd_fast(x, y)
    #    print(f'fn1 {fn1}; fn2 {fn2}')
    #    if fn1 == fn2:
    #        print('OK')
    #    else:
    #        print(x, y)
    #        print('error')

    a, b = map(int, input().split())
    print(gcd_fast(a, b))
