class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        a=0
        b=0 
        n=len(cost)
        s=0
        for i in range(2,n+1):
            s=min((a+cost[i-2]),(b+cost[i-1]))
            a=b
            b=s
            
        return b