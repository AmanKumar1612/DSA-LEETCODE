class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n=len(nums)
        seen=set()
        dup=-1
        for x in nums:
            if x in seen:
                dup=x
            seen.add(x)
        missing=(n*(n+1) //2)-(sum(nums)-dup)
        return [dup,missing]