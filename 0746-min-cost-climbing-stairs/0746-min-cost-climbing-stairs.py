class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n=len(cost)
        dp={0:0,1:0}
        def fun(i):
            if i in dp:
                return dp[i]
            take1=cost[i-1] + fun(i-1)
            take2=cost[i-2] + fun(i-2)
            dp[i]=min(take1,take2)
            return dp[i]
       
        return fun(n)