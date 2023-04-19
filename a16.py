# p108
def calc_diff(a_list: list[int], b_list: list[int]) -> int:
    dp = [0 for _ in range(len(a_list)+1)]
    dp[0] = 0
    dp[1] = a_list[0]
    for n in range(2, len(a_list)+1):
        dp[n] = min(b_list[n-2] + dp[n-2], a_list[n-1] + dp[n-1])

    return dp[-1]


def main():
    n = 5
    a_list = [2, 4, 1, 3]
    b_list = [5, 3, 7]
    ans = 8

    result = calc_diff(a_list, b_list)
    print(ans)
    print(result)
    print(ans == result)


if __name__ == '__main__':
    main()
