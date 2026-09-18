# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        
        def valid(root,mini=None,maxi=None):
            if not root:
                return True
            if mini and root.val <= mini.val :
                return False
            if maxi and root.val >= maxi.val :
                return False
            return valid(root.left,mini,root) and valid(root.right,root,maxi)
        return valid(root)
