class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        s = "123456789"
        res = []
        
        low_len = len(str(low))
        high_len = len(str(high))
        
        # Iterate over all possible lengths of numbers
        for length in range(low_len, high_len + 1):
            # Slide a window of 'length' across the string 's'
            for start in range(10 - length):
                num = int(s[start:start + length])
                if low <= num <= high:
                    res.append(num)
                    
        return res