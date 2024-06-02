def binary_search(keys, query):
    low = 0
    high = len(keys) - 1
    result = -1
    while low <= high:
        mid = (low + high) // 2
        if keys[mid] == query:
            result = mid
            high = mid - 1
        elif keys[mid] < query:
            low = mid + 1
        else:
            high = mid - 1
    return result


def binary_search_last(keys, query):
    """Finds the last occurrence of the query"""
    low = 0
    high = len(keys) - 1
    result = -1
    while low <= high:
        mid = (low + high) // 2
        if keys[mid] == query:
            result = mid
            low = mid + 1
        elif keys[mid] < query:
            low = mid + 1
        else:
            high = mid - 1
    return result


if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
