from collections import Counter
class Solution:

  def maxSubarrayLength(self, nums: List[int], k: int) -> int:
    freq = Counter()
    left = 0
    invalid_count = 0

    for right in range(len(nums)):
      # Increment frequency of right element
      freq[nums[right]] += 1
      if freq[nums[right]] == k + 1:
        invalid_count += 1

      # If the current window contains invalid elements, shift left by 1
      if invalid_count > 0:
        if freq[nums[left]] == k + 1:
          invalid_count -= 1
        freq[nums[left]] -= 1
        left += 1

    return len(nums) - left