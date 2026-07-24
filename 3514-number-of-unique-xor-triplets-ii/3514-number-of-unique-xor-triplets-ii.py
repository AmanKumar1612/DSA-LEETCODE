class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        u = set(nums)
        s2 = {a ^ b for a in u for b in u}
        s3 = {a ^ b for a in s2 for b in u}
        return len(s3)