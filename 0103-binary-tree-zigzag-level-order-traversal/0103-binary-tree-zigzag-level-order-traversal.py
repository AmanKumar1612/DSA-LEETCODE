# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue=[]
        l=[]
        x=[]
        if root is not None:
            queue.append(root)
            queue.append(None)
        while queue:
            n=queue.pop(0)
            if n is not None:
                x.append(n.val)
                if n.left is not None:
                    queue.append(n.left)
                if n.right is not None:
                    queue.append(n.right)
            else:
                if len(l) % 2 == 0: 
                    l.append(x)
                else:
                    l.append(x[::-1])
                x=[]
                if queue:
                    queue.append(None)
        return l