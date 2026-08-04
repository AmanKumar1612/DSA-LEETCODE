class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        a=nums[0]
        b=nums[-1]
        x=[]
        while a<b:
            a=a+1
            if a not in nums:
                x.append(a)
        return x
