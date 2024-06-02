from itertools import permutations


def largest_number_naive(numbers):
    numbers = list(map(str, numbers))

    largest = 0

    for permutation in permutations(numbers):
        largest = max(largest, int("".join(permutation)))

    return largest


def largest_number_fast(numbers):
    numbers = list(map(str, numbers))
    digit_numbers = list(map(len, list(map(str, numbers))))
    paired_lists = list(zip(digit_numbers, numbers))
    paired_lists.sort(key=lambda x: x[1])
    _, numbers = zip(*paired_lists)

    modified_numbers = [int(n) // 10**(len(n)-1) if len(n) >= 2 else int(n) for n in numbers]
    paired_lists = list(zip(numbers, modified_numbers))
    paired_lists.sort(key=lambda x: x[1], reverse=True)
    sorted_strings, _  = zip(*paired_lists)
    return int(''.join(sorted_strings))


if __name__ == '__main__':
    _ = int(input())
    input_numbers = input().split()
    #input_numbers = ['21', '2']
    #print(largest_number_naive(input_numbers))
    print(largest_number_fast(input_numbers))
