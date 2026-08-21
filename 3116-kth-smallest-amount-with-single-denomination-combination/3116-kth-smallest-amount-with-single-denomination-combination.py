import math
from itertools import combinations
from typing import List

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        # Precompute LCM and sign for all non-empty subsets
        subsets = []
        n = len(coins)
        for size in range(1, n + 1):
            sign = 1 if size % 2 == 1 else -1
            for combo in combinations(coins, size):
                lcm_val = combo[0]
                for c in combo[1:]:
                    lcm_val = math.lcm(lcm_val, c)
                subsets.append((lcm_val, sign))

        # Helper function to count distinct amounts <= m
        def count_up_to(m: int) -> int:
            total = 0
            for lcm_val, sign in subsets:
                total += sign * (m // lcm_val)
            return total

        # Binary search for the smallest m where count_up_to(m) >= k
        left = 1
        right = min(coins) * k
        ans = right

        while left <= right:
            mid = (left + right) // 2
            if count_up_to(mid) >= k:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1

        return ans