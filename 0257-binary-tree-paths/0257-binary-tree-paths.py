# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:
        arr=[]
        s=''
        def travel(root,s,arr):
            if not root:
                return
            s+=str(root.val)
            if root.left is not None or root.right is not None:
                s+='->'
            if root.left is None and root.right is None:
                arr.append(s)
            
            travel(root.left,s,arr)
            
            travel(root.right,s,arr)
            
        travel(root,s,arr)
        return arr