from collections import deque
from typing import List


class Solution:

  def lexicographicallySmallestArray(
      self, nums: List[int], limit: int
  ) -> List[int]:
    sorted_nums = sorted(nums)

    groups = []  # List of deques, each containing sorted values in that group
    num_to_group = {}  # Maps a number to its group index

    group_idx = 0
    groups.append(deque([sorted_nums[0]]))
    num_to_group[sorted_nums[0]] = group_idx

    for i in range(1, len(sorted_nums)):
      if sorted_nums[i] - sorted_nums[i - 1] > limit:
        group_idx += 1
        groups.append(deque())

      groups[group_idx].append(sorted_nums[i])
      num_to_group[sorted_nums[i]] = group_idx

    # Reconstruct the result array
    result = []
    for x in nums:
      gid = num_to_group[x]
      result.append(groups[gid].popleft())

    return result