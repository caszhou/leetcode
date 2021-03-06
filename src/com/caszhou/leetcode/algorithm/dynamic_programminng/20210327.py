from functools import lru_cache

costs = [2, 2, 6, 5, 4]
values = [6, 3, 5, 4, 6]


@lru_cache
def one_zero_package_max_value(n: int, c: int):
    print("one_zero_package_max_value(%d, %d)" % (n, c))

    """
    一共有N件物品，第i（i从1开始）件物品的重量为w[i]，价值为v[i]。在总重量不超过背包承载上限W的情况下，能够装入背包的最大价值是多少？

    时间复杂度：O(n)

    :param n: 第n个item
    :param c: pick number
    :return: items max value
    """

    if n == 0:
        return 0

    idx = n - 1

    not_pick = one_zero_package_max_value(idx, c)
    if c >= costs[idx]:
        pick = one_zero_package_max_value(idx, c - costs[idx]) + values[idx]

        max_value = max(not_pick, pick)

        return max_value
    else:
        return not_pick


if __name__ == '__main__':
    print("value: %d" % one_zero_package_max_value(5, 10))
