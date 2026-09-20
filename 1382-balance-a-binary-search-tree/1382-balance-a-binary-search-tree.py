# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode | None) -> TreeNode | None:
        def create(arr,mini,maxi):
            if mini > maxi:
                return
            mid=(mini+maxi)//2
            node=TreeNode(arr[mid])
            node.left=create(arr,mini,mid-1)
            node.right=create(arr,mid+1,maxi)
            return node
        def inorder(root,arr):
            if not root:
                return
            inorder(root.left,arr)
            
            arr.append(root.val)
            inorder(root.right,arr)
        arr=[]
        inorder(root,arr)
        return create(arr,0,len(arr)-1)