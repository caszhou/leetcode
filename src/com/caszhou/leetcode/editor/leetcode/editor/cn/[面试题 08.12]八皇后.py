# 设计一种算法，打印 N 皇后在 N × N 棋盘上的各种摆法，其中每个皇后都不同行、不同列，也不在对角线上。这里的“对角线”指的是所有的对角线，不只是平分整
# 个棋盘的那两条对角线。 
# 
#  注意：本题相对原题做了扩展 
# 
#  示例: 
# 
#   输入：4
#  输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
#  解释: 4 皇后问题存在如下两个不同的解法。
# [
#  [".Q..",  // 解法 1
#   "...Q",
#   "Q...",
#   "..Q."],
# 
#  ["..Q.",  // 解法 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
#  
#  Related Topics 数组 回溯 👍 90 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def generate_board():
            board = list()
            for i in range(n):
                rows[queens[i]] = "Q"
                board.append("".join(rows))
                rows[queens[i]] = "."
            return board

        def backtrack(row: int):
            if row == n:
                board = generate_board()
                solutions.append(board)
            else:
                for column in range(n):
                    if column in columns or row - column in diagonal1 or row + column in diagonal2:
                        continue
                    queens[row] = column
                    columns.add(column)
                    diagonal1.add(row - column)
                    diagonal2.add(row + column)
                    backtrack(row + 1)
                    columns.remove(column)
                    diagonal1.remove(row - column)
                    diagonal2.remove(row + column)

        solutions = list()
        queens = [-1] * n
        columns = set()
        diagonal1 = set()
        diagonal2 = set()
        rows = ["."] * n
        backtrack(0)
        return solutions
# leetcode submit region end(Prohibit modification and deletion)
