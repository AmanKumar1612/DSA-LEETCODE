class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        x=1
        while True:
            if x*k not in nums:
                return x*k
            x=x+1