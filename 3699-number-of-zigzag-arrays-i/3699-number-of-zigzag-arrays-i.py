class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        M = r - l + 1
        
        if n == 1:
            return M
            
        dp = [[1] * M for _ in range(2)]
            
        for _ in range(2, n + 1):
            next_dp = [[0] * M for _ in range(2)]
            
            pref = 0
            for y in range(M):
                next_dp[1][y] = pref % MOD
                pref += dp[0][y]
                
            suff = 0
            for y in range(M - 1, -1, -1):
                next_dp[0][y] = suff % MOD
                suff += dp[1][y]
                
            dp = next_dp
            
        return (sum(dp[0]) + sum(dp[1])) % MOD