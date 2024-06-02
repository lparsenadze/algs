from math import floor, sqrt


def optimal_summands(n):
    summands = []
    current_element = 1
    while n > 0:
        if n - current_element > current_element:
            summands.append(current_element)
            n -= current_element
            current_element += 1
        else:
            summands.append(n)
            n = 0
    return summands



if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    print(*summands)
    print(optimal_summands(n))