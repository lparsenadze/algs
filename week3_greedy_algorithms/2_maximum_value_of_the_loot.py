from sys import stdin


def optimal_value(capacity, weights, values):
    value = 0.
    #40 [5, 4, 3] [10, 30, 30]
    value_per_weight = [v / w for v, w in zip(values, weights)]
    combined = zip(value_per_weight, weights, values)
    sorted_combined = sorted(combined, key=lambda x: x[0], reverse=True)
    value_per_weight, weights, values = zip(*sorted_combined)
    i = 0
    while capacity > 0 and i < len(value_per_weight):
        if capacity > weights[i]:
            value += values[i]
            capacity -= weights[i]
        else:
            value += capacity * value_per_weight[i]
            capacity = 0
        i += 1
    return value


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    #capacity = 5
    #weights = [5, 4, 3]
    #values = [10, 30, 30]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
