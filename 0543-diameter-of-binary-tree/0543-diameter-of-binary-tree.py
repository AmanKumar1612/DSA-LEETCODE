# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def length(root) -> int:
            if root is None:
                return 0
            return 1+max(length(root.left),length(root.right))
        if root is None:
            return 0
        n=length(root.left)+length(root.right)
        r_dia=self.diameterOfBinaryTree(root.left)
        l_dia=self.diameterOfBinaryTree(root.right)
        return max(n,r_dia,l_dia)