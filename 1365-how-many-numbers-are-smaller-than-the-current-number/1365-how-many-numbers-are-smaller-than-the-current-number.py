class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr=[]
        a=0
        while a<len(nums):
            l=0
            for i in nums:
                if nums[a] > i :
                    l=l+1
            arr.append(l)
            a=a+1
        return arr