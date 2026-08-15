class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        total_xor=0
        for i in nums:
            total_xor=total_xor ^ i
        if total_xor !=0:
            return len(nums)
        elif total_xor ==0:
            if sum(nums) == 0:
                return 0
            else:
                return len(nums)-1