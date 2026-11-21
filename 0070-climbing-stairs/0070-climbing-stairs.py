class Solution:
    def climbStairs(self, n: int) -> int:
        dp={1:1,2:2}
        def check(i):
            if i in dp:
                return dp[i]
            dp[i]=check(i-1)+check(i-2)
            return dp[i]
        return check(n)