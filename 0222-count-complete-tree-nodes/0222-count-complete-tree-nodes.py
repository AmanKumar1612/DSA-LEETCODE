# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left_depth = self.get_left_depth(root)
        right_depth = self.get_right_depth(root)

        if left_depth == right_depth:
            return (1 << left_depth) - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def get_left_depth(self, node: Optional[TreeNode]) -> int:
        depth = 0
        while node:
            depth += 1
            node = node.left
        return depth

    def get_right_depth(self, node: Optional[TreeNode]) -> int:
        depth = 0
        while node:
            depth += 1
            node = node.right
        return depth