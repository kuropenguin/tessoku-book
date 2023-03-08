def binary_search(target: int, list: list[int]) -> int:
    left = 0
    right = len(list) - 1
    index = -1
    while left <= right:
        middle = int((left + right)/2)
        if list[middle] == target:
            index = middle + 1
            break
        if list[middle] > target:
            right = middle
        if list[middle] < target:
            left = middle + 1
    return index


def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    index = binary_search(x, a)
    print(index)


if __name__ == '__main__':
    main()
