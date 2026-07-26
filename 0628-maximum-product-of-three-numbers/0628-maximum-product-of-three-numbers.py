class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        a=nums[0]
        b=nums[1]
        x=nums[-1]
        y=nums[-2]
        z=nums[-3]
        res1=a*b*x
        res2=x*y*z
        return res1 if res1>res2 else res2
