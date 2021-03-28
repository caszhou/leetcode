costs = [2, 2, 6, 5, 4]
values = [6, 3, 5, 4, 6]


def one_zero_package_max_value(n: int, c: int):
    print("one_zero_package_max_value(%d, %d)" % (n, c))

    """
    一共有N件物品，第i（i从1开始）件物品的重量为w[j]，价值为v[j]。在总重量不超过背包承载上限W的情况下，能够装入背包的最大价值是多少？

    时间复杂度：O(n)

    :param n: 第n个item
    :param c: pick number
    :return: items max value
    """

    costs.insert(0, 0)
    values.insert(0, 0)

    # n -> row, c -> column
    matrix = [[0 for _ in range(c + 1)] for _ in range(n + 1)]

    # column
    for j in range(1, c + 1):
        cost = j

        # row
        for i in range(1, n + 1):
            item_cost = costs[i]
            item_value = values[i]
            before = i - 1

            if cost >= item_cost:
                matrix[i][j] = max(matrix[before][cost], matrix[before][cost - item_cost] + item_value)
            else:
                matrix[i][j] = matrix[before][cost]

    return matrix[-1][-1]


if __name__ == '__main__':
    print("value: %d" % one_zero_package_max_value(5, 10))
