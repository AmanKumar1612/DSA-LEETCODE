from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        # Step 1: Count frequency of each character
        freqs = Counter(word)
        
        # Step 2: Sort frequencies in descending order
        sorted_counts = sorted(freqs.values(), reverse=True)
        
        total_pushes = 0
        
        # Step 3: Calculate cost based on position multiplier
        for i, count in enumerate(sorted_counts):
            pushes_per_press = (i // 8) + 1
            total_pushes += count * pushes_per_press
            
        return total_pushes