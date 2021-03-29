class TreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, root: TreeNode):
        self.root = root


class BinaryTreeUtils:
    @staticmethod
    def invert(root: BinaryTree):
        if root is not None:
            tmp = root.right
            root.left = root.right
            root.right = tmp

            if root.left is not None:
                BinaryTreeUtils.invert(root.left)

            if root.right is not None:
                BinaryTreeUtils.invert(root.right)

        return root
