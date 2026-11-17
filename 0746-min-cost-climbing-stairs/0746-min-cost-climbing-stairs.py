class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        dp=[0,0] 
        n=len(cost)
        
        for i in range(2,n+1):
            dp.append(min(dp[i-2]+cost[i-2],dp[i-1]+cost[i-1]))
        return dp[-1]