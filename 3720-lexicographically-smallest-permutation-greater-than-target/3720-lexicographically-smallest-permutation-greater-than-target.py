from collections import Counter

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)
        total_counts = Counter(s)
        
        # Track prefix counts of target to check availability quickly
        prefix_counts = [Counter()]
        for ch in target:
            new_count = prefix_counts[-1].copy()
            new_count[ch] += 1
            prefix_counts.append(new_count)
            
        # Try finding the longest matching prefix from right to left
        for i in range(n - 1, -1, -1):
            # Check if target[0...i-1] is a valid subset of s
            req = prefix_counts[i]
            if any(req[ch] > total_counts[ch] for ch in req):
                continue
            
            # Remaining characters available after using target[0...i-1]
            rem = total_counts - req
            
            # Find the smallest character strictly greater than target[i]
            target_char = target[i]
            best_char = None
            for ch in sorted(rem.keys()):
                if ch > target_char and rem[ch] > 0:
                    best_char = ch
                    break
            
            if best_char is not None:
                # Deduct best_char and construct the smallest remaining suffix
                rem[best_char] -= 1
                suffix = []
                for ch in sorted(rem.keys()):
                    suffix.append(ch * rem[ch])
                
                return target[:i] + best_char + "".join(suffix)
                
        return ""