class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        # Step 1: Calculate the sum of the longest sequential prefix
        seq_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                seq_sum += nums[i]
            else:
                break
        
        # Step 2: Use a hash set for O(1) lookups to find the smallest missing integer
        num_set = set(nums)
        while seq_sum in num_set:
            seq_sum += 1
            
        return seq_sum