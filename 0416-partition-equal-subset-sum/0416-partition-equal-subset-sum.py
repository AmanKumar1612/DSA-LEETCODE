class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        s=sum(nums)
        n=len(nums)
        dp=[{} for _ in range(n+1)]
        def fun(i,S):
            
            if  S in dp[i]:
                return dp[i][S]
            if i==n or S > s//2:
                return False
            if (s-S)==S   or (S == s//2 and s % 2 ==0):

                return True
                
            dp[i][S]= fun(i+1,S+nums[i]) or fun(i+1,S)
            if dp[i][S]:
                return True
            return False
        return fun(0,0)
        