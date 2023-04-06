# list がsort済み前提
# FIXME これ今 start_point がどんどん次に行ってしまっている（自分の差分の限界まで進んでから次のstart_pointに移るようにしたい）
def shakutori(diff: int, sorted_list: list[int]) -> int:
    count = 0
    end_point = 1  # start_point の 次から確認を始める
    for start_point in range(len(sorted_list) - 1):
        while end_point < len(sorted_list) and sorted_list[end_point] - sorted_list[start_point] <= diff:
            # start と end の間にある数は全て条件を満たすので、その数をカウントする
            # 11, 13, 15 だった場合、 11 と 15 で条件を満たすのであれば, 12 と15 は必然的に条件を満たす(より近い距離にいるので)
            count += end_point - start_point
            # end_point を動かす
            # end_point が len(sorted_list) になったら 何もしない（動かさない）
            end_point += 1

    return count


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
