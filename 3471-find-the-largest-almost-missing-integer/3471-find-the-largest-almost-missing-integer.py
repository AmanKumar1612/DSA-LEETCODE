class Solution:

  def largestInteger(self, nums: list[int], k: int) -> int:
    n = len(nums)
    if k == n:
      return max(nums)
    if k == 1:
      unique_elements = [x for x in nums if nums.count(x) == 1]
      return max(unique_elements) if unique_elements else -1

    candidates = []

    if nums.count(nums[0]) == 1:
      candidates.append(nums[0])

    if nums.count(nums[-1]) == 1:
      candidates.append(nums[-1])

    return max(candidates) if candidates else -1