# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def LCA(root,n,l) -> list:
            if root is None:
                return False
            l.append(root)
            if root == n:
                return True
            if LCA(root.left,n,l) or LCA(root.right,n,l):
                return True
            l.pop()
            return False
        x,y=[],[]   
        LCA(root,p,x)
        LCA(root,q,y)
        ca=0
        for i in range(min(len(x),len(y))):
            if x[i]==y[i]:
                ca=x[i]
            else:
                break
        return ca