from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        n = len(s)
        half_len = n // 2
        
        # Count frequency of each character in s
        full_counts = Counter(s)
        
        # Determine half frequencies and middle character (if length is odd)
        half_counts = [0] * 26
        mid_char = ""
        
        for ch, count in full_counts.items():
            idx = ord(ch) - ord('a')
            half_counts[idx] = count // 2
            if count % 2 == 1:
                mid_char = ch
                
        # Helper function to compute combinations C(n, r) capped at cap
        def get_combinations(n: int, r: int, cap: int) -> int:
            r = min(r, n - r)
            if r <= 0:
                return 1
            comb = 1
            for i in range(1, r + 1):
                comb = comb * (n - r + i) // i
                if comb > cap:
                    return cap
            return comb

        # Helper function to count multinomial permutations capped at cap
        def count_ways(freqs: list, cap: int) -> int:
            total = sum(freqs)
            res = 1
            for f in freqs:
                if f == 0:
                    continue
                comb = get_combinations(total, f, cap)
                res *= comb
                if res > cap:
                    return cap
                total -= f
            return res

        # Check if total distinct palindromic permutations is less than k
        total_possible = count_ways(half_counts, k)
        if total_possible < k:
            return ""

        # Construct the first half character by character
        first_half = []
        
        for _ in range(half_len):
            for c in range(26):
                if half_counts[c] > 0:
                    # Temporarily pick character c
                    half_counts[c] -= 1
                    ways = count_ways(half_counts, k)
                    
                    if ways >= k:
                        # Fix character c at the current position
                        first_half.append(chr(ord('a') + c))
                        break
                    else:
                        # Skip these combinations and adjust k
                        k -= ways
                        half_counts[c] += 1

        first_half_str = "".join(first_half)
        second_half_str = first_half_str[::-1]
        
        return first_half_str + mid_char + second_half_str