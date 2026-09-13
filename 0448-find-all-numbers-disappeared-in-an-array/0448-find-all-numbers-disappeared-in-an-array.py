class Solution:

  def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
    for x in nums:
      idx = abs(x) - 1
      if nums[idx] > 0:
        nums[idx] = -nums[idx]

    return [i + 1 for i in range(len(nums)) if nums[i] > 0]