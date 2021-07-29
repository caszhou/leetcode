# 有两位极客玩家参与了一场「二叉树着色」的游戏。游戏中，给出二叉树的根节点 root，树上总共有 n 个节点，且 n 为奇数，其中每个节点上的值从 1 到 
# n 各不相同。 
# 
#  
# 
#  游戏从「一号」玩家开始（「一号」玩家为红色，「二号」玩家为蓝色），最开始时， 
# 
#  「一号」玩家从 [1, n] 中取一个值 x（1 <= x <= n）； 
# 
#  「二号」玩家也从 [1, n] 中取一个值 y（1 <= y <= n）且 y != x。 
# 
#  「一号」玩家给值为 x 的节点染上红色，而「二号」玩家给值为 y 的节点染上蓝色。 
# 
#  
# 
#  之后两位玩家轮流进行操作，每一回合，玩家选择一个他之前涂好颜色的节点，将所选节点一个 未着色 的邻节点（即左右子节点、或父节点）进行染色。 
# 
#  如果当前玩家无法找到这样的节点来染色时，他的回合就会被跳过。 
# 
#  若两个玩家都没有可以染色的节点时，游戏结束。着色节点最多的那位玩家获得胜利 ✌️。 
# 
#  
# 
#  现在，假设你是「二号」玩家，根据所给出的输入，假如存在一个 y 值可以确保你赢得这场游戏，则返回 true；若无法获胜，就请返回 false。 
# 
#  
# 
#  示例： 
# 
#  
# 
#  输入：root = [1,2,3,4,5,6,7,8,9,10,11], n = 11, x = 3
# 输出：True
# 解释：第二个玩家可以选择值为 2 的节点。
#  
# 
#  
# 
#  提示： 
# 
#  
#  二叉树的根节点为 root，树上由 n 个节点，节点上的值从 1 到 n 各不相同。 
#  n 为奇数。 
#  1 <= x <= n <= 100 
#  
#  Related Topics 树 深度优先搜索 二叉树 👍 68 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
import math


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def btreeGameWinningMove(self, root, n, x):
        # root = self.ary_to_tree_node(ary, 0, False)

        x_root = self.find_node(root, x)
        half = math.floor(n / 2)

        if x_root is not None:
            left_size = self.count_nodes(x_root.left)
            right_size = self.count_nodes(x_root.right)
            return left_size > half or right_size > half or left_size + right_size < half

        return False
    #
    # def ary_to_tree_node(self, ary, level, right):
    #     if right:
    #         root = TreeNode(ary[2 ^ level])
    #     else:
    #         root = TreeNode(ary[2 ^ level - 1])
    #     level += 1
    #
    #     if len(ary) > 1:
    #         root.left = self.ary_to_tree_node(ary, level, False)
    #
    #     if len(ary) > 2:
    #         root.right = self.ary_to_tree_node(ary, level, True)
    #
    #     return root

    def find_node(self, root, x):
        if root is None:
            return None

        if root.val == x:
            return root

        left = self.find_node(root.left, x)
        right = self.find_node(root.right, x)
        return left if left is not None else right

    def count_nodes(self, node):
        if node is None:
            return 0
        return self.count_nodes(node.left) + self.count_nodes(node.right) + 1
# leetcode submit region end(Prohibit modification and deletion)
