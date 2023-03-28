def shakutori(diff: int, list: list[int]) -> int:
    return 10


def main():
    # n, x = map(int, input().split())
    # a = list(map(int, input().split()))
    n = 7
    k = 10
    l = [11, 12, 16, 22, 27, 28, 31]
    ans = 11
    count = shakutori(k, l)
    print(count)
    print(ans)


if __name__ == '__main__':
    main()
