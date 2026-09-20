# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:
        def create(arr,mini,maxi):
            if mini > maxi:
                return
            mid=(mini+maxi)//2
            node=TreeNode(nums[mid])
            node.left=create(arr,mini,mid-1)
            node.right=create(arr,mid+1,maxi)
            return node
        return create(nums,0,len(nums)-1)
