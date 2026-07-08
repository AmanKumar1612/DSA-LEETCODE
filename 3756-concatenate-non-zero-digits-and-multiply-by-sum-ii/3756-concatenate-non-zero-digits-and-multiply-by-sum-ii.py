class Solution:
    def sumAndMultiply(self, s: str, queries: list[list[int]]) -> list[int]:
        MOD = 10**9 + 7
        
        # 1. Filter out non-zero digits and track their original string indices
        nonzero_digits = []
        nonzero_indices = []
        for i, ch in enumerate(s):
            if ch != '0':
                nonzero_digits.append(int(ch))
                nonzero_indices.append(i)
                
        n = len(nonzero_digits)
        if n == 0:
            return [0] * len(queries)
            
        # 2. Precompute Prefix Concatenation and Digit Sums
        pref_val = [0] * (n + 1)
        pref_sum = [0] * (n + 1)
        for i in range(n):
            pref_val[i + 1] = (pref_val[i] * 10 + nonzero_digits[i]) % MOD
            pref_sum[i + 1] = pref_sum[i] + nonzero_digits[i]
            
        # 3. Precompute Powers of 10 modulo MOD
        pow10 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD
            
        # 4. Process Queries efficiently using binary search (bisect)
        from bisect import bisect_left, bisect_right
        ans = []
        
        for l, r in queries:
            # Find the range of non-zero elements that fall within [l, r]
            idx_start = bisect_left(nonzero_indices, l)
            idx_end = bisect_right(nonzero_indices, r) - 1
            
            if idx_start > idx_end:
                ans.append(0)
                continue
                
            # Get the actual number x formed by the range [idx_start, idx_end]
            length = idx_end - idx_start + 1
            x = (pref_val[idx_end + 1] - pref_val[idx_start] * pow10[length]) % MOD
            
            # Get the sum of digits in that range
            current_sum = pref_sum[idx_end + 1] - pref_sum[idx_start]
            
            ans.append((x * current_sum) % MOD)
            
        return ans