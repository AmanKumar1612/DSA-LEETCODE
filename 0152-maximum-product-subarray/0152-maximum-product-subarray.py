class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prod =nums[0]
        m=1
        n=1
        for i in nums:
            t=m*i
            m=max(i,t,n*i)
            n=min(i,n*i,t)
            prod=max(prod,m)
        return prod