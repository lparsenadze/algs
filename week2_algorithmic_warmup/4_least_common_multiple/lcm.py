def lcm(a, b):
    for l in range(1, a * b + 1):
        if l % a == 0 and l % b == 0:
            return l

    assert False

def lcm_fast(a, b):
    def gcd(a, b):
        if b == 0:
            return a
        a_ = a % b
        return gcd(b, a_)
    g = gcd(a, b)

    return abs(a * b) / g

if __name__ == '__main__':
    #from random import randint
    #for i in range(100):
    #    x = randint(0, 500)
    #    y = randint(0, 500)
    #    fn1 = lcm(x, y)
    #    fn2 = lcm_fast(x, y)
    #    print(f'fn1 {fn1}; fn2 {fn2}')
    #    if fn1 == fn2:
    #        print('OK')
    #    else:
    #        print(x, y)
    #        print('error')
    a, b = map(int, input().split())
    print(lcm_fast(a, b))

