from collections import defaultdict
from typing import List

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        # Map each row to a bitmask of reserved seats (focusing on seats 2 to 9)
        occupied = defaultdict(int)
        for row, col in reservedSeats:
            if 2 <= col <= 9:
                occupied[row] |= (1 << (col - 2))
        
        # Any row not in occupied can accommodate 2 families
        ans = (n - len(occupied)) * 2
        
        left_mask = 0b00001111
        right_mask = 0b11110000
        middle_mask = 0b00111100
        
        for mask in occupied.values():
            can_left = (mask & left_mask) == 0
            can_right = (mask & right_mask) == 0
            can_middle = (mask & middle_mask) == 0
            
            if can_left and can_right:
                ans += 2
            elif can_left or can_right or can_middle:
                ans += 1
                
        return ans