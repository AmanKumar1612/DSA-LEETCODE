from typing import List
import math
import bisect

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        max_val = max(nums)
        
        # Count frequencies of each number
        count = [0] * (max_val + 1)
        for num in nums:
            count[num] += 1
            
        # gcd_count[g] will store the number of pairs with exact GCD equal to g
        gcd_count = [0] * (max_val + 1)
        
        # Iterate backwards from max_val down to 1
        for g in range(max_val, 0, -1):
            # Count how many numbers in nums are multiples of g
            multiples = 0
            for m in range(g, max_val + 1, g):
                multiples += count[m]
            
            # Total possible pairs formed by multiples of g
            total_pairs = multiples * (multiples - 1) // 2
            
            # Remove pairs whose actual GCD is a strict multiple of g (Inclusion-Exclusion)
            minus_pairs = 0
            for m in range(2 * g, max_val + 1, g):
                minus_pairs += gcd_count[m]
                
            gcd_count[g] = total_pairs - minus_pairs

        # Compute prefix sums of the GCD pair counts
        prefix_sums = []
        current_sum = 0
        gcd_values = []
        
        for g in range(1, max_val + 1):
            if gcd_count[g] > 0:
                current_sum += gcd_count[g]
                prefix_sums.append(current_sum)
                gcd_values.append(g)
                
        # Answer each query using binary search (bisect_right)
        ans = []
        for q in queries:
            idx = bisect.bisect_right(prefix_sums, q)
            ans.append(gcd_values[idx])
            
        return ans