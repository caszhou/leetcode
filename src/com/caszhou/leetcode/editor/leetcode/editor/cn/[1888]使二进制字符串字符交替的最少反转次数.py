# 给你一个二进制字符串 s 。你可以按任意顺序执行以下两种操作任意次： 
# 
#  
#  类型 1 ：删除 字符串 s 的第一个字符并将它 添加 到字符串结尾。 
#  类型 2 ：选择 字符串 s 中任意一个字符并将该字符 反转 ，也就是如果值为 '0' ，则反转得到 '1' ，反之亦然。 
#  
# 
#  请你返回使 s 变成 交替 字符串的前提下， 类型 2 的 最少 操作次数 。 
# 
#  我们称一个字符串是 交替 的，需要满足任意相邻字符都不同。 
# 
#  
#  比方说，字符串 "010" 和 "1010" 都是交替的，但是字符串 "0100" 不是。 
#  
# 
#  
# 
#  示例 1： 
# 
#  输入：s = "111000"
# 输出：2
# 解释：执行第一种操作两次，得到 s = "100011" 。
# 然后对第三个和第六个字符执行第二种操作，得到 s = "101010" 。
#  
# 
#  示例 2： 
# 
#  输入：s = "010"
# 输出：0
# 解释：字符串已经是交替的。
#  
# 
#  示例 3： 
# 
#  输入：s = "1110"
# 输出：1
# 解释：对第二个字符执行第二种操作，得到 s = "1010" 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 10⁵ 
#  s[i] 要么是 '0' ，要么是 '1' 。 
#  
#  Related Topics 贪心 字符串 👍 36 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minFlips(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        pre01 = [0] * n
        pre10 = [0] * n
        for i, c in enumerate(s):
            if c == '1':
                if i % 2 == 0:
                    pre01[i] = pre01[i - 1] + 1
                    pre10[i] = pre10[i - 1]
                else:
                    pre10[i] += pre10[i - 1] + 1
                    pre01[i] = pre01[i - 1]
            else:
                if i % 2 == 0:
                    pre10[i] += pre10[i - 1] + 1
                    pre01[i] = pre01[i - 1]
                else:
                    pre01[i] = pre01[i - 1] + 1
                    pre10[i] = pre10[i - 1]
        pre01 = [0] + pre01
        pre10 = [0] + pre10
        if n % 2 == 0:
            return min(pre01[-1], pre10[-1])
        ans = float("inf")
        for i in range(n):
            ans1 = pre01[-1] - pre01[i] + pre10[i]
            ans2 = pre10[-1] - pre10[i] + pre01[i]
            ans = min(ans, ans1, ans2)
        return ans
# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    print(Solution().minFlips("1110000"))
