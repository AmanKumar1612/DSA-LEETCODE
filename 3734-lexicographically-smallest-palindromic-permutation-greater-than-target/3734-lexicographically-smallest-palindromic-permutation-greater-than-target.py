from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        m = n // 2
        freq = Counter(s)
        
        # Check if a palindromic permutation is possible
        odd_chars = [ch for ch, cnt in freq.items() if cnt % 2 != 0]
        if (n % 2 == 0 and len(odd_chars) != 0) or (n % 2 == 1 and len(odd_chars) != 1):
            return ""
        
        mid_char = odd_chars[0] if n % 2 == 1 else ""
        
        # Half counts available to build the first half
        half_counts = {ch: freq[ch] // 2 for ch in freq}
        
        def build_palindrome(first_half: list) -> str:
            first_str = "".join(first_half)
            return first_str + mid_char + first_str[::-1]
        
        # 1. Try matching target[:m] exactly
        can_match = True
        needed = Counter(target[:m])
        for ch, cnt in needed.items():
            if half_counts.get(ch, 0) < cnt:
                can_match = False
                break
                
        if can_match:
            cand = build_palindrome(list(target[:m]))
            if cand > target:
                return cand

        # 2. Find the largest index i (from m - 1 down to 0) to diverge with char > target[i]
        curr_counts = Counter()
        for i in range(m):
            curr_counts[target[i]] += 1
            
        for i in range(m - 1, -1, -1):
            # Remove target[i] so curr_counts represents target[:i]
            curr_counts[target[i]] -= 1
            
            # Check if prefix target[:i] is valid
            valid_prefix = all(half_counts.get(ch, 0) >= curr_counts[ch] for ch in curr_counts)
            if not valid_prefix:
                continue
            
            # Available counts remaining for index i and beyond
            remaining = {}
            for ch in half_counts:
                rem = half_counts[ch] - curr_counts[ch]
                if rem > 0:
                    remaining[ch] = rem
            
            # Try to place the smallest char strictly greater than target[i]
            for o in range(ord(target[i]) + 1, ord('z') + 1):
                c = chr(o)
                if remaining.get(c, 0) > 0:
                    # Construct the first half
                    first_half = list(target[:i]) + [c]
                    remaining[c] -= 1
                    
                    # Fill the rest with smallest available characters
                    for ch in sorted(remaining.keys()):
                        first_half.extend([ch] * remaining[ch])
                    
                    return build_palindrome(first_half)
                    
        return ""