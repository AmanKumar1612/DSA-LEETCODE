class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr=nums[0]
        m=nums[0]
        for i in nums[1:]:
            curr=max(i,curr+i)
            m=max(m,curr)
        return m
            
