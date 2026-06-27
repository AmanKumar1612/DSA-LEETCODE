from collections import Counter

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        count = Counter(nums)
        ans = 0
        
        # Handle the edge case for 1 separately since 1^2 = 1
        if 1 in count:
            c1 = count[1]
            if c1 % 2 == 0:
                ans = c1 - 1
            else:
                ans = c1
        
        # Check for all other bases > 1
        for x in count:
            if x == 1:
                continue
                
            current_len = 0
            curr = x
            
            while curr in count and count[curr] >= 2:
                current_len += 2
                curr = curr * curr
                
            # The peak element of the pattern only needs to appear at least once
            if curr in count:
                current_len += 1
            else:
                current_len -= 1
                
            ans = max(ans, current_len)
            
        return ans