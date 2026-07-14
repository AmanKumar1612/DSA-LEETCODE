import math
from typing import List

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        max_val = max(nums)
        
        # dp[g1][g2] stores the count of subsequence pairs with GCDs g1 and g2
        # Size is (max_val + 1) x (max_val + 1)
        dp = {}
        # Base case: both subsequences are empty (represented by GCD 0)
        dp[(0, 0)] = 1
        
        for x in nums:
            next_dp = dp.copy()
            
            for (g1, g2), count in dp.items():
                # Option 1: Add x to seq1
                new_g1 = x if g1 == 0 else math.gcd(g1, x)
                next_dp[(new_g1, g2)] = (next_dp.get((new_g1, g2), 0) + count) % MOD
                
                # Option 2: Add x to seq2
                new_g2 = x if g2 == 0 else math.gcd(g2, x)
                next_dp[(g1, new_g2)] = (next_dp.get((g1, new_g2), 0) + count) % MOD
                
            dp = next_dp
            
        # Sum up all pairs where g1 == g2 and both are non-empty (> 0)
        ans = 0
        for g1 in range(1, max_val + 1):
            if (g1, g1) in dp:
                ans = (ans + dp[(g1, g1)]) % MOD
                
        return ans