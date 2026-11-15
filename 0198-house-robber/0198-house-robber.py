class Solution:
    def rob(self, nums: list[int]) -> int:
        h1=0
        h2=0
        for i in nums:
            curr=max(h1,h2+i)
            h2=h1
            h1=curr
        return h1