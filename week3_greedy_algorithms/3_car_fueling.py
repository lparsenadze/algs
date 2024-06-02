from sys import stdin


def min_refills(distance, tank, stops):
    # 950 400 [200 375 550 750]
    prev = stops[0]
    for i in range(1, len(stops)):
        tmp = stops[i]
        stops[i] = tmp - prev
        prev = tmp
    # [200, 175, 175, 200]
    stops.append(distance - prev)
    count = 0
    available = tank
    for i in range(len(stops) - 1):
        available -= stops[i]
        if available < 0:
            return -1
        if available < stops[i+1]:
            count += 1
            available = tank
    available -= stops[-1]
    if available >= 0:
        return count

    return -1


if __name__ == '__main__':
    d, m, _, *stops = map(int, stdin.read().split())
    #d, m, stops = (200, 250, [100, 150])
    print(min_refills(d, m, stops))
