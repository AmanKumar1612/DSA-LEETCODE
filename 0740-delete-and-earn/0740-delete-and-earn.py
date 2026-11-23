class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        n=max(nums)
        dp=[0]*(n+1)
        for i in nums:
            dp[i]+=i
        for i in range(2,n+1):
            dp[i]=max(dp[i-1],dp[i-2]+dp[i])
        return dp[-1]