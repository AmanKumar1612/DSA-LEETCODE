class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        x=len(nums)
        c=0
        while i<x:
            if nums[i]==0:
                nums.pop(i)
                c=c+1
                x=x-1
            else:
                i=i+1
        for i in range(c):
            nums.append(0)