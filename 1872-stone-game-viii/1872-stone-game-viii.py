from itertools import accumulate
from typing import List


class Solution:

  def stoneGameVIII(self, stones: List[int]) -> int:
    pref = list(accumulate(stones))
    n = len(stones)

    dp = pref[-1]

    for i in range(n - 2, 0, -1):
      dp = max(dp, pref[i] - dp)

    return dp