from math import floor


def change(money):
    count = 0
    while money > 0:
        if money >= 10:
            count += 1
            money -= 10
        elif 5 <= money < 10:
            count += 1
            money -= 5
        else:
            count += money
            money = 0
    return count

def change_2(money):
    return money % 5 + (money - money % 5) // 10 + int(((money - money % 5) % 10) == 5)

def change_3(money):
    return floor(money / 10) + floor((money % 10) / 5) + money % 5

if __name__ == '__main__':
    #from random import randint
    #for _ in range(100):
    #    money = randint(0, 100)
    #    fn1 = change_3(money)
    #    fn2 = change_2(money)
    #    if fn1 != fn2:
    #        print(money, f"fn1 {fn1}, fn2 {fn2}")
    #    else:
    #        print('OK')
    m = int(input())
    print(change_3(m))
