class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        if s.count('1') < k:
            return ""
        
        n = len(s)
        ans = ""
        min_len = float('inf')
        
        # Collect all indices where '1' occurs
        ones_indices = [i for i, ch in enumerate(s) if ch == '1']
        
        # A valid substring with exactly k ones will start at ones_indices[i] 
        # and end at ones_indices[i + k - 1]
        for i in range(len(ones_indices) - k + 1):
            start = ones_indices[i]
            end = ones_indices[i + k - 1]
            sub = s[start:end + 1]
            curr_len = len(sub)
            
            if curr_len < min_len:
                min_len = curr_len
                ans = sub
            elif curr_len == min_len:
                ans = min(ans, sub)
                
        return ans