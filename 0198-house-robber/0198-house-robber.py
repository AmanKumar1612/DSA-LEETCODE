class Solution:
    def rob(self, nums: list[int]) -> int:
        n=len(nums)
        dp={n:0,n+1:0}
        def fun(i):
            if i in dp:
                return dp[i]
            dp[i]=max(nums[i]+fun(i+2),fun(i+1))
            return dp[i]
        return fun(0)


        