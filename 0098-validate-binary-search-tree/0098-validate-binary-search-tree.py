# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        

        def valid(root,mini,maxi):
            if not root:
                return True
            if maxi and maxi.val <= root.val :
                return False
            if mini and mini.val >= root.val :
                return False
            return valid(root.left,mini,root) and valid(root.right,root,maxi)
        return valid(root,None,None)