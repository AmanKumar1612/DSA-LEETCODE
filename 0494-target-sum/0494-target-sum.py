class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        n=len(nums)
        memo={}
        def fun(i,s):
            if (i,s) in memo:
                return memo[(i,s)]
            if i==n:
                
                if s==target:
                    return 1
                return 0
            memo[(i,s)]= fun(i+1,s+nums[i]) + fun(i+1,s-nums[i])
            return memo[(i,s)]
        
        return fun(0,0)