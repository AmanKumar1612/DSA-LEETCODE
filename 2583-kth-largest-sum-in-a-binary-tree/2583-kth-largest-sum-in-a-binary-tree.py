# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        queue=[]
        x=[]
        s=0
        queue.append("no")
        queue.append(root)
        
        while len(queue) > 0:
            if queue[0]=="no":
                for i in queue:
                    if i is not "no" and i is not None:
                        s+=i.val
                x.append(s)
                s=0
            
            a=queue.pop(0)
            if a=="no":
                if len(queue) == 0:
                    break
                queue.append("no")
            else:
                if a.left is not None:
                    queue.append(a.left)
                if a.right is not None:
                    queue.append(a.right)
        x.sort()
        if k>=len(x):
            return -1
        
        return x[-k] 
