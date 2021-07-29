要想获胜，必须得到一半以上的节点
二号玩家有且仅有以下三种情况可以确保获胜:
1. x的左子树节点数量比n/2多，直接选x的左子树即可获得超过一半的节点
2. x的右子树节点数量比n/2多，直接选x的右子树即可获得超过一半的节点
3. x的左子树与右子树节点数量之和少于n/2, 即x父节点那边的节点数量比n/2多, 直接选x的父节点即可获得超过一半的节点

```
class Solution {
    public boolean btreeGameWinningMove(TreeNode root, int n, int x) {
        TreeNode xRoot = findNode(root, x);
        int left = countNodes(xRoot.left);
        int right = countNodes(xRoot.right);
        int half = n/2;
        if(left > half || right > half || left + right < half){
            return true;
        }
        return false;
    }

    private TreeNode findNode(TreeNode root, int x){
        if(root == null){
            return null;
        }
        if(root.val == x){
            return root;
        }
        TreeNode left = findNode(root.left, x);
        TreeNode right = findNode(root.right, x);
        return left != null ? left : right;
    }

    private int countNodes(TreeNode root){
        if(root == null){
            return 0;
        }
        return countNodes(root.left) + countNodes(root.right) + 1;
    }
}
```