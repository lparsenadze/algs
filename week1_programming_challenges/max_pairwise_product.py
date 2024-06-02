def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product

def max_pairwise_product_fast(numbers):
    first_max = max(numbers)
    max_idx = numbers.index(first_max)
    numbers[max_idx] = 0
    second_max = max(numbers)
    return first_max * second_max

if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product_fast(input_numbers))
