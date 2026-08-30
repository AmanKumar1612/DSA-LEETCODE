class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n

        x = nums.index(min(nums))
        y = nums.index(max(nums))

        i, j = min(x, y), max(x, y)

        return min(j + 1,n - i,(i + 1) + (n - j))